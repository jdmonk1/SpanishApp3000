from codecs import encode

with open('new1.txt', 'rb') as reader:
     # Read & print the first 5 characters of the line 5 times
     print(encode(reader.readline(80), 'hex'))