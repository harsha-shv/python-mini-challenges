# --------------
#Code starts here

def palindrome(num):
    i=num+1
    while(i>num):
        num1=str(i)
        if(num1[::-1]==num1):
            return(int(num1))
        i=i+1




# --------------
#Code starts here

#Function to find anagram of one word in another

def a_scramble(str_1,str_2):
    result=True
    for i in (str_2.lower()):
        if i not in (str_1.lower()):
            result=False
            break
        str_1=str_1.replace(i,'',1) #Removing the letters from str_1 that are already checked
    
    return (result)

#Code ends here


# --------------
#Code starts here
def check_fib(num):
    a = 0;
    b = 1;
    if (num==a or num==b):
        return true;
    c = a+b;
    while(c<=num):
        if(c == num):
            return(True)
        a = b;
        b = c;
        c = a + b;
    return (False)

check_fib(987)


# --------------
#Code starts here

#Function to compress string
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)

#Code ends here


# --------------
#Code starts here
def k_distinct(string,k):
    string=string.lower()
    string=list(string)
    string=list(dict.fromkeys(string))
    c=len(string)
    if c==k:
        return(True)
    else:
        return(False)

k_distinct('Messoptamia',8)


