import lab_chat as lc
from lab_chat import get_peer_node, join_group, get_channel


def get_input(msg):
    print(msg)
    user_input = input()
    return user_input.strip()

def get_username():
    return get_input("What Is Your Username?").upper()

def get_group():
    return get_input("What Group Would You Like To Join?").upper()


def get_message():
    return get_input("What Message Would You Like To Send?")


def initialize_chat():
    username = get_username()
    peer_object = get_peer_node(username)
    group = get_group()
    join_group(peer_object, group)
    return get_channel(peer_object, group)


def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode("utf_8"))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

start_chat()


