import requests
from crypto_class import Crypto
from cryptography.hazmat.primitives import serialization  # store  and read the keys
import base64

# GLOBAL Variables

TOKEN = '683f38ebb3369471fadef97392f05c4a'
UID = '5256700'
API = 'http://msubackend.xyz/api/?route='
USERS = {}  # to stoe the users after reading server data
KEYS = {}  # to store the public keys of all the users


def loadPubKey(pubkey):
    return serialization.load_pem_public_key(pubkey)


# to publish our public key to the server
def publishKey(pubkey):

    route = 'postPubKey'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"

    payload = {
        'pub_key': pubkey,
        'uid': UID,
        'token': TOKEN
    }

    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, json=payload)
    return r.json()


# to get all the  public keys from the server
def getPubKeys():
    global KEYS
    route = 'getPubKey'
    url = f"{API}{route}"

    r = requests.get(url)

    try:
        keys = r.json()
    except:
        print("ERROR!")
        print("Invalid Input!")
        quit()

    # get the keys and store it
    for key in keys['data']:
        KEYS[key['uid']] = key


# to get the user data from the server
def getUsers():

    global USERS
    route = 'getUser'
    url = f"{API}{route}"

    r = requests.get(url)

    users = r.json()
    for user in users['data']:
        USERS[user['uid']] = user


# to get the active users from the server
def getActiveUsers():

    route = 'getActive'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    active_users = r.json()
    active_users = active_users['data']

    real_active_users = []
    for active in active_users:
        active['fname'] = USERS[active['uid']]['fname']
        active['lname'] = USERS[active['uid']]['lname']
        active['email'] = USERS[active['uid']]['email']
        active['pubkey'] = KEYS[active['uid']]
        real_active_users.append(active)

    return real_active_users


# to encrypt and post the messages to server
def postMessage(message, to_uid):
    route = 'postMessage'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"

    # to encrypt the message lets use the Crypto class
    C = Crypto()
    # to load the public key for encryption
    C.load_keys(KEYS[to_uid]['pubkey'])
    encryptedMessage = C.encrypt(message)
    # to make sure that text is in bytes format
    Byte_text = base64.b64encode(encryptedMessage)
    message = Byte_text.decode('utf-8')

    payload = {
        'uid': UID,
        'to_uid': to_uid,
        'message': message,
        'token': TOKEN
    }

    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, json=payload)
    return r.json()


# to get messages from the server and decrypt it using keys
def getMessages():
    print("Getting Messages!!!!!")

    route = 'getMessage'
    url = f"{API}{route}&token={TOKEN}&uid={UID}&latest=true"
    r = requests.get(url)
    data = r.json()
    message = data["data"][0]  # get the latest message from the server

    # now decrypt that encrrypted messgae and show the output
    recieved = base64.b64decode(message['message'])
    print(recieved)


if __name__ == '__main__':
    # intial commands to retrieve information
    getPubKeys()
    getUsers()

   # interactive menu
    UserChoice = input(
        "\nWhat do you like to do :\n1-Check messages\n2-Send message\n3-EXIT\n")

    while (True):

        if (UserChoice == '1'):  # check for messages##########################

            # now get the latest message and decode it
            getMessages()

        elif(UserChoice == '2'):  # Send a message####################
            # get and display the active users
            active = getActiveUsers()
            print("Online Users: ")
            for a in active:
                print(a)

            uidSend = input("Enter the UID of the recipient: ")
            uidSend_firstName = USERS[uidSend]['fname']

            print("Message to ", uidSend_firstName)
            newMessage = input("Type your message here: ")

            postMessage(newMessage, uidSend)

        elif(UserChoice == '3'):
            quit()


#5256700 my uid