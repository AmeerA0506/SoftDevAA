#sleep_in
#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
def sleep_in(weekday, vacation):
  return weekday==False or vacation == True
print(sleep_in(False,True))
print(sleep_in(False,True))
print(sleep_in(True,False))
print(sleep_in(True,True))

#near_hundred
#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
def near_hundred(n):
  return 89<n and n<111 or 189<n and n<211
print(near_hundred(88))
print(near_hundred(90))
print(near_hundred(112))
print(near_hundred(190))

#monkey_trouble
#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
def monkey_trouble(a_smile, b_smile):
  return a_smile==b_smile
print(monkey_trouble(False,True))
print(monkey_trouble(False,True))
print(monkey_trouble(True,False))
print(monkey_trouble(True,True))

#sum_double
#Given two int values, return their sum. Unless the two values are the same, then return double their sum.
def sum_double(a, b):
  if(a==b):
    return 2*a + 2*b
  else:
    return a + b
print(sum_double(1, 2))# → 3
print(sum_double(3, 2)) #→ 5
print(sum_double(2, 2)) #→ 8

#parrot_troubles
#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
def parrot_trouble(talking, hour):
  return (hour < 7 or hour > 20) and (talking)
print(parrot_trouble(True, 6))# → True
print(parrot_trouble(True, 7)) #→ False
print(parrot_trouble(False, 6))# → False

#front3:
#Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
def front3(str):
  if (len(str) < 3):
    return str * 3
  return str[:3] * 3
print(front3('Java'))# → 'JavJavJav'
print(front3('Chocolate'))# → 'ChoChoCho'
print(front3('abc'))# → 'abcabcabc'



