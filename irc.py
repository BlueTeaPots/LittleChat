import socket
import sys
import time

class IRC:
    irc = socket.socket()
    authFilePath = "/home/drixon/.auth/bluetermpots.auth"
    authString = ""
    username = "bluetermpots"
    server = "irc.chat.twitch.tv"
    port = 6667
    
    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        with open(self.authFilePath) as authFile:
            self.authString = authFile.read()
        
    def connect(self, channel):
        # Connect to the server
        print(self.server)
        print("Connecting to: " + self.server)
        self.irc.connect((self.server, self.port))
        print("Connection attempt completed")
        
        # Authenticate with the server as bluetermpots
        print("Attempting authentication")
        self.irc.send(bytes("PASS " + self.authString + "\n", "UTF-8"))
        self.irc.send(bytes("NICK " + self.username + "\n", "UTF-8"))
        print("Sent authentication")
        
        time.sleep(5)

        # Join the requested channel
        print("Attempting channel join")
        self.irc.send(bytes("JOIN #" + channel + "\n", "UTF-8"))
        print("Sent channel join")
        
    def get_response(self):
        response = self.irc.recv(2048).decode("UTF-8")
        if response == "PING :tmi.twitch.tv\n":
            print("GOT PING")
            self.irc.send(bytes("PONG :tmi.twitch.tv\n", "UTF-8"))
            print("SENT PONG")
            respose = ""
        return response
