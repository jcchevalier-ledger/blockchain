from Blockchain import Blockchain

if __name__ == '__main__':
    blockchain = Blockchain()
    t1 = blockchain.new_transaction("JC", "Julien", 10)
    t2 = blockchain.new_transaction("Julien", "Martin", 5)
    t3 = blockchain.new_transaction("JC", "Martin", 2)
    blockchain.new_block(187)

    print(blockchain.chain)
