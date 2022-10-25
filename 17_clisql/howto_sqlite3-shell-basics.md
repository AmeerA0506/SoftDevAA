### Foo Bar:: Ameer Alnasser, Wan Ying Li, Kevin Wang
### SoftDev
### k17 -- Skillet Intro
### 2022-10-24
### time spent: .5 hrs

## What to do
* Remember to add a semi colon at the end of each line
    - If not, don't sweat. the line should appear as --->. You can add a semi colon and it would work as intended. Without a semicolon, a line can be infinitely long, as signified by the --->.
* Follow our basic commands TO A TEE!!!

## What not to do
* Forget ur semicolon lulz

## Basic commands
* ```$ sqlite3 <name>```
or  
```$ sqlite3  
<sqlite3> .OPEN <name>
```
    - <name> could be anything, creates file with <name> (no file extension)
    - Should add <sqlite> before the input bar
* ```CREATE table <tablename>(<col_name1> <param1>, <col_name2> <param2>....<col_name n> <param n>);```
    - Note: from all known documentation, no further columns can be appended
    - possible parameters: TEXT (put in quotes, either single or double), INTEGER, BLOB (any data type), REAL (float)
* ``` insert into <tablename> VALUES(<Val1>, <Val2>....<ValN>);```
    - should insert a value into table if the parameters are true
* ```select * from <tablename>;```
    - returns the content of table.
    - asterisk means all columns, could be replaced with a singular column name or multiple separated by commas

## Fun things we learned
* A file is created with the name provided in the first line of our Basic Commands
* A Sqlite file can have multiple tables (as it is an RDB)
* .mode <format> can help format the output of reading the file.
  - these formats could be quote, line, list, box, table, etc.
* We relearned how to ssh into the CSLab
* Commands are NOT CASE SENSITIVE!!
* spam ctrl-C to terminate session

## QCC:
* what file is created after opening a session? we noticed that if we cat the file, it has undecodable chars
