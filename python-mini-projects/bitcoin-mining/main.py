from hashlib import sha256
import time


# max number of iteration of the Nonce
MAX_NONCE = 100000000000

# define the hash function
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

# mining the block
def mining(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = "0" * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)

        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully minded bitcoins with nonce value: {nonce}")
            return new_hash
        
    raise BaseException(f"Couldn't find correct hash after trying {MAX_NONCE} times.")

if __name__ == "__main__":
    transactions = """
    Player1->Player2->200,
    Player3->Player4->450
    """
    difficulty = 6

    start_time = time.time()
    print("start mining...")
    new_hash = mining(
        5, 
        transactions,
        "0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7",
        difficulty,
    )
    total_time = str((time.time() - start_time))
    print(f"end mining. Mining took: {total_time} seconds.")
    print(new_hash)

