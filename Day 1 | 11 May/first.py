import hashlib

class XCoinBlock:

    def __init__(self,previous_block_hash,transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "PersonA sends 2 XC to PersonX"
t2 = "PersonB sends 2.6 XC to PersonX"
t3 = "PersonX sends 5.6 XC to PersonC"
t4 = "PersonC sends 3.2 XC to PersonX"
t5 = "PersonD sends 0.4 XC to PersonA"
t6 = "PersonX sends 0.9 XC to PersonD"

initial_block = XCoinBlock("0x0",[t1,t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = XCoinBlock(initial_block.block_hash,[t3,t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = XCoinBlock(initial_block.block_hash,[t5,t6])

print(third_block.block_data)
print(third_block.block_hash)