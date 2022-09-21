#string_times
def string_times(str, n):
  # Given a string and a non-negative int n, return a larger string that is n copies of the original string.
  return n * str

#front_times
def front_times(str, n):
  # Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
  if (len(str) < 3):
    return str * n
  else:
    return str[:3] * n

#string_bits
def string_bits(str):
  #Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".  
  res = ""
  for i in range(len(str)):
    if (i % 2 == 0):
      res += str[i]
  return res  

#String_splosion
def string_splosion(str):
  #Given a non-empty string like "Code" return a string like "CCoCodCode".
  output=""
  for x in range(len(str)):
    output += str[:x]
  return output + str


#Last2
def last2(str):
  #Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
  if(len(str)<2):
    return 0
  twochar=str[-2:]
  output=0
  for x in range(len(str)-2):
    if(twochar==str[x:x+2]):
      output+=1
  return output
    

#Array_count9
def array_count9(nums):
  #Given an array of ints, return the number of 9's in the array.
  output=0
  for x in range(len(nums)):
    if nums[x]==9:
      output+=1
      
  return output

#Array_front9
def array_front9(nums):
  # Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
  output=0
  for x in range(len(nums)):
    if(x<4):
      if nums[x]==9:
        return True
      
  return False

#array123
def array123(nums):
    #Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
 for i in range(len(nums)-2):
   if (nums[i:i+3] == [1, 2, 3]):
     return True
 return False

#String_match 
def string_match(a, b):
   # Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
  counter = 0
  for i in range(len(a)-1):
    if (a[i:i+2] == b[i:i+2]):
      counter += 1
  return counter



