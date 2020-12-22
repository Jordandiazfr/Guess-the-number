logo = ''' 

   ____                       _   _                                  _               
  / ___|_   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | |  _| | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                     

'''
import random
number = random.randint(1,100)
print("Welcome to the guessing game")
print("I'm  thinking a number between 0 and 100")
level = input("Choose a difficulty: 'easy' or 'hard' : ")
if level == 'easy':
    life = 10
else:
    life = 5
print ('psssst, the secret number is %d' %(number) )

 #funcion que juzgara el numero 
def hint(guess):
    if guess > number:
        return "Too High"
    else: 
        return "Too low"

while life > 0:
    print("You have %d attempts remainig: " %(life))
    guess = int(input("Make a guess: "))
    if guess == number:
        guessed = True
        print ("You got it right!, the secret number is %d" %(number))
        break
    else:
        print(hint(guess))  
        life-=1
        if life == 0:
            print("You have ran out of guesses, you loose. The number was: %d" %(number))


    
