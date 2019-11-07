"""
@author: Ian Cobia

Encode a string into Base64 by converting the
characters to their ascii numbers, then
convert those numbers into 8 bit binary padding 0's
to the left as needed, combine that into one string,
split it into 6 bits, convert that to decimal, and
finaly compare that to a dict of the Base64 table.


file_name: encode.py

Nov 07 2019

"""
import json


class Encode:
  encoded_strings = []
  encoded_string = ""
  base64_dict = {}
  hash_strings = []
  

  def __init__(self, string_to_encode):
    self.string_to_encode = string_to_encode



  def encode(self, string_to_encode):
    """
    Starts the encoding process
    """
    with open("b64_table.json", "r") as f:
      self.base64_dict = json.load(f)

    self.char_to_acsii(string_to_encode) 



  def char_to_acsii(self, chars = ""):
    """
    Convert chars to ascii number
    """
    string_ascii = []

    for char in chars:
      string_ascii.append(ord(char))

    self.ascii_to_binary(string_ascii)



  def ascii_to_binary(self, nums = []):
    """
    Convert ascii numbers into 8 bit binary
    """
    ascii_binary = [] 
    binary_correct_nums = []

    for num in nums:
      ascii_binary.append(str(bin(num)[2:]))

    # Because bin() doesn't make it 8 bits if it's not an 8 bit number
    for bin_num in ascii_binary:    
      if len(bin_num) < 8:
        binary_correct_nums.append(bin_num.rjust(8, '0'))
      else:
        binary_correct_nums.append(bin_num)

    self.split_binary_nums(binary_correct_nums)



  def split_binary_nums(self, binary_string = []):
    """
    Calls the eight_bit_to_six function which yields
    6 bit chunks of the combined binary string and returns
    a list of them seperated.  Padding has not been
    added at this step.
    """
    temp_string = ""
    temp_list = []

    for item in binary_string:
      temp_string+=item

    for six_bits in self.eight_bit_to_six(temp_string):
      temp_list.append(six_bits)

    self.six_bit_to_decimal(temp_list)



  def six_bit_to_decimal(self, six_bit_list = []):
    """
    Convert the 6 bit binary numbers to Decimal
    so they can be converted to B64
    """
    temp_list = []

    for item in six_bit_list:
      if len(item) == 6:
        temp_list.append(int(item, base=2))
      else:
        length_signs = (6 - len(item))
        temp_var = item.ljust(6, '0')
        temp_list.append(int(temp_var, base=2))

        for i in range(length_signs/2):
          temp_list.append("=")
        
    self.decimal_to_B64(temp_list)



  def eight_bit_to_six(self, num_string = ""):
    """
    Split the string of combined binary into 6 bit chunks
    """
    if len(num_string) > 6:
      for char in range(0, len(num_string), 6):
        yield num_string[char:char+6]



  def decimal_to_B64(self, decimal_list = []):
    """
    Convert decimal to B64
    """
    return_string = ""

    for item in decimal_list:
      if item != "=":
        return_string+=(self.base64_dict.get(str(item)))
      else:
        return_string+=item

    # Encoded String
    self.encoded_string = return_string
    self.encoded_strings.append(return_string)



  def print_encoded_strings(self):
    count = 0
    for item in self.encoded_strings:
      print(str(count) + ":" + item)
      count+=1



  def print_hashed_strings(self):
    for item in self.hash_strings:
      print(item)
