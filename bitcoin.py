#main.py

import time
import math

#TASK 1: CREATE 2 BLOCKS

print("Our first step is to create a block! ")
begin = input("Type 'begin' to begin: " )
while begin != "begin":
    begin = input("Type 'begin' to begin: " )
print("The main parts of a block are: ")
time.sleep(2)
print("id number")
time.sleep(2)
print("hash value")
time.sleep(2)
print("previous block's hash value")
time.sleep(2)
print("transaction data")
time.sleep(2)
id = int(input("Enter the id of the genesis block, or the first block: "))
while id != 1:
    id = int(input("Enter the id of the genesis block, or the first block!"))
    
print("Great! The id of the first block is 1!")
time.sleep(3)

h = int(input("Next, enter a number to serve as the hash value of the genesis block: "))
print("Awesome!")
time.sleep(2)

print("Since there is no block before the genesis block, we will set the previous block's hash value to 0.")
pH = 0
time.sleep(4)

t = input("Finally, enter the transaction information for the genesis block: ")
print("Great job!")
time.sleep(2)

print("You made a block! This is what the block contains: ")
print("ID - 1\nHASH VALUE - ", h, "\nPREVIOUS HASH VALUE - ", pH, "\nTRANSACTION DATA - ", t)
time.sleep(4)

block1 = [id, h, pH, t]

print("Let's make one more block! ")
time.sleep(3)

id = 1
while id != 2:
    id = int(input("Enter the id of the second block: "))
pH = 1
while pH != h:
    pH = int(input("Enter previous hash value: "))
h = math.floor(h * 11 / 7)
val = -1
while val != h:
    val = int(input("Enter hash value (The hash function we are using is: previous hash value * 11 / 7)"))
t = input("Enter transaction data: ")
block2 = [id, h, pH, t]
print("Fantastic!")
time.sleep(2)

print("\n\n")


print("Here is the current blockchain ledger: ")
print("ID - 1\nHASH VALUE - ", block1[1], "\nPREVIOUS HASH VALUE - ", block1[2], "\nTRANSACTION DATA - ", block1[3])
print("\/")
print("\/")
print("ID - 2\nHASH VALUE - ", block2[1], "\nPREVIOUS HASH VALUE - ", block2[2], "\nTRANSACTION DATA - ", block2[3])
time.sleep(3)

temp = block1[1]
nH = input("Now, hack into the blockchain and change the hash value of block 1: ")
block1[1] = nH
print("MODIFIED BLOCK1: ")
print("ID - 1\nHASH VALUE - ", block1[1], "\nPREVIOUS HASH VALUE - ", block1[2], "\nTRANSACTION DATA - ", block1[3])
time.sleep(2)
answer = input("Is BLOCK2's previous hash value equal to BLOCK1's hash value? ")
while answer != "no":
    answer = input("Is BLOCK2's previous hash value equal to BLOCK1's hash value? ")
print("Right! They are not equal, so something is wrong. ")
time.sleep(2)
print("According to BLOCK2, the hash value of BLOCK1 should be ", block2[2])
time.sleep(2)
print("But, the hash value of BLOCK1 is ", block1[1])
time.sleep(3)

while answer != "previous hash value":
    answer = input("What part of BLOCK2 gives us the value the correct hash value of BLOCK1? ")
print("WONDERFUL! You're doing great! ")
block1[1] = temp
time.sleep(3)

print("\n\n")

print("Here is the fixed blockchain ledger: ")
print("ID - 1\nHASH VALUE - ", block1[1], "\nPREVIOUS HASH VALUE - ", block1[2], "\nTRANSACTION DATA - ", block1[3])
print("\/")
print("\/")
print("ID - 2\nHASH VALUE - ", block2[1], "\nPREVIOUS HASH VALUE - ", block2[2], "\nTRANSACTION DATA - ", block2[3])
time.sleep(3)
    
print("Let's add a third block!")
time.sleep(3)
print("Before we can add another block, we have to solve the mining puzzle and show proof-of-work.")
time.sleep(5)
print("To solve the puzzle, find the correct input to produce a particular output. ")
time.sleep(4)
print("The output is 15. There are 30 possible inputs (1 - 30).")
time.sleep(4)
val = 27
nVal = 1
while nVal != 18:
    nVal = int(input("Enter an input: "))

print("You found the right input! 18 outputs 15.")
time.sleep(3)

print("Now, a third block can be added.")
time.sleep(3)

