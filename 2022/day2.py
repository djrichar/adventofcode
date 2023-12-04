
values = []
with open("day2-input.txt", "r") as f:
    for line in f.readlines():
        OPP, ME = line.split()
        opp_val = ord(OPP)-64
        if ME == "X":  ## LOSE
            me_val = 3 if opp_val == 1 else opp_val - 1
        elif ME == "Y": ## DRAW
            me_val = opp_val
        elif ME == "Z": ## WIN
            me_val = 1 if opp_val == 3 else opp_val + 1
        result = me_val
        if me_val == opp_val:
            result += 3
        elif me_val == opp_val+1 or me_val == (opp_val+1)%3:
            result += 6    
        values.append((OPP, opp_val, ME, me_val, result))
        print(values[-1])
print(sum([x[4] for x in values]))