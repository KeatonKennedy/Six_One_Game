# Six One Game

def SignUp():
    while True:
        ReturningUser = input('Do you have an account(Y or N): ')
        if ReturningUser.upper() == 'N':
            newName = input('Enter Username To Use: ')
            newPass = input('Enter Password To Use: ')
            with open(UsersFile, 'a') as f:
                f.write(newName + ' ' + newPass + '\n')
                break
        elif ReturningUser.upper() == 'Y':
            break
        else:
            print('Invalid Input... Try Again.')
        

def Login():
    logins = []
    logged_in1, logged_in2 = False, False
    
    with open(UsersFile) as f:
        for line in f:
            logins.append(line.strip())

    print(logins)
    while logged_in1 == False:
        count = 0
        global name1
        print('\n- Player 1 -')
        name1 = input('Enter Username: ')
        password1 = input('Enter Password: ')
        for line in logins:
            count += 1
            if line == name1 + ' ' + password1:
                print('Access Granted.')
                
                logged_in1 = True
                break
            elif count == len(logins):
                print('Incorrect Login' + '\n')
                
    while logged_in2 == False:
        count = 0
        global name2
        print('\n- Player 2 -')
        name2 = input('Enter Username: ')
        password2 = input('Enter Password: ')
        for line in logins:
            count += 1
            if line == name2 + ' ' + password2 and (name1 != name2 and password1 != password2):
                print('Access Granted.')
                logged_in2 = True
                name2
                break
            elif count == len(logins):
                print('Incorrect Login')
                            
def MainGame():
    print("\nWelcome To Six One You're Done" + '\n')
    turn = 0
    P1_Points, P2_Points = 0,0
    
    for count in range(3):
        P1_Won, P2_Won, Draw = False, False, False
        # Player 1s Turn
        total = 0
        turn += 1
        print('Turn: ' + str(turn))
        print('- ' + name1 + "'s Roll -")
        dice1 = r.randint(1,6)
        dice2 = r.randint(1,6)
        total = dice1 + dice2
        print('You Rolled: ' + str(dice1) + ' & ' + str(dice2) + ' -> +' + str(total) + ' points')
        if dice1 == 6 and dice2 == 6:
            print('Double 6!!! -> Points Set to 0!')
            total = 0
            pass
        if dice1 == dice2:
            dice3 = r.randint(1,6)
            print('Double! -> Extra Roll: ' + str(dice3))
            total += dice3
        if total % 2 == 0:
            print('Total(' + str(total) + ') is even -> +10 Points')
            total += 10
        else:
            print('Total(' + str(total) + ') is odd -> -5 Points')
            total -= 5
            if total < 0:
                total = 0
        P1_Points += total
        print('Total Points For This Round: ' + str(total))
        print('Overall Points: ' + str(P1_Points) + '\n')

        # Player 2s Turn
        total = 0
        turn += 1
        print('Turn: ' + str(turn))
        print('- ' + name2 + "'s Roll -")
        dice1 = r.randint(1,6)
        dice2 = r.randint(1,6)
        total = dice1 + dice2
        print('You Rolled: ' + str(dice1) + ' & ' + str(dice2) + ' -> +' + str(total) + ' points')
        if dice1 == 6 and dice2 == 6:
            print('Double 6!!! -> Points Set to 0!')
            total = 0
            pass
        if dice1 == dice2:
            dice3 = r.randint(1,6)
            print('Double! -> Extra Roll: ' + str(dice3))
            total += dice3
        if total % 2 == 0:
            print('Total(' + str(total) + ') is even -> +10 Points')
            total += 10
        else:
            print('Total(' + str(total) + ') is odd -> -5 Points')
            total -= 5
            if total < 0:
                total = 0
        P2_Points += total
        print('Total Points For This Round: ' + str(total))
        print('Overall Points: ' + str(P2_Points) + '\n')

    print(name1 + "'s Points: " + str(P1_Points))
    print(name2 + "'s Points: " + str(P2_Points))
    if P1_Points > P2_Points:
        print('- ' + name1 + ' Won! -')
        P1_Won = True
    elif P1_Points < P2_Points:
        print('- ' + name2 + ' Won! -')
        P2_Won = True
    else:
        print('Draw!')
        Draw = True
        
    with open(Results_File, 'a') as f:
        today = date.today()
        f.write(str(today) + ' | ')
        f.write(name1 + "'s Points: " + str(P1_Points) + ' | ')
        f.write(name2 + "'s Points: " + str(P2_Points) + ' | ')
        if P1_Won == True:
            f.write(str(name1) + ' Won' + '\n')
        elif P2_Won == True:
            f.write(str(name2) + ' Won' + '\n')
        elif Draw == True:
            f.write('Draw' + '\n')
            
            
    
        
    
import random as r
from datetime import date
UsersFile = 'Users.txt'
Results_File = 'Six_One_Results.txt'  
SignUp()
Login()
MainGame()
