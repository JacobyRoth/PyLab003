
def chat_task(ctx, pipe, n, group):  # function name is chat_task
ctx: This is a ZeroMQ Connection Context
pipe: This is a communications pipe polled by ZeroMQ for messages.
n: This is the peer to peer node my chat app is connected as
group: This is the peer chat group I wanted to join
The chat_task method does not return anything, it appears to be the send/recieve manager.

def get_peer_node(username) # function name is get_peer_node
username: this is the username of the peer you want to get
the get_peer_node returns the username

def join_group(node, group): #function name is join_group
node: This is the node for peer to peer connection
group: the provided group you want to join
The join_group method does not return anything

def get_channel(node, group): # function name is get_channel
node: node for peer to peer connection
group: provided group
The get_channel method return the channel in the provided node and group