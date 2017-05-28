# we set up the path to the lib here
# you can skip this if you store the files in your project
import sys
import os

print(sys.version)

num_string = {}
num_string['0'] = 'ling'
num_string['1'] = 'yi'
num_string['2'] = 'er'
num_string['3'] = 'san'
num_string['4'] = 'si'
num_string['5'] = 'wu'
num_string['6'] = 'liu'
num_string['7'] = 'qi'
num_string['8'] = 'ba'
num_string['9'] = 'jiu'

label_fname = "data.mlf"
label_file = open(label_fname, "w")
label_file.write("#!MLF!#\n")
# here we use HTK to calculate the same thing
for filename in os.listdir('data/TAB/'):
    if filename[5] == '0':
        continue
    data_label_file = open('data/TAB/' + filename, 'r')
    lines = data_label_file.readlines()[1:]
    for x in lines:
        if len(x.split()[0]) == 1:
            label_file.write('\"*/' + os.path.splitext(filename)[0] + '0' + x.split()[0] + '.lab\"\n')
        else:
            label_file.write('\"*/' + os.path.splitext(filename)[0] + x.split()[0] + '.lab\"\n')
        for c in x.split()[3]:
            label_file.write(num_string[c] + '\n')
        label_file.write('.\n')

label_fname = "test.mlf"
label_file = open(label_fname, "w")
label_file.write("#!MLF!#\n")
for filename in os.listdir('data/TAB/'):
    if filename[5] != '0':
        continue
    data_label_file = open('data/TAB/' + filename, 'r')
    lines = data_label_file.readlines()[1:]
    for x in lines:
        if len(x.split()[0]) == 1:
            label_file.write('\"*/' + os.path.splitext(filename)[0] + '0' + x.split()[0] + '.lab\"\n')
        else:
            label_file.write('\"*/' + os.path.splitext(filename)[0] + x.split()[0] + '.lab\"\n')
        for c in x.split()[3]:
            label_file.write(num_string[c] + '\n')
        label_file.write('.\n')


def debug():
    if x.split()[2] != '0' and x.split()[2] != '1' and x.split()[2] != '2' and x.split()[2] != '3' and \
    x.split()[2] != '4' and x.split()[2] != '5' and x.split()[2] != '6' and x.split()[2] != '7' and \
    x.split()[2] != '8' and x.split()[2] != '9' and x.split()[2] != '10' and x.split()[2] != '11':
        print x.split()[2]
