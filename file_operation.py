################################## OPERATIONS ON FILES ##################################

#import library
import os

print """
ASSIGNMENT NO. : 2
ASSIGNMENT     : OPERATIONS ON FILES
"""

# display_menu function definition
def display_menu():
	# default user choice
	user_choice = 0
	
	# repeat till user exit
	while(user_choice!=4):
		# print menu
		print "\t\t MENu"
		print "\t 1. Open File"
		print "\t 2. Copy File contents"
		print "\t 3. Delete file"
		print "\t 4. Exit"
		
		# accept user_choice 
		user_choice=int(input( "\t Enter your choice:"))
		
		# check for available options
		if user_choice == 1:
			os.system('clear')
			print "\t\t OPEN FILE OPERATION"
			# open_file function call
			open_file()
		elif user_choice == 2:
			os.system('clear')
			print "\t\t COPY FILE CONTENTS"
			# copy_file function call
			copy_file()
		elif user_choice == 3:
			os.system('clear')
			print "\t\t DELETE FILE OPERATION"
			# delete_file function call
			delete_file()
		elif user_choice == 4:
			# program exit
			exit(0)
		else:
			print "You have entered wrong choice!!!"

# open_file function definition
def open_file():
	# accept file name from user
	file_name = raw_input('Enter the name of file: ')
	# try block
	try:
		# open file in default read mode
		myFile = open(file_name)
	except IOError:
		print "The file not found error!!!"
		return 
	# try end
	
	# try block
	try:
		# print file contents
		print myFile.read()
	except:
		print "Error while reading a file!!!"
	
	finally:
		myFile.close()
	# try end
	
# copy_file function definition
def copy_file():
	# accept source-file name from user
	source_file_name = raw_input('Enter the Source file name: ')
	
	# try bllock
	try:
		# open file in default read mode
		source_file = open(source_file_name)
	
	except IOError:
		print "The file not found..."
		return
	# try end	
	
	# accept destination file and open it in write mode
	destination_file_name = raw_input('Enter the destination file name: ')
	destination_file = open(destination_file_name,'w')
	
	# try block
	try:
		# copy contents of source file in destination file
		destination_file.write(source_file.read())
		
	except IOError:
		print "The file copying error!!!"
		return 
	finally:
		source_file.close()
		destination_file.close()
	# end try
			
# delete_file function definition
def delete_file():
	# accept file name from user
	file_name = raw_input('Enter the file name: ')
	
	# try block
	try:
		# try block 
		try:
			# check for file exist
			del_file = open(file_name)
			# if exists ask for confirmation
			ans = raw_input('Are you sure? y/n : ')
			if ans == 'y':
				del_file.close()
				# remove file
				os.system('rm '+ file_name)
			elif ans == 'n':
				del_file.close()
				return
			else:
				print "You have entered wrong choice!!!"
			
		except IOError:
			print "File not  found error!!!"
			return
			
		# try end
		
	except:
		print "Error while deleting file"
		return
	# try end
	
# display_menu function call
display_menu()
	
