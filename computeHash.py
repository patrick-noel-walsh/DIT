import os
import os.path
import time
import hashlib
import sys

# constants
UTF_CODE = "utf-16"
EXIT_HASH_CODE = "5"

#global variables
global hashCodeDesc

# start clearScreen
def clearScreen():
  os.system('cls')    # For Windows
  os.system('clear')  # For Linux/OS X
  return
# end clearScreen

# start - errorMessage
def errorMessage(message):
  print(message)
  time.sleep(1)

  return
# end - errorMessage

# start getHashCode
def getHashCode():
  # global variable used to indicate that the user has selected to exit
#  global EXIT_HASH_CODE

#  EXIT_HASH_CODE = "5"

  menuOption = 0
  # keep looking for input until a valid entry is made
  while menuOption not in ("1","2","3","4","5"):
    clearScreen();

    # display the available hash codes
    print("Available Hash Codes")
    print("====================")
    print("")
    print("1. SHA-1")
    print("2. SHA-256")
    print("3. SHA-512")
    print("4. SHA-384")
    print("5. Quit")
    print("")
    print("Select Menu Option (1-5):")

    # get the user input
    menuOption=input()

    # check that a valid option is selected
    if menuOption not in ("1","2","3","4","5"):
      errorMessage("Invalid Option - please select 1-5")

  return menuOption
# end getHashCode

# start - getInputString
def getInputString():
  clearScreen();

  # get the string to hash
  inputString = input("Input String to Check: ")

  return inputString
# end - getInputString

# start - getFileName
def getFileName():
  clearScreen();

  # get the name of the file to hash
  fileName = input("Input File Name to Check: ")

  return fileName
# end - getFileName


# start - calculateHash
def calculateHash(encodedInput, hashCode):
  # global variable used in the display results function
  global hashCodeDesc

  if hashCode == "1":
    # calculate the message digest using SHA1
    messageDigest = hashlib.sha1(encodedInput)

    # set the global variable for the display results function
    hashCodeDesc = "SHA-1"

  elif hashCode == "2":
    # calculate the message digest using SHA256
    messageDigest = hashlib.sha256(encodedInput)

    # set the global variable for the display results function
    hashCodeDesc = "SHA-256"

  elif hashCode == "3":
    # calculate the message digest using SHA512
    messageDigest = hashlib.sha512(encodedInput)

    # set the global variable for the display results function
    hashCodeDesc = "SHA-512"

  elif hashCode == "4":
    # calculate the message digest using SHA-384
    messageDigest = hashlib.sha384(encodedInput)

    # set the global variable for the display results function
    hashCodeDesc = "SHA-384"

  # convert the hash object to a hex string
  hexString = messageDigest.hexdigest()

  return hexString
# end - calculateHash

# start - getFileContents
def getFileContents(fileName):

  # open the file
  fileOpen = open(fileName,'rb')

  # read the contents into a byte array
  fileContents = fileOpen.read()
 
  return fileContents
# end - getFileContents

# start - displayResults
def displayResults(inputVar, hashCodeMenu, hashString):
  clearScreen();

  # display the results
  print("Input    = ", inputVar)
  print("Hashcode = ", hashCodeMenu, "->", hashCodeDesc)
  print("Result   = ", hashString)
  print("")

  # wait for the user to press <Return>
  tmp = input("Press Enter to Continue")

  return
# end - displayResults


# start - calculateTheHashOfAString
def calculateTheHashOfAString():
    # get the string to hash
    inputString = getInputString()

    # get the hash code the user wants to use
    hashCode = getHashCode()

    # check if the user has selected to exit
    if hashCode != EXIT_HASH_CODE:
      
      # compute the hash of the string using the seleced code
      # note - string must be UTF encoded
      hashString  = calculateHash(inputString.encode(UTF_CODE), hashCode)

      # display the results of the hash
      displayResults (inputString, hashCode, hashString)

    return
# end - calculateTheHashOfAString

# start - calculateTheHashOfAFile
def calculateTheHashOfAFile():
  # get the filename to hash
  fileName = getFileName()

  # check if the file exists
  if os.path.exists(fileName):
    # get the hash code the user wants to use
    hashCode = getHashCode()

    # check if the user has selected to exit
    if hashCode != EXIT_HASH_CODE:
      # read the contents of the file into a string
      fileContents = getFileContents(fileName)

      # compute the hash of the string using the seleced code
      hashString = calculateHash(fileContents, hashCode)

      # display the results of the hash
      displayResults(fileName, hashCode, hashString)

  else:
    # file input by the user does not exist
    errorMessage("File Does Not Exist!")

  return 
# end calculateTheHashOfAFile

# start - getMainMenuOption
def getMainMenuOption():
  menuOption = 0
  # keep looking for input until a valid entry is made
  while menuOption not in ("1","2","3"):
    clearScreen();

    # display the menu
    print("Main Menu")
    print("=========")
    print("1. Input String")
    print("2. Input Filename")
    print("3. Quit")
    print("")
    print("Select Menu Option (1-3):")

    # read input from user
    menuOption=input()

    # check if the option is valid
    if menuOption not in ("1","2","3"):
      errorMessage("Invalid Option - please select 1-3")

  return menuOption 
# end getMainMenuOption

    
# start - main

# check what version of python is running
if sys.version_info[0] < 3:
    errorMessage("Must be using Python 3")
    sys.exit()

# main loop
option="0"
while option!="3":
  option = getMainMenuOption()  

  if option=="1": 
    calculateTheHashOfAString()

  elif option=="2":
    calculateTheHashOfAFile()

  elif option=="3":
    print("good bye")
    time.sleep(1)
    clearScreen()

# end - main
