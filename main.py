from hacking import *

# receive from cmd
args = sys.argv
address = (args[1], int(args[2]))

# build socket
with socket.socket() as client_socket:
    client_socket.connect(address)
    # send encoded message
    login = hack_login(client_socket)
    password = hack_password(login, client_socket)
    print(json.dumps({'login': login, 'password': password}))
    client_socket.close()

