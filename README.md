# Simple_Query_Processor
This is a program that replicates some of the functionality of SQL Servers. It works under the assumptions that we will only be doing Selections based on one condition, Joining on only one condition. 

It is also assumed that it has already been optimized and works on conditions like:

Selection EMPLOYEE DNO = 5 EMPS_DNO5 

Where the table selected values are being stored is named at the end.

CSV files were used as to eliminate any SQL calls to a server that would return the end result without any of the intermediate steps being shown. 
