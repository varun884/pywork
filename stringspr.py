# # Strings ---> Array Like Layout, Immutable , Indexed
# # Create Read Update Delete
# # Create ==== '' , "" , ''' ''' , """ """ 
# es = '' # False
# s1 = 'hello, world'
# s2 = "hey, world"
# s3 = '''This is multiline
# in another line...'''
# print(type(s1) , type(s2) , type(s3) , type(es))
# # Read ---- use indices ---- 2 way indexing
# #Left To Right
# print(s1[0] , s1[1] , s1[2])
# # Right To Left --- using negative indices
# print(s1[-1] , s1[-2] , s1[-3])

# # Update  ---- immutable
# #s1[0] = 'R' not allowed
# s1 = 'new string' # overriding the last s1, not updating 

# # Delete
# print(es)
# del es
# #print(es)
# #del s2[3]

# # Traversal
# s = 'array like object in string'
# #s[0] , s[1] , s[2] , s[3]
# # i = 0
# # while i < len(s):
# #     print(s[i])
# #     i += 1
# # using for loop
# for i in range(len(s)):
#     print(s[i] , end = ' ')
# print()
# for i in s:
#     print(i , end = ' ')
# #print(len(s))
# print()
# while True:
#     st = input("Enter A String : ")
#     if st == '':
#         break 
#     else:
#         continue
s = 'parallelogram'
#print(len(s))
# news = ''
# for i in range(4,10):
#     news += s[i]
# print(news)
# slicing --- [beg = 0:end = len(string):step = 1]
print(s[2:7:1])
print(s[::])

# Reverse a string
# s = 'circle'
# #for i in range(len(s)-1,-1,-1): #(beg-end,end-beg,step)
# #    print(s[i],end='')
# print(s[::-1])# interchange the values of beg and end itself

# ###############################################################3
# # Methods
# # Universal functions
# s = 'hello, world' # on the basis of ascii table / utf-8 bit
# type(s)
# len(s)
# ord('a')
# chr(125)
# print(chr(999))
# s = 'this is a string'
# print( min(s),max(s))
# #int() float()
# x = 908
# print(str(x))

# Methods --- object
s = 'this is a string'
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
s = 'Hello, World'
print(s.swapcase())
print(','  in   s)
print(s.index('o'))
print(s.find('x')) # -1 ---> Not FOUND
# Return Boolean 
s = 'alphabeticall'
print(s.isupper())
print(s.islower())
print(s.istitle())
print(s.isalpha())
s = '65726354 a'
print(s.isdigit())
print(s.isalnum())


s = 'parallelogram'
print(s.count('l'))
#strip() , lstrip(), rstrip()
s = '       hello, world     '
print(s.rstrip() , 'hey' , sep = ',')
s = 'rediff'
print(s.ljust(10 , '$')) 
print(s.rjust(20 ," "))
print(s.rjust(15 ," "))
print(s.rjust(10 ," "))
print(s.center(50 , "$"))

x,y,z,a = 90,80,100,"StringTypeValue"
print("{} , {} and {} are integers".format(x,y,z))
print(f"{a}, {x} , {y} , {z} are all objects in Python!") # Formatted SString

# print("Table")
# number_ = int(input("Enter A Number : "))
# for i in range(1,11):
#     print(f"{number_} x {i} = {number_ * i}")

s = 'parallelogram'
print(s.replace('llel' , '#' , 2))


# maketrans ---> output(dictionary) ---> translate
s = 'this is a sample string for demo purposes'
outstr = 'aeiou'
instr = f'{chr(333)}{chr(444)}{chr(555)}{chr(666)}{chr(777)}'
len(outstr) == len(instr)
table = "".maketrans(outstr , instr) # returns a dictionary
print(table)
print(s.translate(table))


s = 'hey, this is a string?'

print(s.startswith('hey'))
print(s.endswith("?"))

































