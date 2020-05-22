
# this program mimics a fallout terminal you can hack
# lol

from random import *


def intro():
    print('Good luck hacking this terminal')
    difficulty = input('Choose your level. \n1: Novice \n2: Advanced \n3: Expert \n4: Master\n')
    if difficulty not in ('1' and '2' and '3' and '4'):
        print('Restart and chose a real difficulty.')

    return int(difficulty)


def interface(level):

    filler = ['[([&%$)++@!#$%%^', '^&^#%^$*!$$*', '~!!)%&+$#@#+']

    novice_words = ['LAKE', 'MEAL', 'MATH', 'ROAD', 'BATH', 'DATA', 'CITY', 
                    'MENU', 'DEBT', 'GOAL', 'MOOD', 'YEAR', 'BEER', 'USER', 'IDEA', 'DESK', 
                    'EXAM', 'POEM', 'MEAT', 'WIFE', 'WOOD', 'MODE', 'GIRL', 'SONG', 'GATE',
                    'GENE', 'UNIT', 'LOSS', 'LOVE', 'FACT', 'NEWS', 'FOOD', 'LADY', 'POET', 
                    'BIRD', 'DISK', 'ROLE', 'SOUP', 'CELL', 'AREA', 'MALL', 'OVEN', 'DIRT', 
                    'ARMY', 'WEEK', 'HAIR', 'TOWN', 'TALE', 'KING', 'HALL']

    advanced_words = ['MONTH', 'UNION', 'WOMAN', 'RIVER', 'DRAMA', 'TOOTH', 'SKILL', 
                      'HEART', 'PIANO', 'QUEEN', 'CHEEK', 'VIRUS', 'ACTOR', 'CHILD', 'BONUS', 
                      'PHOTO', 'MUSIC', 'MEDIA', 'EVENT', 'BASIS', 'SHIRT', 'APPLE', 'POWER', 'YOUTH', 
                      'CHEST', 'BLOOD', 'BUYER', 'HOTEL', 'HONEY', 'PIZZA', 'UNCLE', 'TRUTH', 'THING', 
                      'VIDEO', 'ENTRY', 'ERROR', 'NIGHT', 'WORLD', 'RATIO', 'OWNER', 'PHONE', 'MOVIE', 
                      'PAPER', 'DEATH', 'SCENE', 'STORY', 'BREAD', 'DEPTH', 'SALAD', 'STEAK']

    expert_words = ['SECTOR', 'MEMORY', 'TONGUE', 'ESTATE', 'EFFORT', 
                    'NATION', 'THROAT', 'FLIGHT', 'WRITER', 'POTATO', 'WEALTH', 'BREATH',
                    'ENERGY', 'PERSON', 'MOMENT', 'FAMILY', 'ORANGE', 'DEALER', 'CANCER',
                    'PLAYER', 'MEMBER', 'SERIES', 'VOLUME', 'NATURE', 'THANKS', 'GUITAR',
                    'METHOD', 'SINGER', 'DINNER', 'COUSIN', 'OFFICE', 'REGION', 'INJURY', 
                    'BASKET', 'CAMERA', 'AGENCY', 'SAFETY', 'EXTENT', 'LEADER', 'SYSTEM', 
                    'ADVICE', 'WINNER', 'SPEECH', 'PEOPLE', 'LENGTH', 'RECIPE', 'POLICY', 
                    'COUNTY', 'GROWTH', 'COFFEE']

    master_words = ['OUTCOME', 'CONTEXT', 'STORAGE', 'ANALYST', 'PENALTY', 'TENSION', 
                    'OPINION', 'COURAGE', 'ABILITY', 'VERSION', 'LIBRARY', 'PROBLEM', 'SPEAKER', 'GROCERY',
                    'FUNERAL', 'CONCEPT', 'PHYSICS', 'THOUGHT', 'SURGERY', 'PASSION', 'REVENUE', 'DIAMOND',
                    'WEDDING', 'SCIENCE', 'WARNING', 'COUNTRY', 'PAYMENT', 'TEACHER', 'FISHING', 'SESSION', 
                    'PRODUCT', 'DISEASE', 'MANAGER', 'ARTICLE', 'SOCIETY', 'CLIMATE', 'READING', 'WRITING', 
                    'MEANING', 'MESSAGE', 'CONTROL', 'AIRPORT', 'HOUSING', 'FREEDOM', 'STUDENT', 
                    'FAILURE', 'COLLEGE', 'CABINET', 'QUALITY', 'VARIETY']

    for i in range(10):
        print((filler[randint(0,2)])
        + (filler[randint(0,2)])
        + (novice_words[randint(0,49)])
        + (filler[randint(0,2)]), sep='')

interface(5)