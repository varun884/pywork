# Input / Output
x = 90
# Output --- print()
print(x )
print(100 ,end='-')
print(100,200,30045.6,78.9,"Hello" , False , sep='.' , end = '--------')
print(1,2,3,9,8,7,6,5,4 , sep = '.')

# Data Types 
#1. Numbers --- int, float, complex
x = 8968645424687656576587697556364356467576576
print(type(x))
y = 653765.235427655752763547628536543265498273947 # upto 15 places of precision
print(y)
z = 56 + 5.6j
print(type(z))

#2. Strings --- '' , "" , ''' ''' , """ """ --- strings (array of characters)
s= 'hello'
s1 = "hey"
s3 = ''' this is a multi line string . 
these are not comments'''
print(type(s) ,type(s1) , type(s3))
print(s , s1, s3 , sep = ',')

#3. Boolean --- True - 1 / False - 0 (are subclasses to integers)
x = True
y = False

# Input() ---- always takes string format, hence Typecasting is required
# Typecast --- int() , float(), complex() , str()
val = int(input("Enter Here : "))
val2 = float(input('Enter Again : '))
print("You Entered : " , type(val))
print(val + val2)

