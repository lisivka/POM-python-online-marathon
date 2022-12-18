'''
Numbers in the Morse code have the following pattern:

all digits consist of 5 characters;
the number of dots at the beginning indicates the numbers from 1 to 5, the remaining characters are dashes;
starting with the number 6, each dot is replaced by a dash and vise versa.
Write the function morse_number() for encryption of a number in a three-digit format in Morse code.

Attention!
Do not use any collection data like lists, tuples, dictionaries for holding Morse codes

For example:

Test	Result
print(morse_number("295")) ..--- ----. .....
print(morse_number("005")) ----- ----- .....
print(morse_number("513")) ..... .---- ...--
print(morse_number("784")) --... ---.. ....-
'''


def morse_number(n: str):
    morse_str = ""
    for i in n:
        N = int(i)
        if 0 <= N <= 5:
            # print(n, N, "." * N + "-" * (5 - N) + " ")
            morse_str += "." * N + "-" * (5 - N) + " "
        else:
            # print(n, N, "-" * (N - 5) + "." * (10 - N) + " ")
            morse_str += "-" * (N - 5) + "." * (10 - N) + " "

    return morse_str


print(morse_number("295"))
print(morse_number("005"))
print(morse_number("513"))
print(morse_number("784"))
