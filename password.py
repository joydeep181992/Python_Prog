#! /usr/bin/python3
# password.py - An insecure password locker program.

password = {'facebook':'123fdfaf',
	'google':'32111','yahoo':'fafaf2314s'}

# first line of command line i.e. sys.argv[0] = password.py
# i.e actually ~user: python3 password.py account

import sys,pyperclip

account = sys.argv[1]
if len(sys.argv) < 2:
	print('fewer argument in command line......')
	sys.exit()

if account in password:
	pyperclip.copy(password[account])
	print('the password for '+account+ 'copied to clipbord use "ctrl+v"')
else:
	print('there is no account in such name please add it')






