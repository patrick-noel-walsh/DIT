# password lenhth
PWORD_LENGTH = 3

# list of characters to use in the passwords
CHARACTERS = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# recursive function to create the dictionary
def createDictionary (password, position, recursive):
   iterator = 0

   # for each character in the list
   while iterator < len(CHARACTERS):
        # get the character from the list
        char = CHARACTERS[iterator]
    
        # substitute the chacter from the list into the current password at the current position
        password = password[:position-1] + char + password[position:]
    
        if position==PWORD_LENGTH:
           # if the position is the last character in the password then print it out
           print(password)

        else:
           # otherwise call the function again increasing the position by 1
           # note: we do not allow the last recursive call
           createDictionary(password, position+1, False)
        
        iterator = iterator + 1

   # final recursive call if the position is greater than 1
   if position > 1 and recursive:
      createDictionary(password, position-1, True)

# main body

# create an initial value for the password
password = ''
while len(password) < PWORD_LENGTH:
   password = password + ' '

# start the process to create the dictionary
createDictionary(password, 1, True)



