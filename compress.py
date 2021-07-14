
from struct import *

def LZW_Compress(data, filename):
    
    # Building the dictionary.
    maximum_table_size = pow(2,15)      
    dictionary_size = 256                   
    dictionary = {chr(i): i for i in range(dictionary_size)}    
    string = ""             
    compressed_data = []    # variable to store the compressed data.

    # iterating through the input symbols.
    # Applying LZW Compression algorithm
    for symbol in data:                     
        string_plus_symbol = string + symbol # get input symbol.
        if string_plus_symbol in dictionary: 
            string = string_plus_symbol
        else:
            compressed_data.append(dictionary[string])
            if(len(dictionary) <= maximum_table_size):
                dictionary[string_plus_symbol] = dictionary_size
                dictionary_size += 1
            string = symbol

    if string in dictionary:
        compressed_data.append(dictionary[string])

    # storing the compressed string into a file (byte-wise).
    # out = filename.split(".")[0]
    output_file = open(filename, "wb")
    for data in compressed_data:
        output_file.write(pack('>H',int(data)))
        
    output_file.close()