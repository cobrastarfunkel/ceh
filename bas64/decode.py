"""
@author: Ian Cobia

Decode a string from Base64 back to it's orignal state.
First it takes the Base64 chars and converts them to their
respective numbers using the Base64 dict stored in
the .json file that is created by the main python file or stored in
this directory if it's already been run. Then it turns those into
binary numbers, pads the left so they're all six bits, combines that
into a long binary string, splits the string into 8 bits,
converts the 8 bits into decimal numbers, and finally converts those
to ascii chars corresponding to the decimal numbers.

file_name: decode.py

Nov 07 2019

"""
import json


class Decode:
  decoded_string = ""
  base64_dict = {}



  def decode(self, string_to_decode):
    """
    Open the base_64 json file and assign it
    to a dict then start the decoding process.
    """
    with open("b64_table.json", "r") as f:
      self.base64_dict = json.load(f)

    self.b64_to_decimal(string_to_decode)



  def b64_to_decimal(self, chars):
    """
    Change the base64 chars to their corresponding
    decimal numbers using the bas64 dict
    """
    string_b64 = []

    for char in chars:
      for key, value in self.base64_dict.items():
        if value == char:
          string_b64.append(int(key))
    self.decimal_to_binary(string_b64)



  def decimal_to_binary(self, dec_nums = []):
    """
    Convert the decimal numbers to binary and remove the 0b
    assigned by python.
    """
    binary_nums = ""
    binary_list = []
    temp_num = 0

    for num in dec_nums:
      temp_num = bin(num)[2:]
      binary_list.append(temp_num)
    
    self.binary_to_eight_bits(binary_list)



  def binary_to_eight_bits(self, bin_dec_list = []):
    """
    Pad the left with 0's if the number is not a 6  bit number,
    then combine all the 6 bit binary numbers into one string,
    finally split the string into 8 bit binary numbers.
    """
    six_bit_list = []
    temp_string = ""
    eight_bit_list = []

    for num in bin_dec_list:
      if (len(num) < 6):
        six_bit_list.append(num.rjust(6, "0")) 
      else:
        six_bit_list.append(num)
    for item in six_bit_list:
      temp_string+=item
      
    for char in range(0, len(temp_string), 8):
      eight_bit_list.append(temp_string[char:char+8])
    self.eight_bits_to_decimal(eight_bit_list)



  def eight_bits_to_decimal(self, binary_list = []):
    """
    Convert the eight bit binary umbers to decimal
    """
    dec_nums = []

    for num in binary_list:
      dec_nums.append(int(num, base=2))

    self.decimal_to_ascii(dec_nums)



  def decimal_to_ascii(self, dec_list = []):
    """
    Convert the decimal numbers to ascii
    """
    ascii_string = ""

    for num in dec_list:
      ascii_string+=chr(num)

    # The decoded String
    self.decoded_string = ascii_string










