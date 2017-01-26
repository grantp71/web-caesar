def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char = letter.lower()
    for i in range(len(alphabet)):
        if char == alphabet[i]:
            return i

def rotate_character(char, rot):
    lwr_alpha = 'abcdefghijklmnopqrstuvwxyz'
    upr_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for n in range(len(lwr_alpha)):
        if char == lwr_alpha[n]:
            return lwr_alpha[((alphabet_position(char))+rot)%26]
        elif char == upr_alpha[n]:
            return upr_alpha[((alphabet_position(char))+rot)%26]
    return char

def encrypt(text, rot):
    encrypted = ''
    for eachChar in text:
        encrypted = encrypted + rotate_character(eachChar, rot)
    return encrypted
