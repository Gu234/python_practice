import random
import string

WORDS = [
    'dare',
    'calorie',
    'allocation',
    'filter',
    'vain',
    'makeup',
    'brother',
    'hook',
    'spoil',
    'history',
    'resist',
    'subject',
    'practice',
    'cotton',
    'experience',
    'mourning',
    'information',
    'mine',
    'real',
    'origin',
    'improve',
    'fax',
    'interactive',
    'linen',
    'theory',
    'communist',
    'shape',
    'resource',
    'undermine',
    'week',
    'strange',
    'artificial',
    'carrot',
    'motif',
    'so',
    'twitch',
    'calm',
    'lose',
    'flourish',
    'difference',
    'plant',
    'exact',
    'hospitality',
    'threat',
    'goalkeeper',
    'spread',
    'runner',
    'protect',
    'relieve',
    'reserve',
]
    
LETTERS = string.ascii_letters + string.digits + string.punctuation

def generate_password(size=10):
    return ''.join(random.choices(LETTERS, k=size))

def generate_readable_password(n=5):
    return '-'.join(random.choices(WORDS, k=n))



if __name__ == '__main__':
    print(generate_password(20))
    print(generate_readable_password(10))
