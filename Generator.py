import os
import mnemonic
from pycoin.key.BIP32Node import BIP32Node

# Read in the mnemonic words from the input file
mnemonic_words = []
with open("mnemonic_words.txt", "r") as f:
    mnemonic_words = f.read().splitlines()

# Generate all possible 12-word mnemonic combinations
mnemonic_combinations = []
for i in range(len(mnemonic_words) - 11):
    for j in range(i+11, len(mnemonic_words)):
        mnemonic_combinations.append(mnemonic_words[i:j+1])

# Create a BIP32Node for each mnemonic and generate the bitcoin address
addresses = []
for mnemonic in mnemonic_combinations:
    try:
        seed = mnemonic.to_seed()
        root = BIP32Node.from_master_secret(seed)
        address = root.bitcoin_address()
        addresses.append((mnemonic, address))
    except Exception as e:
        print(f"Error generating address for mnemonic {mnemonic}: {e}")

# Write the results to an output file
with open("mnemonic_addresses.txt", "w") as f:
    for mnemonic, address in addresses:
        f.write(f"{mnemonic}: {address}\n")