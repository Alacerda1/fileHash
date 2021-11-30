import hashlib
import collections

count = 0
# Basically a true or false statement until
# files are outside of F0 to F21
while count < 21:
    # set filepath to equal individual files within files doc(including file type)
    file_path = "files/f" + str(count) + ".docx"
    # sets max amount of bits
    BLOCK_SIZE = 65536
    # Library(in this case SHA3 512)
    hash_handler = hashlib.sha3_512()



    # Open file path as binary
    with open(file_path, 'rb') as f:
        fb = f.read(BLOCK_SIZE)

        # Iterates through file using a while loop adding 1 to each file until
        # outside of parameters then end
        while fb:
            hash_handler.update(fb)
            fb = f.read(BLOCK_SIZE)


    # Iterates through files until count reaches 21
    count = count + 1

    file_hexHash = hash_handler.hexdigest()

    print(f"{file_path} file hash value: \n{file_hexHash}", file=open('hash.txt', 'a'), )







