# coding=utf-8
import config
import utils
import socket
import re
import time
import thread
from time import sleep
from emote import *



def main():
    s = socket.socket()
    s.connect((config.HOST, config.PORT))
    s.send("PASS {}\r\n".format(config.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(config.NICK).encode("utf-8"))
    s.send("JOIN #{}\r\n".format(config.CHAN).encode("utf-8"))

    chat_message = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    #utils.mess(s, "Zdarova")

    thread.start_new_thread(utils.fillOpList, ())
    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("POND :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0)
            message = chat_message.sub("", response)
            print(response)


            if message.strip() == "!time":
                utils.mess(s, "Стрим идёт уже " + time.strftime("%A %B %d %Y"))
            if message.strip() == "!randomemote":
                utils.mess(s, )
        sleep(1)





if __name__ == "__main__":
    main()