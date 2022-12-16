# TODO: task_3 + 
"""Given a string, check if its characters can be rearranged to form a palindrome.
Where a palindrome is a string that reads the same left-to-right and right-to-left.

Example
"trueistrue" -> false;
"abcab" -> true because "abcba" is a palindrome
[input] string s (min 1 letters)

[output] boolean"""


def isPalindrome(str):
    count_single = 0
    count_twin = 0
    for letter in str:
        if str.count(letter) % 2 == 0:
            str = str.replace(letter, "")
            count_twin += 1
        else:
            str = str.replace(letter, "")
            count_single += 1
        # print("1= ", count_single, "2= ", count_twin)

    return True if (count_single <= 1 and count_twin >= 0) else False



strg = "bccaa"
strg = "trueistrue"
# strg = "A"
# strg = "2333332"
print(isPalindrome(strg))
