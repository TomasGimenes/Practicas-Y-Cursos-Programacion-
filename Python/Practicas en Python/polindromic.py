s = "babad"

def longest_palindrome(s:str):
    lista = list(s)
    for i in s:
        if s.startswith(i):
            print("yes")
        else:
            print("nor")
        


longest_palindrome(s)