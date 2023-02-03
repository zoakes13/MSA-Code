
import time
import random

def printboard():
    print("     1   2   3")
    print(f"A    {A1} | {A2} | {A3}   ")
    print("    ___|___|___")
    print(f"B    {B1} | {B2} | {B3}   ")
    print("    ___|___|___")
    print(f"C    {C1} | {C2} | {C3}  ")
    print("       |   |   ")

def choosemode():
    while(True):  
        print("Hello! Welcome to Tic Tac Toe you silly little bitch!")
        choice = input("Would you like to:\n1. Play with a bot?\n2. Play with another player?\n3. Quit\n")
        choice = int(choice)
        if choice != 1 and choice != 2 and choice != 3:
            print("Please input either 1, 2, or 3 dumbass")
        else:
            return choice

def two(lane, s1, s2, s3, tac):
    if lane.count(" ") == 1:
        if lane.count("O") == 2:
            space = lane.index(" ")
            if space == 0:
                return s1
            if space == 1:
                return s2
            if space == 2:
                return s3
        if lane.count("X") == 2:
            if tac == False:
                rtac = []
                space = lane.index(" ")
                if space == 0:
                    return rtac.append(s1)
                if space == 1:
                    return rtac.append(s2)
                if space == 2:
                    return rtac.append(s3)
            try:
                #Checks if tac is a list of X blocks
                tac.reverse()
            
            except:
                return tac
            
            else:
                space = lane.index(" ")
                if space == 0:
                    tac = tac.append(s1)
                    return tac
                if space == 1:
                    tac = tac.append(s2)
                    return tac
                if space == 2:
                    tac = tac.append(s3)
                    return tac

        else:
            if tac == False:
                return False

    else:
        if tac == False:
            return False


