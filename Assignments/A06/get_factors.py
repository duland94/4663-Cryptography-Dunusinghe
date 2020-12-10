import math
from typing import NamedTuple
# first let read the numbers from the file and store them as numbers in a list
def readFileData(fileName):
    try:
        fileHandler=open(fileName,'r')
    except:
        print("File is not found!")
        quit()
    
    numberList=list()   #to store the numbers

    for lines in fileHandler:
        numberList.append(int(lines))
    return numberList   #return the number list finally




# to check wheter it is a prime number and if so to get the prime factors
def getPrimeFactors(number):
    """
    The steps 1 and 2 take care of composite numbers and step 3 takes care of prime numbers. To prove that the complete algorithm works, we need to prove that steps 1 and 2 actually take care of composite numbers. This is clear that step 1 takes care of even numbers. And after step 1, all remaining prime factor must be odd (difference of two prime factors must be at least 2), this explains why i is incremented by 2.
Now the main part is, the loop runs till square root of n not till n. To prove that this optimization works, let us consider the following property of composite numbers.
Every composite number has at least one prime factor less than or equal to square root of itself.
This property can be proved using counter statement. Let a and b be two factors of n such that a*b = n. If both are greater than √n, then a.b > √n, * √n, which contradicts the expression “a * b = n”.

In step 2 of the above algorithm, we run a loop and do following in loop
a) Find the least prime factor i (must be less than √n,)
b) Remove all occurrences i from n by repeatedly dividing n by i.
c) Repeat steps a and b for divided n and i = i + 2. The steps a and b are repeated till n becomes either 1 or a prime number.



    """
    factors=list()
    # Print the number of two's that divide n 
    while number % 2 == 0: 
        factors.append(2), 
        number = number / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(number))+1,2): 
          
        # while i divides n , print i ad divide n 
        while number % i== 0: 
            factors.append(i) 
            number = number / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if number > 2: 
        factors.append(number) 
    
    return factors



dataList=list()
result=list()
dataList=readFileData('numbers.txt')





#for lines,idx in enumerate(dataList):
count=0;
for numberTocheck in dataList:
    result=getPrimeFactors(numberTocheck)
    if(len(result)==1):
        print("Number",numberTocheck,"-Prime")
    else:
        resultFactor="Number "+str(numberTocheck)+"Factors:"
        factors=""
        for x in result:
            count=count+1
            if(count!=1 and count!=len(result)+1):
                factors=factors+" * "
            factors=factors+str(x)
        print(resultFactor,factors)





