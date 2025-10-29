# Explanation of the Code

## Solution to Coding Exercise 1

This code is for the game **Rock, Paper, Scissors**.  
The function `battle(userChoice, computerResponse)` decides who wins.

1. Function Setup
   - You give `battle` two inputs: what the user picks and what the computer picks.  
   - It gives you one output: who won the round.
   - If both the user and the computer choose the same thing (Rock vs Rock, Paper vs Paper, Scissors vs Scissors),  
     the result is a tie: `"Draw! Round will be played again!"`
2. The code checks these rules with `if`, `elif`, and `else`
```python
def battle(userChoice, computerResponse): #This is where operations are done to see who won

    '''
    This function compares the choices of the user and computer in order to determine who wins the round based on the rules of rock, paper, scissor
    We pass in the user's choice and the computer's choice
    '''
    
    if userChoice == computerResponse: #If the two choices are the same, then it is a draw
        #We catch the draw up front so we don't have to manage Rock and Rock/Paper and Paper later in the code
        return("\nDraw!\nRound will be played again!")
    
    elif userChoice == 'Rock': #Calculates winner based on who chose what
        #If a user chooses Rock, then if the computer chooses Paper, they lose, but if they choose Scissors, they win
        if computerResponse == 'Paper':
            
            return('\nComputer Wins!')
        
        else: #If there is no draw and the computer did not pick Paper, then it must have chosen Scissors
            
            return("\nPlayer 1 Wins!")
    
    elif userChoice == 'Paper':
        #If a user chooses Paper, then if the computer chooses Scissors, they lose, but if they choose Rock, they win
        if computerResponse == 'Scissors':
            
            return('\nComputer Wins!')
        
        else: #If there is no draw and the computer did not pick Scissors, then it must have chosen Rock
            
            return('\nPlayer 1 Wins!')
    
    else: #If the user did not choose Rock or Paper, then the only option left is Scissors
        
        if computerResponse == 'Rock': #If the computer, picks rock then it wins
            
            return('\nComputer Wins!')
        
        else: #If there is no draw and the computer did not pick Rock, then it must have chosen Paper
            
            return('\nPlayer 1 Wins!')
```

## Solution to Coding Exercise 2

This part is about asking the user for their choice.
1. `input()` This shows a question on the screen and waits for the user to type something
2. Wrapping `input()` in `int()` allows us to take in a string and convert it to an integer
3. Then we save this result into a variable
```python
userOption = int(input('\nMake your decision. 1, 2, 3, or 4: ')) #User makes their decision
```
