### Solution to Coding Exercise 1
```
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
```

### Solution to Coding Exercise 2
```
userOption = int(input('\nMake your decision. 1, 2, 3, or 4: ')) #User makes their decision
```
