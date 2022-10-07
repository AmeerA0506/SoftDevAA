'''
Young Lions Crying At War :: Ameer Alnasser, Yat Long Chan, Wilson Mach
SoftDev pd08
K07 -- Web dev *
2022-10-4
time spent: 0.5hrs
'''
import csv
import random as rng
from flask import Flask
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?
@app.route("/") # Q1: What points of reference do you have for meaning of '/'?

def occupation():
    file1 = open("occupations.csv",'r')
    file1.readline() #we dont like the first line, it hates us 
    sha= file1.readlines()
    sha = sha[:-1] # we want to remove the last entry, which is the total 
    dictionary = {}
    output=""
    for e in sha:
        if e[0] == '"':
            dictionary[e[1:e.find('",')]] = float(e[e.find('",')+2:len(e)-1]) # if theres a comma in the key, we want to acknowledge it as a dif situation 
        else:
            dictionary[e[0:e.find(',')]] = float(e[e.find(',')+1:len(e)-1]) 
    dic = dictionary

    occlist = []
    for key in dic:
        number = int((dic[key])*10)
        for x in range(number):
            occlist.append(key) # we wanted to find a way to make it random
    index = rng.randint(0, len(occlist)-1)
    
    
    for x in dic:
        output+= x + "<br>"
    return "<h2> Young Lions Crying At War:: Ameer Alnasser, Yat Long Chan, Wilson Mach</h2>"\
           +"Your randomly selected occupation is " + occlist[index] \
+ " with a " + str(dic[occlist[index]]) + "% chance." + "<br>"+"<br>"\
+"<h1> Occupations </h1>" + output
        
app.debug = True        # enable auto-reload upon code change, auto reloading the terminal and not the webpage

app.run()  # Q5: Where have you seen similar constructs in other languages?

