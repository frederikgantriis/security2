import enum

p = 1000003


def get_p():
    return p


def sum_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


def recieve_data(connstream, numbers):
    data = connstream.recv(1024)
    # empty data means the client is finished with us
    while data:
        result, numbers = add_numbers_to_arr(connstream, data, numbers)
        if not result:
            # we'll assume do_something returns False
            # when we're finished with client
            break
        data = connstream.recv(1024)
    # finished with client
    return numbers


def add_numbers_to_arr(connstream, data, numbers):
    # do somehing with the remote user!
    numbers.append(int(data.decode()))

    print("Recieved: ", data.decode())
    return False, numbers


class Peer(enum.Enum):
    Alice = 10024
    Bob = 10025
    Charlie = 10026
