import random
import re
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

# -------------------------------------------------------------
valid_url_pattern0 = "((http|https)://)(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]" + "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)"
valid_url_pattern1 = "(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]" + "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)"
valid_url_pattern2 = "[a-zA-Z0-9@:%._\\+~#?&//=]" + "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)"

def isURLValid(url : str) :
    if re.search(re.compile(valid_url_pattern0), url) or re.search(re.compile(valid_url_pattern1), url) or re.search(re.compile(valid_url_pattern2), url):
        return True
    return False

if __name__ == "__main__" :
    # print(isURLValid('https://www.geeksforgeeks.org/check-if-an-url-is-valid-or-not-using-regular-expression/#:~:text=Match%20the%20given%20URL%20with,regular%20expression%2C%20else%20return%20false.'))
    pass