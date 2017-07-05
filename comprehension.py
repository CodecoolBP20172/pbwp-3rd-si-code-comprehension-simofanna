import random   # import random module. This module acess many new operations.
                # we use this, because in line9 we want that, the computer to pick a random number between 1-20

guessesTaken = 0        # we create a variable called guessesTaken, which contains an integer value of zero:

print('Hello! What is your name?')      #print is a bulit-in fuction, witch prints the string inside the bracket.
myName = input()                        #we create a variable called myName, which equal an input form the user.

number = random.randint(1, 20)          #we create a varible called number which is equal an random integer number between 1 - 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')      # the print function prints myName(What the user specified) and combine with strings and becomes one string.

while guessesTaken < 6:                 # we create a while loop witch examine that our guessesTaken variable is a lower number than 6. While this condition is true, we enter to the loop.
    print('Take a guess.')              # if the while condition is true. the print function prints a string in witch request a guess from the user.
    guess = input()                     # the guess variable store this answer from the user. now this is a string
    guess = int(guess)                  # convert guess variable to an integer. now guess is a number.

    guessesTaken += 1                   #while guessesTaken number in a lower number than 6, increase guessesTaken by one.

    if guess < number:                  # check if the guess value(got form the user) is a lower number than our random numberVariable, enter an if statement
        print('Your guess is too low.')     # if the condition is true the program prints a string than our guess is too low.

    if guess > number:                      #this if statement start only if the guess value not a lower number than our random numberVariable.
        print('Your guess is too high.')    # if our guessVariable is a bigger number than our random numberVariable print for the user a string.

    if guess == number:                     # if the previous two if statement not true, this one will start if our guess value equal our random numberVariable.
        break                               # break statement to exit the loop immediately. return from the while loop
                                            
if guess == number:                         # check if guess value is equal with number value
    guessesTaken = str(guessesTaken)        # convert guessesTaken string into an integer
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') # and print a string chain with this two variable

if guess != number:                         # check if guess value not equal with number value
    number = str(number)                    # convert numbert value into a string
    print('Nope. The number I was thinking of was ' + number) # print out the console a string chain with value of number Variable.
