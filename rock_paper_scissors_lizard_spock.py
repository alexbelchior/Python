import random
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

#Regra
    #Rock ganha Lizard
    #Rock ganha Scissors
    #Spock ganha Scissors
    #Spock ganha Rock
    #Paper ganha Rock
    #Paper ganha Spock
    #Lizard ganha Spock
    #Lizard ganha Paper
    #Scissors ganha Paper
    #Scissors ganha Lizard

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if (name == 'rock'):
        return 0
    elif (name == 'Spock'):
        return 1
    elif (name == 'paper'):
        return 2
    elif (name == 'lizard'):
        return 3
    elif (name == 'scissors'):
        return 4
    else:
        return 'Erro'
    
def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if (number == 0):
        return 'rock'
    elif (number == 1):
        return 'Spock'
    elif (number == 2):
        return 'paper'
    elif (number == 3):
        return 'lizard'
    elif (number == 4):
        return 'scissors'
    else:
        return 'Desconhecido'
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    print 'Players choice '+ player_choice

    player_number = name_to_number(player_choice)
   
    comp_number = random.randrange(0,5)
    
    comp_choice = number_to_name(comp_number)
    
    print 'Computer choice '+ comp_choice
    
    resultado = player_number - comp_number
    
    print resultado
    
    if (resultado == 1) or (resultado == 2):
        print 'Human player wins'
    elif (resultado == 0):
        print 'Empate'
    else:
        print 'Computer wins'

    print ''

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

