import re
import math
from unittest import result
import string
from xml.dom.expatbuilder import InternalSubsetExtractor

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
    print("First char ",text[0])
    if text[0].isupper():
        for c in text:
            if c in list_chr:
                next_text+=" "
            
            else:
            
                next_text+=c

        next_text = next_text.title()
        next_text = next_text.strip()
        next_text = next_text.replace(" ","")
    else:
        pass
    

    
    return next_text

def create_phone_number(n):
    result=""
    if len(n)<10:
        raise ValueError("Please enter a good list")

    for index, value in enumerate(n):
        if index == 0:
            result +='('+str(value)

        elif index <2 and index >0:
            result += str(value)
            
        elif index==2:
            result +=str(value)+') '

        elif index>2 and index <5:
            result +=str(value)

        elif index==5:
            result += str(value)+'-'
        elif index >5:
            result += str(value)

    return result


def create_phone_number_short(n):
    """List manipulation"""
    n = ''.join(map(str,n))
    print("type", n)
    return '(%s) %s-%s'%(n[:3],n[3:6],n[6:])

def square_digits(num):
    """power of two"""
    result=""
    power = 2
    str_num = str(num)
    for value in str_num :
        result+=str(int(math.pow(int(value),power)))

    return int(result)


def square_digits_short(num):
    """Using join"""
    return int(''.join(str(int(d)**2) for d in str(num)))

def alphabet_position(text):
    """Dictionary use zip or  and get"""
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_num = [*range(1,len(alphabet)+1,1)]
    result = ""
    

    if len(alphabet) != len(alphabet_num):
        raise ValueError("Wrong matching for dictonary")

    alphabet_dict = dict(zip(alphabet,alphabet_num))

    for ch in text:
        if ch.lower() in alphabet_dict.keys():
            result+= str(alphabet_dict.get(ch.lower()))+' '

    return result.strip()

def generate_alphabet():
    alphabet_lst=list(string.ascii_lowercase)
    alphabet_num= list(range(1,len(alphabet_lst)+1,1))
    return alphabet_lst,alphabet_num

def unique_in_order(iterable):
    result =[]
    result_without_double=[]

    print("lenI",len(iterable))
    if len(iterable)<1:
        return []

    if len(iterable)==1:
        return list(str(iterable))
    # Make the list
    for c in iterable:
        result.append(c)
    print(result)

    # Take out the repete sequence
    for index , value in enumerate(result):

        if len(result) > (index+1):
            if result[index] != result[index+1]:
                result_without_double.append(value)
    if result[-1] != result_without_double[-1]:
        result_without_double.append(result[-1])


    return result_without_double

def unique_in_order_short(iterable):
    res = []
    for item in iterable:
        if len(res) == 0 or item != res[-1]:
            print("Len",len(res))
            res.append(item)
    return res


if __name__ == '__main__':
    # print(disemvowel("This website is for losers LOL!"))
    # print(disemvowel_short("This website is for losers LOL!"))
    # a= 12
    # b = -16
    # print(get_sum_v2(-24,15))
    # print(find_next_square(145))
    # print(to_camel_case("Toto_le_pregunto_si_Tengo-novia"))
    # print(create_phone_number_short([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    #print(square_digits(9119))
    #print(square_digits_short(9119))
    #print(alphabet_position("The sunset sets at twelve o' clock."))
    # print(generate_alphabet())
    # print(unique_in_order('A'))
    print(unique_in_order_short('AAAABBBCCDAABBB'))



