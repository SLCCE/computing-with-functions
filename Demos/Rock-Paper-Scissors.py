#Rock, Paper Scissors Game

#Modules
import random
import time

#Functions

def userChoice(userSelection): #Converts the user's choice to an item

    '''
    This function converts the user's decision between 1, 2, or 3 into a proper rock, paper, or scissors item
    '''
    
    if userSelection == 1: #Looks at what the user entered
        
        userSelection = 'Rock' #Changes variable to the item
    
    elif userSelection == 2:
        
        userSelection = 'Paper'
    
    elif userSelection == 3:
        
        userSelection = 'Scissors'
    
    return userSelection

def computerResponse(): #Computer will generate it's own choice and will be converted into an item

    '''
    This function randomly generates a number between 1, 2, or 3 and then converts it into rock, paper, or scissors
    '''

    computerChoice = random.randint(1, 3) #Randomly chooses between 1, 2, or 3
    
    if computerChoice == 1:
        
        computerChoice = 'Rock'
    
    elif computerChoice == 2:
        
        computerChoice = 'Paper'
    
    elif computerChoice == 3:
        
        computerChoice = 'Scissors'
    
    return computerChoice #Choice is saved in function call

def battle(userChoice, computerResponse): #This is where operations are done to see who won

    '''
    This function compares the choices of the user and computer in order to determine who wins the round based on the rules of rock, paper, scissor
    '''
    
    if userChoice == computerResponse:
        
        return("\nDraw!\nRound will be played again!")
    
    elif userChoice == 'Rock': #Calculates winner based on who chose what
        
        if computerResponse == 'Paper':
            
            return('\nComputer Wins!')
        
        else:
            
            return("\nPlayer 1 Wins!")
    
    elif userChoice == 'Paper':
        
        if computerResponse == 'Scissors':
            
            return('\nComputer Wins!')
        
        else:
            
            return('\nPlayer 1 Wins!')
    
    else:
        
        if computerResponse == 'Rock':
            
            return('\nComputer Wins!')
        
        else:
            
            return('\nPlayer 1 Wins!')

#Title Slide
print("Welcome to Rock, Paper, Scissors!") #Game begins

#Hidden input to start, once they press enter the code will continue

while True: #Will make the user press enter to play, if they try to break the system it will repeat

    try:
        
        userBegins = input('Press Enter to play!') #The user can enter anything they want, but they must press enter to continue
        
        break #Once the right thing is done the while loop ends
    
    except KeyboardInterrupt:
    
        continue

#Rules
print('''
The rules are simple:

Rock beats scissors

Scissors beats paper

Paper beats rock
''')

while True:

    try:
    
        userBegins = input('Press Enter to continue!')
    
        break
    
    except KeyboardInterrupt:
        
        continue

#Gameplay Explanation

print('''
Gamplay Rules:

You will play three rounds of rock, paper, scissors.

You will select one of the three items (rock, paper, or scissors) and the computer will also choose one

The winner of the round will earn 1 point and the next round will begins

If a tie occurs, neither the player nor the computer will receive a point and the round will be replayed

At the end of three rounds, whoever has the most points wins

You can choose to exit any time and the final score and winner will be decided on the score at the time

You may play as many times as you wish to, each time a new set of rounds begins, all points are set to 0
''')

while True:

    try:
    
        userBegins = input('Press Enter to continue!')
    
        break
    
    except KeyboardInterrupt:
        
        continue

#Gameplay begins

while True: #Continious loops to play multiple games
    
    userScore = 0 #Player score
    
    computerScore = 0 #Computer score
    
    numberOfRounds = 1 #Keeps track of the number of rounds, starts at 1 because the first round will be played

    while numberOfRounds < 4: #3 round maximum is set (4-1=3)
        
        print("\n\033[1;32;50m Round",numberOfRounds) #Round shown in color green
        
        print("\033[0;0;0m") #Color reverted back to normal
    
        #Dashboard View
        
        print('1. Rock\n2. Paper\n3. Scissors\n4. Exit Game')
        
        #User chooses their option
        
        while True: #Will filter out any errors that occur and give a feedback mechanism
        
            try:
    
                userOption = int(input('\nMake your decision. 1, 2, 3, or 4: ')) #User makes their decision
                
                if userOption < 1 or userOption > 4: #If the user enters something wrong, the will be prompted to start again
                    
                    raise Exception('\nInvalid Input')
                
                break
            
            except ValueError: #Will not allow alphanumeric answers or float values
                
                print('\nEnter in numerical, integer form')
                
                continue
            
            except KeyboardInterrupt: #User cannot interrupt the game
                
                print('\n\nPlease do not try to break the game')
                
                continue
            
            except Exception as e: #Catches exception raised in if statementr
                
                print(e)
                
                continue
        
        if userOption == 4: #Game will end if the user wants it to
                    
                    break
        
        userConversion = userChoice(userOption) #Converted to item
        
        #Pause
        
        print('\nThe computer is making its move...')
        
        time.sleep(1) #Time.sleep used at regular intervals to build tension and give time for the user to read the information displayed
        
        #Computer makes its choice
        
        computerConversion = computerResponse() #Computer decision made
        
        #Battle Screen
        print('\n' + userConversion,'Vs.',computerConversion) #Shows both options
        
        #Winner Screen
        
        print('\nCalculating...')
        
        time.sleep(2)
        
        winner = battle(userConversion, computerConversion) #Winner is decides
        
        print(winner) #Winner printed
        
        #Points are tallied
        
        if winner == '\nPlayer 1 Wins!':
            
            userScore += 1 #If player 1 wins their score increases by 1
            
            numberOfRounds += 1 #Number of rounds is updated
        
        elif winner == '\nDraw!\nRound will be played again!':
            
            numberOfRounds += 0 #If it is a draw then neither player wins
        
            #If no one wins then the round is replayed
        
        else:
            
            computerScore += 1 #If player 1 does not win the computer's score increases by 1
            
            numberOfRounds += 1 #Number of rounds is updated
            
        print('\nTallying points...')
            
        time.sleep(2)
        
        print('\nThe Score is now\nPlayer 1:',userScore,'\nComputer:',computerScore)
        
        print('\nPlease wait...')
        
        time.sleep(1)
        
        #Loops to start new round
    
    #Final Score is presented
    
    print('\nFinal Score!\nPlayer 1:',userScore,'\nComputer:',computerScore)
    
    #Winner is presented
    
    if userScore > computerScore:
        
        print('\nPlayer 1 Wins!')
    
    else:
        
        print('\nComputer Wins!')
    
    #User decides whether to keep playing or not
    
    while True:
    
        try:
        
            userDecision = input("\nWould you like to play again? (y/n): ").lower() #Makes sure the user is entering the correct options
            
            if userDecision == 'y' or userDecision == 'n':
                
                break
            
            else:
                
                raise Exception('\nInvalid Input')
        
        except ValueError:
            
            print('\nIncorrect Format')
            
            continue
        
        except KeyboardInterrupt:
                
                print('\n\nPlease do not try to break the game')
                
                continue
        
        except Exception as e:
            
            print(e)
            
            continue
            
    if userDecision == 'n':
        
        break #If user no longer wants to play the game will end
    
    elif userDecision == 'y':
    
        continue #If the user wants to play more the game will continue

#Ending Screen
print("\n\n\nThank You For Playing!")
