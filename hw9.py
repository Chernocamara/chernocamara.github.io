
# PART A

myList = ["apple", "banana", "orange", "berry"]

print(myList)
myList2 = [myList[1],myList[2],myList[3]]
print(myList2)
myList2.append("mango")
print(myList2)
myList2.pop(2)
print(myList2)
myList3 = myList2


# part B

# count(sub,[start,[end]].  python string method count() returns the number of occurrence of substring sub in the range [start, end].

str = "this is string example....wow!!!";

sub = "i";
print ("str.count(sub, 4, 40) : ") 
str.count(sub, 4, 40)
sub = "wow";
print ("str.count(sub) : ", str.count(sub))

# endswith(suffix,[start,[end]]). Python string method endswith() returns True if the string ends with the specified suffix,
#  otherwise return False optionally restricting the matching with the given indices start and end.
suffix = "wow!!!";
print (str.endswith(suffix))
print (str.endswith(suffix,20))

suffix = "is";
print (str.endswith(suffix, 2, 4))
print (str.endswith(suffix, 2, 6))

# find/index(sub,[start,[end]]). Python string method index() determines if string str occurs in string or in a substring of string if starting index beg and ending index end are given
str1 = "this is string example....wow!!!";
str2 = "exam";

print (str1.index(str2))
print (str1.index(str2, 1))
print (str1.index(str2, 4))



# join(). The join() method takes all items in an iterable and joins them into one string.


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)


#Python string method replace() returns a copy of the string in which the occurrences of old have been replaced with new, optionally restricting the number of replacements to max.
str = "this is string example....wow!!! this is really string"
print (str.replace("is", " was"))
print (str.replace("is", " was", 3))

# split([sep[,maxsplit]]). Return a list of the words in the string S, using sep as the delimiter string. If maxsplit is given,
#  at most maxsplit splits are done. If sep is not specified or is None, any whitespace string is a separator and empty strings are removed from the result.

grocery = 'Milk, Chicken, Bread, Butter'

# maxsplit: 2
print(grocery.split(', ', 2))

# maxsplit: 1
print(grocery.split(', ', 1))

# maxsplit: 5
print(grocery.split(', ', 5))

# maxsplit: 0
print(grocery.split(', ', 0))


# splitlines([keepends]). The splitlines() method splits the string at line breaks and returns a list of lines in the string.

grocery = 'Milk\nChicken\r\nBread\rButter'

print(grocery.splitlines())
print(grocery.splitlines(True))

grocery = 'Milk Chicken Bread Butter'
print(grocery.splitlines())




#startswith(prefix[,start[,end]]). startswith() method takes a maximum of three parameters:
# startswith() method takes a maximum of three parameters:

#prefix - String or tuple of strings to be checked
#start (optional) - Beginning position where prefix is to be checked within the string.
#end (optional) - Ending position where prefix is to be checked within the string.




text = "programming is easy"
result = text.startswith(('python', 'programming'))

# prints True
print(result)

result = text.startswith(('is', 'easy', 'java'))

# prints False
print(result)

# With start and end parameter
# 'is easy' string is checked
result = text.startswith(('programming', 'easy'), 12, 19)

# prints False
print(result)


# strip([chars]) - a string specifying the set of characters to be removed from the left and right part of the string.
string = '  xoxo love xoxo   '

# Leading and trailing whitespaces are removed
print(string.strip())

# All <whitespace>,x,o,e characters in the left
# and right of string are removed
print(string.strip(' xoe'))

# Argument doesn't contain space
# No characters are removed.
print(string.strip('stx'))

string = 'android is awesome'
print(string.strip('an'))


# part C

from math import sqrt
 
def isPrime(n):
 
    # Corner case
    if (n <= 1):
        return False
 
    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
 
    return True
 
 
# Driver Code
if isPrime(11):
    print("true")
else:
    print("false")




# PART D
def disStuInfo(schoolID,firstName,lastEmail):
    print(schoolID)
    print(firstName)
    print(lastEmail)


disStuInfo("10001", "john", "john@123.com")
