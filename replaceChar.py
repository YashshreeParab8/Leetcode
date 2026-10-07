# Given a string, a character oldChar, and a character newChar, replace every occurrence of oldChar with newChar.
# All other characters should remain unchanged
# Solved on Skilli daily challenges

def replace_pi(s):
    result = []
    i = 0
    n = len(s)
    while i < n:
        if i + 1 < n and s[i] == 'p' and s[i + 1] == 'i':
            result.append("3.14")
            i += 2
        else:
            result.append(s[i])
            i += 1
    return ''.join(result)