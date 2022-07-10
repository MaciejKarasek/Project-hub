from random import choice
while True:
    pchoice = input("Pick (R)ock, (P)aper or (S)cissors: ")
    if pchoice in ['R', 'P', 'S']:
        break
    else:
        print('Choice has to be R, P or S')
bchoice=choice(['R', 'P', 'S'])
bot = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}[bchoice]
print (f'Bot choice: {bot}') 

if pchoice == bchoice:
    print('Draw')
else:
    if pchoice == 'S':
        print({'R':'You lost', 'P':'You won'}[bchoice])
    if pchoice == 'R':
        print({'P':'You lost', 'S':'You won'}[bchoice])
    if pchoice == 'P':
        print({'S':'You lost', 'R':'You won'}[bchoice])