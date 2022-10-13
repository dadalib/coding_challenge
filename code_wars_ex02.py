import re
def use_regex(word):
    """---Using regex
    At least six characters long
    contains a lowercase letter
    contains an uppercase letter
    contains a digit
    only contains alphanumeric characters (note that '_' is not alphanumeric)

    (?=.*[a-z])        // use positive look ahead to see if at least one lower case letter exists
    (?=.*[A-Z])        // use positive look ahead to see if at least one upper case letter exists
    (?=.*\d)           // use positive look ahead to see if at least one digit exists
    (?=.*\W)           // use positive look ahead to see if at least one non-word character exists
    ^              # begin word
    (?=.*?[a-z])   # at least one lowercase letter
    (?=.*?[A-Z])   # at least one uppercase letter
    (?=.*?[0-9])   # at least one number
    [A-Za-z\d]     # only alphanumeric
    {6,}           # at least 6 characters long
    $              # end word

    """
    # Match 6 string
    regex_is_alpha ='(^[a-zA-Z0-9]+$)'
    regex_6strings= '(\\b\w{6}\\b)'
    regex_lower_case = '(?=.*[a-z])'
    regex_upper_case = '(?=.*[A-Z])'
    regex_digit = '(?=.*\d)'
    regex_not_numeric = '(?=.*\W)'

    if re.match(regex_is_alpha, word):
        return True

    else:
        return False

def format_duration(seconds):
    """Format integer secondd on time

    Args:
        seconds(int):

    Return:

    """
    
    if str(seconds).isdigit() == False:

        raise ValueError("Please insert à number")

    elif seconds == 0:
        return "now"

    if seconds <60 and seconds>1:
        return "%s second" % seconds 
    
    elif seconds >=60 and seconds<360:
        minute,second = divmod(seconds,60)
        if second >1:
            return "%s minute and %s seconds"%(minute,second)
        else:
            return "%s hour" % minute

    elif seconds>=3600:
        hour,rest_minutes = divmod(seconds,3600)
        print(hour,rest_minutes)
        if rest_minutes >= 60:
            minute,second = divmod(rest_minutes,60)
            if second > 1:
                return "%s hour, %s minute and %s seconds"%(hour,minute,second)
            if second == 0:
                return "%s hour and %s minute"%(hour,minute)

def scramble(s1, s2):

    for c2 in s2:
        if s1.count(c2)<s2.count(c2) :
            return False
    return True 

    
            



            

         


    



if __name__=='__main__':
    # print(use_regex("tatf%Lh"))
    # print(format_duration(10563))
    print(scramble('cedewaraaossoqqyt', 'codewars'))