id = 1
while id != 3:
    id = int(input("Enter the id of the third block: "))
pH = 1
while pH != h:
    pH = int(input("Enter previous hash value: "))
h = math.floor(h * 11 / 7)
val = -1
while val != h:
    val = int(input("Enter hash value (The hash function we are using is: previous hash value * 11 / 7)"))
t = input("Enter transaction data: ")
block3 = [id, h, pH, t]
print("Fantastic!")
time.sleep(3)

print("\n\n")

print("Here is the current blockchain ledger: ")
print("ID - 1\nHASH VALUE - ", block1[1], "\nPREVIOUS HASH VALUE - ", block1[2], "\nTRANSACTION DATA - ", block1[3])
print("\/")
print("\/")
print("ID - 2\nHASH VALUE - ", block2[1], "\nPREVIOUS HASH VALUE - ", block2[2], "\nTRANSACTION DATA - ", block2[3])
print("\/")
print("\/")
print("ID - 3\nHASH VALUE - ", block3[1], "\nPREVIOUS HASH VALUE - ", block3[2], "\nTRANSACTION DATA - ", block3[3])
time.sleep(4)

#TASK 4: VERIFY BLOCKS

print("Now, we are going to create a peer-to-peer network. ")
time.sleep(4)
print("This kind of network contains nodes. ")
time.sleep(3)
print("A node is a computer that stores a copy of the blockchain. ")
time.sleep(4)
print("Let's create the first node. ")
time.sleep(3)
node1 = str(block1[1]) + "_" + str(block2[1]) + "_" + str(block3[1])
node2 = str(block1[1]) + "_" + str(block2[1]) + "_" + str(block3[1])
node3 = str(block1[1]) + "_" + str(block2[1]) + "_" + str(block3[1])
inVal = "null"
while inVal != node1:
    inVal = input("Enter the hash values of each block, separating them by an underscore: ")
print("Great! Now do the same thing to make another node: ")
time.sleep(2)
inVal = "null"
while inVal != node2:
    inVal = input("Enter the hash values of each block, separating them by an underscore: ")
print("Great! Finally, make one more copy. ")
time.sleep(2)
inVal = "null"
while inVal != node3:
    inVal = input("Enter the hash values of each block, separating them by an underscore: ")

print("Here are the three nodes that make up our network: ")
print("NODE 1: ", block1[1], block2[1], block3[1])
print("NODE 2: ", block1[1], block2[1], block3[1])
print("NODE 3: ", block1[1], block2[1], block3[1])
time.sleep(3)

temp = block2[1]
nH = int(input("Now, change the hash value of a block in one of our network nodes: "))

print("Here are the three nodes that make up our network: ")
print("NODE 1: ", block1[1], block2[1], block3[1])
print("NODE 2: ", block1[1], nH, block3[1])
print("NODE 3: ", block1[1], block2[1], block3[1])
time.sleep(2)

inVal = "null"
while inVal != "yes":
    inVal = input("Wait, is something wrong? ")

inVal = "null"
while inVal != 2:
    inVal = int(input("What node is not like the others? "))

inVal = "null"
while inVal != "no":
    inVal = input("Should we change the other nodes to match this one? ")
    
inVal = "null"
while inVal != "yes":
    inVal = input("Exactly! Should we change this node to match the other nodes?")

print("Yes! You got it! We should change this node to match the other nodes because the other nodes form the majority.")
time.sleep(5)

block2[1] = temp

print("Here are the three nodes that make up our network: ")
print("NODE 1: ", block1[1], block2[1], block3[1])
print("NODE 2: ", block1[1], block2[1], block3[1])
print("NODE 3: ", block1[1], block2[1], block3[1])
time.sleep(2)

print("GREAT JOB!!! YOU'VE CREATED A SECURE BLOCKCHAIN!")

print("\n\n")

print("Here is the current blockchain ledger: ")
print("ID - 1\nHASH VALUE - ", block1[1], "\nPREVIOUS HASH VALUE - ", block1[2], "\nTRANSACTION DATA - ", block1[3])
print("\/")
print("\/")
print("ID - 2\nHASH VALUE - ", block2[1], "\nPREVIOUS HASH VALUE - ", block2[2], "\nTRANSACTION DATA - ", block2[3])
print("\/")
print("\/")
print("ID - 3\nHASH VALUE - ", block3[1], "\nPREVIOUS HASH VALUE - ", block3[2], "\nTRANSACTION DATA - ", block3[3])

print("\n\nGoodbye!")
    





    









