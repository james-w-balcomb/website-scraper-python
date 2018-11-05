import socket


def check_socket(host_name, port_number):

    # socket.gethostbyname('google.com')

    socket_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_socket.settimeout(1)

    socket_socket_connect_ex = socket_socket.connect_ex((host_name, port_number))

    if socket_socket_connect_ex == 0:

        print("Port is open")

        status = True

    else:

        print("Port is not open")

        status = False

    return status


def does_hostname_resolves(host_name):

    try:

        socket.gethostbyname(host_name)

        status = True

    except socket.error:

        status = False

    return status
