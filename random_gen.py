import random
eng_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
'w', 'x', 'y', 'z']

eng_big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
'W', 'X', 'Y', 'Z']

def randomLinkCode():
    link_key = []
    link_key.append(f'{random.randint(0,9)}')
    link_key.append(random.choice(eng_small))
    link_key.append(f'{random.randint(0,99)}')
    link_key.append(random.choice(eng_big))
    link_key.append(random.choice(eng_small))
    
    return ''.join(link_key)

# if __name__ == "__main__" :
#     pass