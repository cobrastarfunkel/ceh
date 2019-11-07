#!/usr/bin/python
import base64
import string
from encode import Encode
from decode import Decode
import json

"""
To make sure it works correctly
"""
test_var = "Test with a long string"
base64_test = base64.b64encode(test_var)
print("Original Text --> " + base64.b64decode(base64_test))
print("Encoded with Python Lib --> " + base64_test)


"""
The dictionary below is here in case the json file is not present
in the directory.  This will ensure the table is present for the
Encode and Decode classes, but is not necessary to run the code.
"""
base64_dict = { 0 : "A", 1 : "B", 2 : "C", 3 : "D", 4 : "E",
5 : "F", 6 : "G", 7 : "H", 8 : "I", 9: "J", 10 : "K", 11 : "L",
12 : "M", 13 : "N", 14 : "O", 15 : "P", 16 : "Q", 17 : "R",
18 : "S", 19 : "T", 20 : "U", 21 : "V", 22 : "W", 23 : "X",
24 : "Y", 25 : "Z", 26 : "a", 27 : "b", 28 : "c", 29 : "d",
30 : "e", 31 : "f", 32 : "g", 33 : "h", 34 : "i", 35 : "j",
36 : "k", 37 : "l", 38 : "m", 39 : "n", 40 : "o", 41 : "p",
42 : "q", 43 : "r", 44 : "s", 45 : "t", 46 : "u", 47 : "v",
48 : "w", 49 : "x", 50 : "y", 51 : "z", 52 : "0", 53 : "1",
54 : "2", 55 : "3", 56 : "4", 57 : "5", 58 : "6", 59 : "7",
60 : "8", 61 : "9", 62 : "+", 63 : "/" }
with open('b64_table.json', 'w') as f:
  json.dump(base64_dict, f)


def main():
   
  en = Encode(test_var)
  en.encode(test_var)
  print('Encoded String-->: '+ en.encoded_string)

  de = Decode(test_var)
  de.decode(en.encoded_string)
  print('Decoded String-->: '+ de.decoded_string)



if __name__ == "__main__":
  main()
