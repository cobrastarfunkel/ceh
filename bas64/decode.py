import json


class Decode:
  decoded_string = ""
  base64_dict = {}



  def __init__(self, string_to_decode):
    self.string_to_decode = string_to_decode



  def decode(self, string_to_decode):
    with open("b64_table.json", "r") as f:
      self.base64_dict = json.load(f)

    self.b64_to_decimal(string_to_decode)



  def b64_to_decimal(self, chars):
    string_b64 = []

    for char in chars:
      for key, value in self.base64_dict.items():
        if value == char:
          string_b64.append(int(key))
    self.decimal_to_binary(string_b64)



  def decimal_to_binary(self, dec_nums = []):
    binary_nums = ""
    binary_list = []
    temp_num = 0

    for num in dec_nums:
      temp_num = bin(num)[2:]
      binary_list.append(temp_num)
    
    self.binary_to_eight_bits(binary_list)



  def binary_to_eight_bits(self, bin_dec_list = []):
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
    dec_nums = []

    for num in binary_list:
      dec_nums.append(int(num, base=2))

    self.decimal_to_ascii(dec_nums)

  def decimal_to_ascii(self, dec_list = []):
    ascii_string = ""

    for num in dec_list:
      ascii_string+=chr(num)

    self.decoded_string = ascii_string










