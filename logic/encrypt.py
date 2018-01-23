alphabet = ['1', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]
capitalAlphabet = ['!', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
text = "Jeg elsker IB Jeg lyver aldrig"


def encoder(shift):
    Result = {}
    for i in range(27):
        if i + shift < 27:
            Result[alphabet[i]] = alphabet[i + shift]
        if i + shift > 26:
            Result[alphabet[i]] = alphabet[(i + shift) - 27]
    return Result


def cesarcipher(text, shift):
    text = list(text)
    alphabetshifted = encoder(shift)
    length = text.__len__()
    for i in range(length):
        if str(text[i]).isupper():
            # Take an upper case letter, find its lowercase shifted equivalent, take that letter and uppercase it
            text[i] = str(alphabetshifted[str(text[i]).lower()]).upper()
        if not str(text[i]).isupper():
            text[i] = alphabetshifted[text[i]]

    return ''.join(text)


def decode(text):
    result = "not found"
    text = list(text)
    textb = list(text)
    for i in range(27):
        alphabetshifted = antiencode(i)
        # Decode routine
        for j in range(len(text)):
            if str(text[j]).isupper():
                text[j] = str(alphabetshifted[str(textb[j]).lower()]).upper()
            if not str(text[j]).isupper():
                text[j] = alphabetshifted[str(textb[j]).lower()]
        result = ''.join(text)
        print(result)


def antiencode(shift):
    result = {}
    alphaa = alphabet
    alphab = alphabet
    for i in range(27):
        if i - shift >= 0:
            result[alphaa[i]] = alphab[i - shift]
        if i - shift < 0:
            result[alphaa[i]] = alphab[27 - (shift - i)]
    return result
