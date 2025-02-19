# YOU ONLY HAVE TO SUBMIT FUNCTIONS FOR WHICH
# YOU ARE THE DRIVER IN PAIR PROGRAMMING
import random 
import numpy as np

# Here are some history variables to test your code on. Feel free to create your own.
hist1 = []
hist2 = [("split","steal")]
hist3 = [("split","split"),("steal","split"),("split,steal"),("split,split"),("steal,split")]
hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","split"),("split","split"),("steal","split")]

# Your team's 1st strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 

def code_crafters2(history):
    action = "steal"
    if len(history) > 0:
        choice = random.randint(0,2)
        if choice == 0 or choice == 1:
            action = "steal"
        else:
            action = "split"
    elif len(history) > 15:
        action = history[-1]
    elif len(history) > 20:
        opponent_10_previous = history[-10:]
        action = opponent_10_previous
    elif len(history) > 35:
        opponent_steal_count = 0
        opponent_split_count = 0
        for r in history:
            r = (me, opponent) 
            if opponent == "split":
                opponent_split_count += 1
            else:
                opponent_steal_count += 1
        steal_percentage = (opponent_steal_count/(opponent_steal_count + opponent_split_count)) * 100
        split_percentage = (opponent_split_count/(opponent_split_count+opponent_steal_count)) * 100
        if steal_percentage > split_percentage:
            action = random.choice(["split"], ["steal"], ["steal"])
        else:
            action = random.choice(["split"], ["split"], ["steal"])
    elif len(history) > 50:
        if len(history) % 5 == 0 or  len(history) % 3  == 0 or len(history) % 4   == 0:
            action = "steal"
        else:
            action = "split"
    elif len(history) > 75:
        action = "steal"
    elif len(history) > 90:
        action = history[-1]
    elif len(history) > 110:
        if len(history) % 2 == 0:
            action = "steal"
        else:
            action = "split"
    elif len(history) > 130:
        percentage = random.randint(1, 10)
        if percentage < 7:
            action = "steal"
        else:
            action = "split"
    elif len(history) > 150:
        opponent_13_previous = history[13:]
        action = opponent_13_previous
    return action



def codecrafters1(history):
    if len(history) == 0:
        action = "steal"
    
    elif len(history) < 30:
        action = random.choice(["steal", "steal","split"])

    elif len(history) >=30:
        for action in range(len(history)):
                Opponentlastmove = history[-1]
                Nextmove = Opponentlastmove[1]
                action = Nextmove
    elif len(history) >= 60:
        percentage = random.randint(1,10)
        if percentage <= 7:
            action = "steal"
        else: 
            action = "split"
    elif len(history) >= 90:
        OpponentSplit = 0
        OpponentSteal = 0
        OpponentPercent = 0
        for r in history:
            (me,them) = r
            if them == "split":
                OpponentSplit += 1
            elif them == "steal":
                OpponentSteal += 1
        OpponentPercent1 = OpponentSplit / (OpponentSteal + OpponentSplit)
        OpponentPercent2 = OpponentSteal / (OpponentSteal + OpponentSplit)
        if OpponentPercent1 > OpponentPercent2:
            percentage2 = random.randint(1,20)
            if percentage2 >= 15:
                action = "steal"
            else:
                action = "split"
    elif len(history) >= 120:
        percentage = random.randint(1,10)
        if percentage >= 7:
            action = Nextmove
        else: 
            action = random.choice(["steal","split"])
    elif len(history) >= 150:
                
        opponent25previous = history[-25:]

        newMoves = []

        for r in history:

            opponentMoves = r
                
        newMoves.append(opponentMoves)
        splitCount = 0
        stealCount = 0
        for m in newMoves:
            if m == "split":
                splitCount += 1
            else:
                stealCount += 1
            if splitCount > stealCount:
                percentage3 = random.randint(1,20)
                if percentage3 >= 17:
                    action = "split"
            elif stealCount > splitCount:
                action = "steal"
            else:
                action = "steal"
    elif len(history) >= 180:
            Opponentlastmove = history[-1]
            Nextmove = Opponentlastmove[1]
            action = Nextmove
    else:
        if len(history) % 5 == 0:
            action = random.choice(["steal", "steal","split"])
                
        if len(history) % 20 == 0:
            action = random.choice(["steal", "steal", "steal", "steal", "split", "split"])
    return action

def codeCrafters3(history):
    opp_hist = [move[1] for move in history]

    if len(opp_hist) < 3:
        return 'steal'
    
    splits = opp_hist.count('split')
    steals = opp_hist.count('steal')
    total = len(opp_hist)

    if splits / total > 0.5:
        return 'steal'
    
    if steals / total > 0.5:
        if random.random() < 0.7:
            return 'steal'
        else:
            return 'split'
    
    if random.random() < 0.6:
        return 'steal'
    else:
        return'split'






                


    



# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 
