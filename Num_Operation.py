################################## OPERATIONS ON NUMBERS ##################################

print """
ASSIGNMENT NO. : 1
ASSIGNMENT     : OPERATIONS ON NUMBERS
"""

def display_menu():
	user_choice = 0
	
	# Repeat until choice = exit
	while user_choice != 5:
		# Print Menu
		print "\t\t MENU"
		print "1.\t Factorial of Number"
		print "2.\t Compare"
		print "3.\t Prime Number"
		print "4.\t Palindrome"
		print "5.\t Exit"
		print "Enter your choice:"
		
		# Accept user choice
		user_choice=int(input())
		
		if(user_choice == 1):
			# Factorial function call		
			fact()
		elif(user_choice == 2):
			# Compare function call
			compare()
		elif(user_choice == 3):
			# Prime_Number function call
			prime_number()
		elif(user_choice == 4):
			# Palindrome function call
			palindrome()
		elif(user_choice == 5):
			# Exit the program
			exit()
		else:
			# Print the error
			print "You have entered wrong choice!!!"
			
def fact():
	# Accept user input 
	num = int(input("Enter the number: "))
	# Set fact to 1
	fact = 1
	
	# repeat until num equals to 1
	while(num >= 1 ):
		fact = fact * num
		num = num - 1
		
	# Print the factorial
	print "Factorial of number is ", fact

def compare():
	# Accept 3 user inputs ex. : 4, 6, 9
	num1, num2, num3 = input("Enter the three numbers: ")
	
	# Compare three numbers and print result
	if ((num1 > num2 > num3) == True ):
		print num1," is greatest..."
	elif((num1 < num2 > num3) == True):
		print num2," is greatest..."
	else:
		print num3," is greatest..."
		
def prime_number():
	# Accept user input
	num = int(input("Enter the number: "))
	# set default divisor to 2
	divisor = 2
	# set default result of mod to -1
	result = -1
	
	# repeat until divisor < number and remainder != 0 
	while divisor < num and result != 0:
		result = num % divisor
		divisor += 1
	
	# check for prime number
	if result == 0:
		print "The number is not Prime"
	else:
		print "The number is prime"

def  palindrome():
	# Accept user string 
	str_var = raw_input("Enter the string: ")
	
	# Reverse the user string 
	reverse_str = str_var[::-1]
	
	# Compare both strings to check whether it is palindrome
	if str_var == reverse_str:
		print "The string is palindrome..."
	else:
		print "The string is not palindrome..."

# Display function call
display_menu()



		
			
		
