'''
Charles's Angels::Aleksandra Shifrina, Nakib Abedin, Ameer Alnasser
SoftDev pd08
K04 -- RNG + Dictionaries
2022-09-22
time spent: 0.5hrs
DISCO:
    *figured out that .keys() returns all keys of a dictionary  
    *figured out typecasting. ex: int(4.0)
    *figured out general solution for returning a random devo 
QCC:
    *will the final dictionary work with our code?
    *how do we ensure that the code will completely randomly chose a devo?
OPS Summary:
    1. gather all keys from dictionary in a list, keys
    2. pick a random index using length of list
    3. retrieve key from list
    4. generate a random element from list associated with key
    5. return random devo
'''

import random as rng

#krewes = {1:['A', 'B', 'C'], 2:['D', 'E', 'F']}

krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
         }


def find_devo(krewes):
    keys = list(krewes)
    index = rng.randint(0, len(keys)-1)
    key = keys[index]
    rando_value = rng.randint(0, len(krewes[key])-1)
    return krewes[key][rando_value]