while True:
    A1 = " "
    A2 = " "
    A3 = " "
    B1 = " "
    B2 = " "
    B3 = " "
    C1 = " "
    C2 = " "
    C3 = " "
    
    choice = choosemode()

    #Bot
    if choice == 1:
        dif = input("Would you liek to play on\n1. Easy\n2. Hard\n")
        if dif == "1":
            win = False
            count = 1
            while win == False:
                printboard()
                time.sleep(1)
                if count % 2 == 0:
                    turn = 2
                else:
                    turn = 1
                if count == 10:
                    print("It was a tie!")
                    time.sleep(1)
                    break
                retry = True
                while retry == True:   
                    if turn == 1:
                        tac = input(f"\n\nMake your move player {turn}! Ex. A1, A2...")
                    
                    #BOT
                    if turn == 2:
                        rand = random.randint(1, 9)
                        if rand == 1:
                            tac = "A1"
                        if rand == 2:
                            tac = "A2"
                        if rand == 3:
                            tac = "A3"
                        if rand == 4:
                            tac = "B1"
                        if rand == 5:
                            tac = "B2"
                        if rand == 6:
                            tac = "B3"
                        if rand == 7:
                            tac = "C1"
                        if rand == 8:
                            tac = "C2"
                        if rand == 9:
                            tac = "C3"
                    
                    out = ""
                    if turn == 1:
                        letter = "X"
                    if turn == 2:
                        letter = "O"
                    if tac == "A1":
                        if A1 != " ":
                            out = "taken"
                        else:   
                            A1 = letter
                            out = "good"
                    if tac == "A2":
                        if A2 != " ":
                            out = "taken"
                        else:
                            A2 = letter
                            out = "good"
                    if tac == "A3":
                        if A3 != " ":
                            out = "taken"
                        else:   
                            A3 = letter
                            out = "good"
                    if tac == "B1":
                        if B1 != " ":
                            out = "taken"
                        else:    
                            B1 = letter
                            out = "good"
                    if tac == "B2":
                        if B2 != " ":
                            out = "taken"
                        else:   
                            B2 = letter
                            out = "good"
                    if tac == "B3":
                        if B3 != " ":
                            out = "taken"
                        else:
                            B3 = letter
                            out = "good"
                    if tac == "C1":
                        if C1 != " ":
                            out = "taken"
                        else:
                            C1 = letter
                            out = "good"
                    if tac == "C2":
                        if C2 != " ":
                            out = "taken"
                        else:
                            C2 = letter
                            out = "good"
                    if tac == "C3":
                        if C3 != " ":
                            out = "taken"
                        else:    
                            C3 = letter
                            out = "good"
                    


                    if out == "good":
                        retry = False
                    if out == "taken":
                        print("Oops!  That space has been taken, try again!")
                    if out == "again" or out == "":
                        print("Oops!  Try that one again, something went wrong")
                
                #check win
                
                
                if A1 == A2 and A2 == A3:
                    if A1 != " ":
                        win = True
                if B1 == B2 and B2 == B3:
                    if B1 != " ":
                        win = True
                if C1 == C2 and C2 == C3:
                    if C1 != " ":
                        win = True
                
                if A1 == B1 and B1 == C1:
                    if C1 != " ":
                        win = True
                if A2 == B2 and B2 == C2:
                    if C2 != " ":
                        win = True
                if A3 == B3 and B3 == C3:
                    if C3 != " ":
                        win = True

                if A1 == B2 and B2 == C3:
                    if B2 != " ":
                        win = True
                if C1 == B2 and B2 == A3:
                    if C1 != " ":
                        win = True
                
                if win == True:
                    printboard()
                    print(f"Player {turn} won!")
                    time.sleep(1)
                count += 1
            
        if dif == "2":
            win = False
            count = 1
            while win == False:
                printboard()
                time.sleep(1)
                if count % 2 == 0:
                    turn = 2
                else:
                    turn = 1
                if count == 10:
                    print("It was a tie!")
                    time.sleep(1)
                    break
                retry = True
                while retry == True:   
                    if turn == 1:
                        tac = input(f"\n\nMake your move player {turn}! Ex. A1, A2...")
                    
                    #BOT
                    if turn == 2:
                        tac = False
                        if count > 2:
                            if A1 == A2 or A1 == A3 or A2 == A3:
                                lane = f"{A1}{A2}{A3}"
                                tac = two(lane, "A1", "A2", "A3", tac)
                            if B1 == B2 or B1 == B3 or B2 == B3:
                                lane = f"{B1}{B2}{B3}"
                                tac = two(lane, "B1", "B2", "B3", tac) 
                            if C1 == C2 or C1 == C3 or C2 == C3:
                                lane = f"{C1}{C2}{C3}"
                                tac = two(lane, "C1", "C2", "C3", tac)          
                        
                        try:
                            tac = tac[0]
                        
                        except:
                            tac = tac
                        
                        
                        if tac == False:
                            rand = random.randint(1, 9)
                            if rand == 1:
                                tac = "A1"
                            if rand == 2:
                                tac = "A2"
                            if rand == 3:
                                tac = "A3"
                            if rand == 4:
                                tac = "B1"
                            if rand == 5:
                                tac = "B2"
                            if rand == 6:
                                tac = "B3"
                            if rand == 7:
                                tac = "C1"
                            if rand == 8:
                                tac = "C2"
                            if rand == 9:
                                tac = "C3"
                    
                    out = ""
                    if turn == 1:
                        letter = "X"
                    if turn == 2:
                        letter = "O"
                    if tac == "A1":
                        if A1 != " ":
                            out = "taken"
                        else:   
                            A1 = letter
                            out = "good"
                    if tac == "A2":
                        if A2 != " ":
                            out = "taken"
                        else:
                            A2 = letter
                            out = "good"
                    if tac == "A3":
                        if A3 != " ":
                            out = "taken"
                        else:   
                            A3 = letter
                            out = "good"
                    if tac == "B1":
                        if B1 != " ":
                            out = "taken"
                        else:    
                            B1 = letter
                            out = "good"
                    if tac == "B2":
                        if B2 != " ":
                            out = "taken"
                        else:   
                            B2 = letter
                            out = "good"
                    if tac == "B3":
                        if B3 != " ":
                            out = "taken"
                        else:
                            B3 = letter
                            out = "good"
                    if tac == "C1":
                        if C1 != " ":
                            out = "taken"
                        else:
                            C1 = letter
                            out = "good"
                    if tac == "C2":
                        if C2 != " ":
                            out = "taken"
                        else:
                            C2 = letter
                            out = "good"
                    if tac == "C3":
                        if C3 != " ":
                            out = "taken"
                        else:    
                            C3 = letter
                            out = "good"
                    


                    if out == "good":
                        retry = False
                    if out == "taken":
                        print("Oops!  That space has been taken, try again!")
                    if out == "again" or out == "":
                        print("Oops!  Try that one again, something went wrong")
                
                #check win
                
                
                if A1 == A2 and A2 == A3:
                    if A1 != " ":
                        win = True
                if B1 == B2 and B2 == B3:
                    if B1 != " ":
                        win = True
                if C1 == C2 and C2 == C3:
                    if C1 != " ":
                        win = True
                
                if A1 == B1 and B1 == C1:
                    if C1 != " ":
                        win = True
                if A2 == B2 and B2 == C2:
                    if C2 != " ":
                        win = True
                if A3 == B3 and B3 == C3:
                    if C3 != " ":
                        win = True

                if A1 == B2 and B2 == C3:
                    if B2 != " ":
                        win = True
                if C1 == B2 and B2 == A3:
                    if C1 != " ":
                        win = True
                
                if win == True:
                    printboard()
                    print(f"Player {turn} won!")
                    time.sleep(1)
                count += 1

            if dif != "1" and dif != "2":
                print("ERROR")
        
    
    
    
    #2 Player
    if choice == 2:
        win = False
        count = 1
        while win == False:
            printboard()
            if count % 2 == 0:
                turn = 2
            else:
                turn = 1
            if count == 10:
                print("It was a tie!")
                time.sleep(1)
                break
            retry = True
            while retry == True:   
                tac = input(f"\n\nMake your move player {turn}! Ex. A1, A2...")
                
                out = ""
                if turn == 1:
                    letter = "X"
                if turn == 2:
                    letter = "O"
                if tac == "A1":
                    if A1 != " ":
                        out = "taken"
                    else:   
                        A1 = letter
                        out = "good"
                if tac == "A2":
                    if A2 != " ":
                        out = "taken"
                    else:
                        A2 = letter
                        out = "good"
                if tac == "A3":
                    if A3 != " ":
                        out = "taken"
                    else:   
                        A3 = letter
                        out = "good"
                if tac == "B1":
                    if B1 != " ":
                        out = "taken"
                    else:    
                        B1 = letter
                        out = "good"
                if tac == "B2":
                    if B2 != " ":
                        out = "taken"
                    else:   
                        B2 = letter
                        out = "good"
                if tac == "B3":
                    if B3 != " ":
                        out = "taken"
                    else:
                        B3 = letter
                        out = "good"
                if tac == "C1":
                    if C1 != " ":
                        out = "taken"
                    else:
                        C1 = letter
                        out = "good"
                if tac == "C2":
                    if C2 != " ":
                        out = "taken"
                    else:
                        C2 = letter
                        out = "good"
                if tac == "C3":
                    if C3 != " ":
                        out = "taken"
                    else:    
                        C3 = letter
                        out = "good"
                


                if out == "good":
                    retry = False
                if out == "taken":
                    print("Oops!  That space has been taken, try again!")
                if out == "again" or out == "":
                    print("Oops!  Try that one again, something went wrong")
            
            #check win
            
         
            if A1 == A2 and A2 == A3:
                if A1 != " ":
                    win = True
            if B1 == B2 and B2 == B3:
                if B1 != " ":
                    win = True
            if C1 == C2 and C2 == C3:
                if C1 != " ":
                    win = True
            
            if A1 == B1 and B1 == C1:
                if C1 != " ":
                    win = True
            if A2 == B2 and B2 == C2:
                if C2 != " ":
                    win = True
            if A3 == B3 and B3 == C3:
                if C3 != " ":
                    win = True

            if A1 == B2 and B2 == C3:
                if B2 != " ":
                    win = True
            if C1 == B2 and B2 == A3:
                if C1 != " ":
                    win = True
            
            if win == True:
                printboard()
                print(f"Player {turn} won!")
                time.sleep(1)
            count += 1
            
            

    if choice == 3:
        print("Goodbye :(")
        break