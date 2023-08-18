from flask import Flask, jsonify, request
import hashlib
import time

app = Flask(__name__)

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

# Create the blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

@app.route('/mine', methods=['GET'])
def mine_block():
    new_block_data = "Block #" + str(previous_block.index + 1)
    new_block = create_new_block(previous_block, new_block_data)
    blockchain.append(new_block)
    return jsonify(message="New block mined!", index=new_block.index, hash=new_block.hash), 200

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain:
        chain_data.append({
            'index': block.index,
            'timestamp': block.timestamp,
            'data': block.data,
            'hash': block.hash
        })
    return jsonify(chain_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
