
# format () Method :

'''

Performs a string formatting operation. The string on which this method
is called can contain literal text or replacement fields delimited by braces {}.
Each replacement field contains either the numeric index of a positional argument,
or the name of a keyword argument.
Returns a copy of the string where each replacement field is replaced
with the string value of the corresponding argument.
'''

str1 = "Hello World!"  # 11 characters

str2 = 'This is an example string'


print ("Your name is %s and your account id is %d" %("Kevin",14456))

print ("Calling str1 {0} and calling str2 {1}".format(str1,str2))

print ("Value1 {} Value2 {} and Value3 {}".format("python",100,"pycharm"))

print ("Value1 {1} Value2 {0} and Value3 {2}".format("python",100,"pycharm"))

print ("Value1 {a} Value2 {b} and Value3 {c}".format(a="python",b=100,c="pycharm"))