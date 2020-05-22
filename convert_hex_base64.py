


import requests

def intro():

    name = input('Hello traveler. What is your name? ')
    print('I have been waiting to judge a mortal soul.')
    print('You will be judged on your typing skills, ', name)
    print('Type the sentence as fast as possible')

def sentence():

    ready = input('Are you ready? Yes or no? The timer will start when you say yes. ')
    ready = ready.upper()
    if ready == 'YES':
        r = requests.get('https://quote-garden.herokuapp.com/api/v2/quotes/random')
        piece = r.json()
        sentence = piece['quote']['quoteText']
        time_start = time.time()
        typer = input(sentence + '\n')





    else:
        print('Ok, goodbye.')
        
    
