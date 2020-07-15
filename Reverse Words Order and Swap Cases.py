
#Implement a function that takes a string consisting of words separated by single spaces and returns a string containing all those words but in the reverse order 
#and such that all cases of letters in the original string are swapped i.e. lowercase letters become uppercase and uppercase letters become lowercase 

def reverse_words_order_and_swap_cases(sentence):
    a = []
    l = list(sentence)
    for i in l:
        j = ""
        if i.islower():
            j = i.upper()
        elif i.isupper():
            j = i.lower()
        else:
            a.append(i)
        a.append(j)
    o = ''.join(a)
    new =o.split(' ')
    out = ' '.join(reversed(new))
    return out
            
if __name__ == '__main__':