import sys, getopt, crypt

# global variables used to hold the salt and the encrypted password
global salt
global encryptedPassword

# function to check if the password matches the value passed in
def passwordMatch (password):
  global salt
  global encryptedPassword

  # default to password not found
  passwordFound = False

  # caclulate the hash of the password using the salt passed in
  calcCrypt = crypt.crypt(password, salt)

  # check if the calculated hash matches what is passed in
  if calcCrypt == salt+encryptedPassword:
    passwordFound = True
     
  # print out the current password
  print(password)

  return passwordFound

# function to check all passwords in the dictionary
def checkPasswords():
  f = open('dictionary.txt')

  # read the first line of the dictinoary
  line = f.readline()

  # while there are more lines to read
  while line:
    # string out the \n from the password
    password = line.strip('\n')

    # check if this password matches what was passed in
    if passwordMatch(password):
      # if it matches then print out the password and exit the loop
      print('Password Found: ',password)
      break
    else:
      # if no match, then read the next line
      line = f.readline()

  # close the file
  f.close()

def crackPassword(argv):
   global salt
   global encryptedPassword

   # output the arguments passed in
   print ('Number of arguments:', len(sys.argv), 'arguments.')
   print ('Argument List:', str(sys.argv))

   # read the arguments from the command line
   try:
      opts, args = getopt.getopt(argv,"hs:e:")
   except getopt.GetoptError:
      print ("crackPassword.py -s '<salt>' -e <encrypted password>")
      sys.exit(2)

   # process each of the arguments to assign the global variables for the salt and the encrypted password
   for opt, arg in opts:
      if opt == '-h':
         print ("crackPassword.py -s <salt> -e <encrypted password>")
         sys.exit()
      elif opt in ("-s"):
         salt = arg
      elif opt in ("-e"):
         encryptedPassword = arg


   # print out the values for salt and password
   print ('Salt is ', salt)
   print ('Encrypted Password is ', encryptedPassword)

   # check all the passwords in the dictionary
   checkPasswords()

# main body
crackPassword(sys.argv[1:])

