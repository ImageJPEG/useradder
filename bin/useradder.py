#!/usr/bin/env python3

from ldap3 import Server, Connection, ALL, NTLM
import getpass

print('Welcome to mass useradder for Active Directory')
hostname = input('Please tell me the IP or hostname of the server you\'d like to connect to:\n')
server = Server(hostname, get_info=ALL)

print('I will now try to connect to that server, please wait')

conn = Connection(server)
conn.bind()

print(conn)
input('Press Enter to continue...')
print(server.info)
input('Press Enter to continue...')
print('Alright, now if you didn\'t receive any errors, let\'s try logging you in as a user')

conn.unbind()
del conn

domain = input('Please tell me your domain:\n')
person = input('Please tell me your user name:\n')
passphrase = getpass.getpass('Please enter your password:\n')
combo = domain + "\\" + person
conn = Connection(server, user=combo, password=passphrase, authentication=NTLM)
print(conn.extend.standard.who_am_i())
exit()
