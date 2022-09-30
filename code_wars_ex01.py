import re
import math

def disemvowel(string_):
    vowels = ['A','E','I','O','U']
    new_str =""
    for ch in string_:
        if ch.capitalize() not in vowels:
            new_str+=ch
            
    return  new_str
    
def disemvowel_short(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

def get_count(sentence):
    """Count vowels in str
    Args:
        sentence(str) : String give by the user

    Returns:
        counter(int) : Counter of vowels

    """
    vowels = ['a','e','i','o','u']
    counter = 0
    
    if len(sentence)<0 or type(sentence) is not str:
        raise ValueError("Please take give a string")
    
    for ch in sentence:
        if ch.lower() in vowels:
            counter +=1
            
    return counter

def getCount(str):
    """Using regex"""
    return len(re.findall('[aeiou]',str,re.IGNORECASE))

def get_count_short(s):
    """Using sum"""
    return sum(c in 'aeiou' for c in s)

def get_sum(a,b):
    """Sum for two element starting for the min range
    Args:
        a(int) :
        b(int) : 
    """
    soma=0
    if a==b:
        return a
    elif a > b:
        for i in range(b,a+1):
            soma += i
        return soma
    else:
        for i in range(a,b+1):
            soma += i
        return soma

def get_sum_v2(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

def get_sum_short(a, b):

    if a>b : a,b = b,a
    return sum(range(a,b+1))

        

def check_is_square(value):
    for i in range(value //2 +1):
        print(i)
        if i*i == value:
            return True, i
    return False,-1

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    check, value= check_is_square(sq)
    result=0
    if check == True:
        result = (value+1)*(value+1)
    else:
        result = value
        return  str(result)+" since"+str(sq)+" is not a perfect square"
                      
    return result

def find_next_square_short(sq):
    """Now if a number is sqrt"""
    return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1

def to_camel_case(text):
    """Convert to capital camle case
    Args:
        text(str) : input text 

    Returns:
        new_text(str): 
    """

    list_chr = ['-','_']
    next_text = ""

    for c in text:
        print(c)
        if c in list_chr:
            next_text+=" "
            # next_text.join(" ")
        else:
           
            next_text+=c
            # next_text.join(c)


    next_text = next_text.title()
    next_text = next_text.strip()
    next_text = next_text.replace(" ","")
    

    
    return next_text

def to_camel_case_v2_expection(text):





if __name__ == '__main__':
    # print(disemvowel("This website is for losers LOL!"))
    # print(disemvowel_short("This website is for losers LOL!"))
    # a= 12
    # b = -16
    # print(get_sum_v2(-24,15))
    # print(find_next_square(145))
    print(to_camel_case("Toto_le_pregunto_si_Tengo-novia"))



