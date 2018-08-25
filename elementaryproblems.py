#-------------------------------
#    ____  _           _______       ______                          _____ __            ___
#   / __ \(_)  _____  / / ___/____  / __/ /__      ______ _________ / ___// /___  ______/ (_)___  _____
#  / /_/ / / |/_/ _ \/ /\__ \/ __ \/ /_/ __/ | /| / / __ `/ ___/ _ \\__ \/ __/ / / / __  / / __ \/ ___/
# / ____/ />  </  __/ /___/ / /_/ / __/ /_ | |/ |/ / /_/ / /  /  __/__/ / /_/ /_/ / /_/ / / /_/ (__  )
#/_/   /_/_/|_|\___/_//____/\____/_/  \__/ |__/|__/\__,_/_/   \___/____/\__/\__,_/\__,_/_/\____/____/
#
# Solutions to Adriann's Simple Programming Problems in Python
# These are not THE or the only solutions to these problems but they are what I have come up with.
#-------------------------------
from operator import mul
from functools import reduce
from random import randint
from math import sqrt

# Write a program that prints ‘Hello World’ to the screen.
def helloworld():
	print("Hello World")

# Write a program that asks the user for their name and greets them with their name.
def greet():
	print("Hello,", str(input()))

# Modify the previous program such that only the users Alice and Bob are greeted with their names.
def greetAliceOrBob():
	name = str(input())
	# Print Hello + their name, only if their name is Alice or Bob, only print Hello if not.
	#Uses python's ternary operators
	print("Hello, " + name if name == "Alice" or name == "Bob" else "Hello")

# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n
def sum1ToN():
	n = int(input("Give me a number: "))
	#Prints the sum of the list form of the range 1, to n+1 to account for the range function only going up to the second number not to the second number
	print(sum(list(range(1, n + 1))))

# Modify the previous program such that only multiples of three or five are considered in the sum
def sum1ToNIfDivisible():
	n = int(input("Give me a number: "))
	# Print the sum of each x in range 1 to N if X is evenly divisible by 3 or 5
	print(sum([x for x in range(1, n + 1) if x % 3 == 0 or x % 5 == 0]))

# Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.
def sumOrProduct1ToN():
	n = int(input("Give me a number: "))
	opt = str(input("Sum or factorial: "))
	if (opt == "factorial"):
		return print(reduce(mul, list(range(1, n + 1)), 1))
	return print(sum(list(range(1, n + 1))))

# Write a program that prints a multiplication table for numbers up to 12.
def table(n = 12):
	# Forget making any ordinary multiplication table that justs prints it in a string/array
	# I made that *expletive* graphical AND it can go up to any number you want.
	line = ""
	# The code explains it self once you run it
	# Also this code would be way simpler if I didn't want it to be cosmetically pleasing
	# Most of this code is for making the numbers visually line up as much as possible going down columns
	for row in range(1, n + 1):
		for column in range(1, n + 1):
			if row == 1:
				line += str(row * column) + "  "
			elif column == 1 and row < 10:
				line += str(row * column) + "  "
			elif column == 2 and row < 5:
				line += str(row * column) + "  "
			elif column == 3 and row < 4:
				line += str(row * column) + "  "
			elif column == 4 and row == 2:
				line += str(row * column) + "  "
			elif column > 9 and row < 10:
				line += str(row * column) + "  "
			else:
				line += str(row * column) + " "
		line += "\n"
	print(line)

# Write a program that prints all prime numbers.
# So there are multiple ways to do this, the two main ways are Trial Division, which I'm sure most people did,
# or the Sieve of Eratosthenes. Since I know how to implement both, I did both.
# Also, it said write a program that prints all prime numbers. It is impossible to print all prime numbers, because it would never terminate as it would be like trying to print to infinity. You would run out of memory fast.
def allPrimes():
	# Trial Division
	i = 2
	while True:
		if isPrime(i):
			print(i)
		i++

	# Sieve of Eratosthenes
	for x in eratosthenes((2**63)-1):
		print(x)

def isPrime(n):
	# If n is 2 or 3 it's obviously a prime
    if n == 2 or n == 3:
		return True
	# If n is divisible by 2 or is less than 2 it's obviously not a prime
    if n % 2 == 0 or n < 2:
		return False
	# I would use N ** .5 to be even less dependent on libraries but Math.sqrt() is more understandable and is faster
    for i in range(3, sqrt(n) + 1, 2):
        if n % i == 0:
			return False
    return True

#I know it said all prime numbers not all prime numbers up to n, but just input N as 2^63 -1 and call it a day
def eratosthenes(n):
	# Make a list of all the integers less than or equal to n (and greater than one). Strike out the multiples of all primes less than or equal to the square root of n, then the numbers that are left are the primes.
	isPrime = {}
	# Create a list of True values except for 1 because 1 is obviously not a prime so it's safe to cross out
	isPrime[1] = False
	for i in range(2, n + 1):
		isPrime[i] = True

	# Actual sieve logic/checkprime logic
	checkn = sqrt(n)
	for i in range(2, checkn + 1):
		if isPrime[i]:
			for factor in range(2, n + 1):
				j = i * factor
				if (j > n): break
				isPrime[j] = False
	primes = []
	# If the Boolean in the index in isPrime is True then append index to prime list
	for i in range(1, n + 1):
		if isPrime[i]:
			primes.append(i)
	return primes

# Write a guessing game where the user has to guess a secret number.
def higherorlower():
	#Generate a random number between 1 and 100
	number = randint(1, 100)
	guess = 0
	guesses = []
	#While the guess is not equal to the generated number
	while guess != number:
		guess = input("Guess: ")
		if guess:
			if guess.isdigit():
				guess = int(guess)
				if (guess not in guesses):
					guesses.append(guess)
				if (guess > number):
					print("Lower!")
				if (guess < number):
					print("Higher!")
	print("Congratulations! The number was " + str(number))
	print("It took you " + str(len(guesses)) + " guesses to find this number")

# Write a program that prints the next 20 leap years.
def next20leapyears(year = 2018):
	leapyears = []
	#Only print the next 20 leap years
	while len(leapyears) is not 20:
		#If the last 3 digits of the year are divisble by 4
		if int(str(year)[1:]) % 4 == 0:
			if year % 100 == 0 and year % 400 == 0:
				leapyears.append(year)
			else:
				leapyears.append(year)
		year += 1
	print(leapyears)

# Write a program that computes 4⋅∑ k=1 10^6 (−1)k + 1 / 2k−1.
def summationprob():
	s = 0
	for k in range(1, (10 ** 6) + 1):
		s += (-1 ** (k + 1)) / ((2 * k) - 1)
	return s * 4
