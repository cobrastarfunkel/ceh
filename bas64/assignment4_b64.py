#!/usr/bin/python
"""
@author: Ian Cobia

The main program that drives the encode.py and decode.py
classes.  Creates the json file those two classes use to covert
to and from base64.  This file also handles the hashing
of the Base64 encoded Strings.

file_name: assignment4_b64.py

Must have the encode.py and decode.py classes for this to function.
The json file holding the base64 dict will be generated.

Nov 07 2019

"""
import base64
from encode import Encode
from decode import Decode
import json
import hashlib



en = Encode("")
de = Decode("")
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



def menu_loop():

  print("\n1. Encode a String")
  print("2. Decode a String")
  print("## Below Options will Hash then Encode String ##")
  print("3. Hash a String with SHA1")
  print("4. Hash a String with MD5")
  print("0. Exit")
  user_selection = raw_input("What would you like to do? ")
  return user_selection



def encode_string():
  user_string = raw_input("\nEnter a String to Encode: ")
  en.encode(user_string)
  print("\nOriginal String -> " + user_string)
  print("Encoded String -> " + en.encoded_string)
  print("Lib Encode -> "+ base64.b64encode(user_string))



def decode_string(s = ""):
  de.decode(s)
  print("\n\n\n\n\n##### Decoded -> " + de.decoded_string + "\n")



def select_encoded_string(to_hash = False, hash_type = "MD5"):
  user_input = ""

  en.print_encoded_strings()

  if to_hash:
    user_input = raw_input("Which String would you like to Hash(Use Index Number)? ")
  else:
    user_input = raw_input("Which String would you like to Decode(Use Index Number)? ")
  
  if int(user_input) >= 0 and int(user_input) < len(en.encoded_strings):
    if to_hash:
      hash_strings(hash_type, en.encoded_strings[int(user_input)])
    else:
      decode_string(en.encoded_strings[int(user_input)])

  else:
    print("Invalid Input!")


def hash_strings(hash_type, s = ""):
  temp_string = ""
  hsha1 = hashlib.sha1()
  hmd5 = hashlib.md5()

  if hash_type == "SHA1":
    hsha1.update(s)
    en.hash_strings.append(hsha1.hexdigest())
    temp_string = str(hsha1.hexdigest())
  else:
    hmd5.update(s)
    en.hash_strings.append(hmd5.hexdigest()) 
    temp_string = str(hmd5.hexdigest())

  en.encode(temp_string)

    

def main():

  while True:
    user_selection = menu_loop()


    if(user_selection == "1"):
      encode_string()


    if(user_selection == "2") and len(en.encoded_strings) > 0:
      user_input = raw_input("\nWould you like to Decode a String from your List(y/n)? ")
      if(user_input.lower() == "y"):
        select_encoded_string()
      else:
        user_input = raw_input("\nEnter a String to Decode(Must be Base64): ")
        decode_string(user_input)


    elif(user_selection == "2"):
      user_input = raw_input("\nEnter a String to Decode(Must be Base64): ")
      decode_string(user_input)


    elif(user_selection == "3"):
      if len(en.encoded_strings) > 0:
        user_input = raw_input("\nHash a String from your encoded List(y/n)? ")

        if(user_input.lower() == "y"):
          select_encoded_string(True, "SHA1")
        else:
          user_input = raw_input("Enter your Password: ")
          hash_strings("SHA1", user_input)

      else:
        user_input = raw_input("Enter your Password: ")
        hash_strings("SHA1", user_input)


    elif(user_selection == "4"):
      if len(en.encoded_strings) > 0:
        user_input = raw_input("\nHash a String from your encoded List(y/n)? ")

        if(user_input.lower() == "y"):
          select_encoded_string(True, "MD5")
        else:
          user_input = raw_input("Enter your Password: ")
          hash_strings("MD5", user_input)

      else:
        user_input = raw_input("Enter your Password: ")
        hash_strings("MD5", user_input)


    if(user_selection == "0"):
      break

    print("\n\n\n\n\n#### Encoded Strings ####")
    en.print_encoded_strings()
    print("\n#### Hashed Strings ####")
    en.print_hashed_strings()
  


if __name__ == "__main__":
  main()
