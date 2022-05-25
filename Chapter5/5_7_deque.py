def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
        return True

print(palindrome('a'))
print(palindrome('racecar'))
print(palindrome('straw warts'))
print(palindrome('fishsticks'))
print(palindrome('ambergris'))

def another_palindrom(word):
    return word == word[::-1]

print(another_palindrom('a'))
print(another_palindrom('racecar'))
print(another_palindrom('straw warts'))
print(another_palindrom('fishsticks'))