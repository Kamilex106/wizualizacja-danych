def parzyste(string):
    return string[::2]

def nostatnich(string, n=1):
    return string[-n:]

def odwrocony_string(string):
    return string[::-1]

def dluzszy_string(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str2) > len(str1):
        return str2
    else:
        return "obydwa sa takie same."

def format_string(name, dob):
    return "My name is {}. My date of birth is {}.".format(name, dob)


# Testowanie funkcji
string = "Lorem_ipsum_dolor_sit_amet"
name = "Kamil"
date = "01/01/2000"

print(parzyste(string))
print(nostatnich(string))
print(nostatnich(string, 4))
print(odwrocony_string(string))
print(dluzszy_string("abc", "defgh"))
print(dluzszy_string("abcd", "ef"))
print(format_string(name, date))
