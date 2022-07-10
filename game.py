from random import choice

def RPS(pchoice):
    bchoice=choice(['R', 'P', 'S'])
    if pchoice == bchoice:
        return [2, bchoice]
    else:
        if pchoice == 'S':
            return [{'R':0, 'P':1}[bchoice], bchoice]
        if pchoice == 'R':
            return [{'P':0, 'S':1}[bchoice], bchoice]
        if pchoice == 'P':
            return [{'S':0, 'R':1}[bchoice], bchoice]