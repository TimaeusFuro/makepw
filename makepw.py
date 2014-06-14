#!/usr/bin/python3

from random import SystemRandom

# Get all printable ASCII characters.
# We only use ASCII for maximum compatibility, but we'll use the whole
# range of them.
ascii = ''.join(chr(x) for x in range(0x20, 0x7f));

def makepw(length = 20, characters = ascii):
    random = SystemRandom()
    return ''.join(random.choice(characters) for x in range(0, length))

if __name__ == '__main__':
    print(makepw())
    
