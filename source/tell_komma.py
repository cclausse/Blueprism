import os

match = '","'
erase_num = 4
cnt = 0
errorcount=0
os.chdir('C:\\Users\\Carsten Claussen\\Documents\\GitHub\\blueprism\source')
cvs_file = os.path.join("..\\data\\Workitems_smn.csv")
#
with open('..\\data\\Workitems_smn.csv', 'r') as rf:
    for line in rf:
        cnt += 1
        numComma = line.count(match)
        if numComma != 10:
            errorcount+=1
            print("Antall komma i linje " + str(cnt) + " = "  + str(numComma))
            break
    print("Antall feil: " + str(errorcount) )



