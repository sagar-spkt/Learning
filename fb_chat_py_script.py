import fbchat
from getpass import getpass
username = 'spkt.sagar'
client = fbchat.Client(username, getpass())
friends = client.getUsers('Pawan Paudel')
sent = client.send("Rowdy Paudel", friends[0].uid)