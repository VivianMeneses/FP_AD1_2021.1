

'''def verifica_igualdade(s1,s2):
    if s1 == s2:
        return True
    else:
        return False'''

def palindrome(v):
    if len(v) > 1:
        if v[0] == v[len(v)-1]:
            if len(v) == 2:
                return True
            else:
                v = v[1:len(v)-1]
                if palindrome(v):
                    return True
        else:
            return False
    else:
        return True

txt = "aswaaqsa"
txt = "".join(txt.split())
if palindrome(txt):
    print("é palindrome")
else:
    print("não é palindrome")