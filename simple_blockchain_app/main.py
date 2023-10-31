import time
from flask import Flask, jsonify
from flask import Flask, jsonify
from block import Block   # Adjust this import based on your file names
from blockchain import Blockchain
app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine_block():
    new_block = Block(len(blockchain.chain), blockchain.get_latest_block().hash, time.time(), "New Block")
    blockchain.add_block(new_block)
    return jsonify(message="Block mined successfully"), 200

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify(chain=[str(block) for block in blockchain.chain]), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
