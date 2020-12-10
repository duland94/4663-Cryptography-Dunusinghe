## Assignment 8 - Public Key Encryption
### Dulan Dunusinghe
### Description:
This project will use an existing python library called cryptography (appropriately named) to use public key encryption to encrypt and decrypt messages sent between two entities. We need a method to allow two scripts to "talk" or communicate over a network. This means NOT on the same computer. Using a library called Flask, we can do that. A Flask server runs and "listens" or monitors a "port" on a computer. When requests are directed to that port either from an internal request or an external request, they are handled by the process monitoring the port, or in our case Flask.

A request can either ask for information (GET) or send information (POST). There are variations of requests that imply different actions, but we will get by with GET and POST for our project. Below you see a general picture of what is happening.

There is a client/server on A and a client/server on B. Notice that the clients don't talk to their own servers! Why? They don't need to. Each process is local and can simply read or write from the local file system to communicate. However, each client does communicate with the server on the other machine.
### Files

|   #   | File                       | Description                                                |
| :---: | -------------------------- | ---------------------------------------------------------- |
|   1   | [)     | )                                             |

>I made this stuff up, so don't go reading into it to deeply


### Instructions

- This project was compiled using python


