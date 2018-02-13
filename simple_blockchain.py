# The tutorial used for this talks to Blockchain over HTTP
# You need to have an HTTP client, like Postman or cURL

# Each block has an index, a timestamp (in Unix time), a list of transactions, a proof (more on that later)
# and the hash of the previous Block

# So new block contains within itself a hash of the previous Block
# This is crucial because it's what gives blockchain immutability
# ie if an attacker corrupted an earlier block then all subsequent blocks will contain
# incorrect hashes. This is the core idea behind blockchain.

# When our Blockchain is instantiated we’ll need to seed it with a
# genesis block—a block with no predecessors. We’ll also need to add a “proof” to our
# genesis block which is the result of mining (or proof of work).

# SHA are secure hash algorithms, a family of cryptographic hash functions

# Proof of Work

# A PoW algorithm is how new Blocks are created, or mined on the blockchain
# The goal of PoW is to discover a number which solves a problem
# The number must be difficult to find but easy to verify by anyone on the network

# A very simple example
# Let's decide a hash of some integer x multiplied by another y must end in 0
# So, hash(x * y) = ac23dc...0

# I'm guessing that x is like the key of the hash function, our input.
# Then this x is multiplied by y to create the input into the hash function
# The function is applied and a long string is produced

# To implement this

# from hashlib import sha256
# x = 5
# y = 0  # We don't know what y should be yet...
# while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "0":
#     y += 1
# print(f'The solution is y = {y}')

# the solution here is y = 21, since the produced hash ends in 0
# hash(5 * 21) = 1253e9373e...5e3600155e860

# So we keep on trying diff y's and multiply that by x to give our input into the hash function


# In Bitcoin, the PoW algorithm is called Hashcash, and it's not too diff from our example.
# It's the algorithm miners race to solve in order to create a new block.
# The difficulty is determined by the number of characters searched for in a string
# The miners are then rewarded for their solution by receiving a coin

# To create an API for our blockchain, we are going to use Python Flask Framework.
# It's a micro-framework and it makes it easy to map endpoints to Python functions.
# This allows us to talk to our blockchain over the web using HTTP requests

# We’ll create three methods:
#
# /transactions/new to create a new transaction to a block
# /mine to tell our server to mine a new block.
# /chain to return the full Blockchain.

# To run the blockchain, you need to run a server by opening the python file in terminal
# To mine a block:
# Open up Postman and make a GET request to http://localhost:5000/mine
# To create a new transaction:
# Use Postman and make POST request to http://localhost:5000/transactions/new with a body containing
# our transaction structure
# To view the full chain:
# Use Postman and make a GET request to http://localhost:5000/chain

# Remember the whole point of blockchains is that they are all decentralised.
# We have to implement a Consensus algorithm to make sure all nodes reflect the same chain

# Before we implement a Consensus algorithm, we need a way to let a node know about neighbouring nodes
# on the network. Each node on the network should keep a registry of other nodes on the network
# We've used a set() to hold the list of nodes. This is an easy way of ensuring new nodes are idempotent
# meaning that no matter how many times we add a specific node, it appears only once.

# So conflict is when one node has a different chain to another node. To resolve this, we make a rule that
# the longest valid chain is the de-facto one.