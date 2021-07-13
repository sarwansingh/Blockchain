#Blockchain
import hashlib
import datetime
import json
from flask import Flask, jsonify, request, render_template
import requests

from uuid import uuid4
from urlparse import urlparse

#Create a blockchain
class Blockchain:
    def __init__(self):
        #constructor
        self.chain = []
        self.transactions = []
        #genesis block being created, in constructor first time it will trigger
        self.create_block(proof = 1, previous_hash = '0')
        self.nodes=set()
        
    def create_block(self,proof,previous_hash):
        #Define essential data for the blocks
        block = {'index' : len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transaction' : self.transactions
                 }
       
        #make transaction list empty
        self.transactions = []
        self.chain.append(block)
        return block
   
    def get_previous_block(self):
        return self.chain[-1]
   
    def proof_of_work(self,previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 -
                                                previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof=True
            else:
                new_proof += 1
        return new_proof
               
    def hash(self,block):
        #json.dumps encodes any python object  into json formatted string
        encoded_block = json.dumps(block).encode()
        #hash libraries deal with byte objects
        return hashlib.sha256(encoded_block).hexdigest()
    
    def is_chain_valid(self,chain):
       
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
           
            if block['previous_hash'] != self.hash(previous_block):
                return False
           
            #check the validity of block also
            previous_proof = previous_block['proof']
            new_proof = block['proof']
            hash_operation = hashlib.sha256(str(new_proof**2 -
                                                previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
           
            previous_block = block
            block_index += 1        
        return True
    
    #Format of transaction Sender, Receiver, Amount
    def add_transaction(self,sender,receiver,amount):
        self.transactions.append({'sender' : sender,
                                  'receiver' : receiver,
                                  'amount' : amount})
       
        previous_block = self.get_previous_block()
        return previous_block['index'] + 1
      
    def add_nodes(self, address):
        parsed_url=urlparse(address)
        #in python to add an element in a list we use append
        #in python to add an element in a set we use add
        self.nodes.add(parsed_url.netloc)
        
blockchain = Blockchain()
app = Flask(__name__)  
node_address = str(uuid4()).replace('-','')

@app.route('/')
def hello_world():
	return render_template("index.html") 
	
@app.route('/add_trans')
def addTransaction():
	return render_template("transform.html")
	
@app.route('/mine_block', methods = ['GET'])
def mine_block():
   
    previous_block = blockchain.get_previous_block()
   
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
   
    previous_hash = blockchain.hash(previous_block)
   
    #default transaction
    blockchain.add_transaction(sender=node_address,receiver = 'sarwan singh',
                               amount = 10)
      
    block = blockchain.create_block(proof, previous_hash)
    response = {'previous_block': previous_block , 
				'previous_proof': previous_proof,
				'proof' :  proof , 
				'previous_hash': previous_hash , 
				'message' : '****Congrats you mined a block***',
                'index': block['index'], 
                'timestamp': block['timestamp'],
               'proof': block['proof'],
               'previous_hash': block['previous_hash'],
               'transaction'   : block['transaction']}
    #whenever request on webpage
    return jsonify(response), 200

@app.route('/mine_block1', methods = ['GET'])
def mine_block1():
   
    previous_block = blockchain.get_previous_block()
   
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
   
    previous_hash = blockchain.hash(previous_block)
   
    #default transaction
    blockchain.add_transaction(sender=node_address,receiver = 'sarwan singh',
                               amount = 10)
      
    block = blockchain.create_block(proof, previous_hash)
    response = {'previous_block': previous_block , 
				'previous_proof': previous_proof,
				'proof' :  proof , 
				'previous_hash': previous_hash , 
				'message' : '****Congrats you mined a block***',
                'index': block['index'], 
                'timestamp': block['timestamp'],
               'proof': block['proof'],
               'previous_hash': block['previous_hash'],
               'transaction'   : block['transaction']}
    #whenever request on webpage
    return render_template("index.html", data=response)

#Getting the chain of blocks
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain':blockchain.chain,
                'length':len(blockchain.chain)}
   
    return jsonify(response), 200

#Getting the chain of blocks
@app.route('/get_chain1', methods = ['GET'])
def get_chain1():
	response = {'chain':blockchain.chain,'length':len(blockchain.chain)}
				
	return render_template("index.html", data=response) # jsonify(response), 200
	
	
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message' : 'The chain is valid'}
    else:
        response = {'message' : 'chain is not valid'}
    return jsonify(response), 200

# url is accessed from the browser	
@app.route('/add_transaction1', methods = ['POST'])
def add_transaction1():
	if request.method == 'POST':
		sender   = request.form['txtsender']
		receiver = request.form['txtreceiver']
		amount   = request.form['txtamount']
		index = blockchain.add_transaction(sender, receiver, amount)
		response = {'message' : 'The transaction has been added to block '+str(index)}
		return render_template("index.html", data=response)# jsonify(response), 201

#url is accessed from Postman chrome app		
@app.route('/add_transaction', methods = ['POST'])
def add_transaction():
	json = request.get_json()
	transaction_keys = ['sender','receiver','amount']
	if not all(key in json for key in transaction_keys):
		return 'Some values are missing',400
	index = blockchain.add_transaction(json['sender'],
									   json['receiver'],
									   json['amount'])
	response = {'message' : 'The transaction has been added to block'+str(index)}
	return jsonify(response), 201
	
@app.route('/about')
def fabout():
	return '<html><h1>This is about page</h1><hr> <a href="/">Main Page</a></html> '
	
if __name__ == '__main__':
	app.run(debug="true")