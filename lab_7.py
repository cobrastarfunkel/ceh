#!/usr/bin/python
import urllib2
import string
import re
import socket

'''
regex to match the following
(www.)? Match 0 or 1 of the pattern www.
[a-zA-Z]{1,100} match 1-100 of any letter
\. match a . after above letters
[a-zA-Z0-9]{1,100} match 1-100 of any letter or number
\. match a period after above numbers and letters
.* match 0 or more of any character
'''
url_regex = r'((www\.)?[a-zA-Z]{2,100}\.[a-zA-Z0-9]{1,100}\..*)'



'''
Take in a list, compare it to the url_regex and
return a split string. It only ended up being used once
'''
def list_to_string(s, use_regex=True, delimiter=','):
  ret_string = ""
  s = str(s)

  for element in s.split(delimiter):
    if use_regex:
      if re.findall(url_regex, element):
        ret_string += element + '\n'
    else:
        ret_string += element + '\n'

  return ret_string



lab71 = ""
for line in urllib2.urlopen("http://www.cisco.com"):
  if 'href' in line:
     lab71 = lab71 + line


# First regex pass
lab71 = str(re.findall(url_regex ,lab71))
lab71 = list_to_string(lab71)

with open("lab7-1.txt", 'w') as f:
  f.write(lab71)


# String wasn't working, there were a few duplicates
lab72 = []

#Split on spaces, URL's don't have spaces
for line in lab71.split():

  # Split on double quotes, No quotes in URL's
  for split_l in line.split('"'):

    # Split on \
    for split_2 in split_l.split('\''):

    # I assume the .css aren't url's, I could be wrong
      if re.findall(url_regex, split_2) and '.css' not in split_2:
       lab72.append(split_2)
# Convert to set to remove duplicate entries
set_list = list(set(lab72))
set_list.sort()

# Convert back to String to write to file
lab72 = list_to_string(set_list)
lab72_2 = ""

# Loop through String and split on ' to clean up random stuff
'''
Match regex one more time to clean up a duplicate and get rid of '] from list
The second regex takes care of any direcotries that slipped in.  There shouldn't be
a URL that starts with a single slash
(^/){1} Means match a single / one time at the start of the line
.+ Means match anything one or more times
The third is for a jpg that was floating around in there.
'''
for item in lab72.split('\''):

  if re.findall(url_regex, item) and not (re.findall(r'(^/){1}.+', item) or re.findall(r'^.+\.jpg$', item)): 
    lab72_2 += item + '\n'

with open("lab7-2.txt", 'w') as f:
  f.write(lab72_2)

print(lab72_2)


# Try to Resolve IP's
#for line in lab72_2.split('\n'):
#  print(line)
#  try:
#    socket.gethostbyname(line)
#  except Exception as invalid_host:
#    print("Invalid HOST")
#  else:
#    print(socket.gethostbyname(line))


