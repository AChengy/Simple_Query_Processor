import csv

#a function that splits the lines then sends them to the proper functions
def parse(line):
    parsedline = line.split()
    if parsedline[0] == 'Join':
        join(parsedline[1:])
    elif parsedline[0] == 'Selection':
        selection(parsedline[1:])
    elif parsedline[0] == 'Projection':
        projection(parsedline[1:])

def join(commands):
    #pick the CSV file/Table to open
    lefttable = commands[0]+'.csv'
    righttable = commands[1]+'.csv'
    #find what to call the next intermediate table
    newtable = commands[len(commands)-1]+'.csv'

    #find the join condition
    for i, command in enumerate(commands):
        if command == '=':
            leftcondition = commands[i-1]
            rightcondition = commands[i+1]

    #open the table writing to
    w = open(newtable, 'wb')
    writer = csv.writer(w)

    #find the right tables titles for the CSV and find what colum the condition is in
    with open(righttable, 'rb') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                righttitles = row;
                for j, title in enumerate(row):
                    if title == rightcondition:
                        rightconditionloc = j;

    with open(lefttable, 'rb') as f1:
        reader1 = csv.reader(f1)
        for i1, row in enumerate(reader1):
            if i1 == 0:
                for j, title in enumerate(row):
                    if title == leftcondition:
                        leftconditionloc = j
                writer.writerow(row+righttitles)
            else:
                with open(righttable, 'rb') as f:
                    reader = csv.reader(f)
                    for rightrow in reader:
                        if row[leftconditionloc] == rightrow[rightconditionloc]:
                            writer.writerow(row+rightrow)

    w.close()



def selection(commands):
    #pick the CSV file /Table to open
    table = commands[0]+'.csv'
    #find what to call the intermediate table
    newtable = commands[len(commands)-1]+'.csv'

    for i, command in enumerate(commands):
        if command == '=':
            leftcondition = commands[i-1]
            rightcondition = commands[i+1]

    #open the table writing to
    w = open(newtable, 'wb')
    writer = csv.writer(w)

    #find what column the left value is and read those
    with open(table,'rb' ) as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                for j, title in enumerate(row):
                    if title == leftcondition:
                        titleLoc = j
                writer.writerow(row)
            else:
                if row[titleLoc] == rightcondition:
                    writer.writerow(row)
    w.close()



def projection(commands):
    #table we are projecting from
    table = commands[0]+'.csv'

    #table we are projecting to
    projectedtable = commands[len(commands)-1]+'.csv'

    projectedtitles = commands[1:-1]
    projectedtitles = map(lambda x: filter(lambda y: y != ',', x),projectedtitles)

    w = open(projectedtable, 'wb')
    writer = csv.writer(w)

    writer.writerow(projectedtitles)

    with open(table, 'rb') as f:
        reader = csv.reader(f)

        titlelocs = []
        for i, row in enumerate(reader):
            if i == 0:
                for j, title in enumerate(row):
                    if title in projectedtitles:
                        titlelocs.append(j)
            else:
                tuple = []
                for loc in titlelocs:
                    tuple.append(row[loc])
                writer.writerow(tuple)

    w.close()


f = open('Input.txt', 'r') #opens the text file for reading

#iterate through each line of the file and send it to parse
for line in f:
    parse(line)

#close the file
f.close()