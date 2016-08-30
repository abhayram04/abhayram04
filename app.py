import sys,os,random

print "Hey, welcome to PyGame!"
name = input("Enter a number between 1 and 100")
num = random.randint(1,100)
if num == name:
	print "You got it right!"
else:
	print "You are wrong!"

