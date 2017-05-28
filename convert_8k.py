import os
import subprocess
import sys

print(sys.version)

train_in_fname = "train_in.list"
train_out_fname = "train_out.list"
train_in_file = open(train_in_fname, "w")
train_out_file = open(train_out_fname, "w")

test_in_fname = "test_in.list"
test_out_fname = "test_out.list"
test_in_file = open(test_in_fname, "w")
test_out_file = open(test_out_fname, "w")
# Convert training data to 8kHz
for filename in os.listdir('data/train/'):
    try:
        output = subprocess.check_output(["sox", "-r", "16000", "-b", "16", "-c", "1", "-e", "signed-integer", "-t", "raw",
                                         'data/train/' + filename, "-r", "8000", "-t", "raw", 'data/train_8k/' + filename])
        train_in_file.write('data/train_8k/' + filename + '\n')
        train_out_file.write('data/train_8k_noise/' + filename + '\n')
    except subprocess.CalledProcessError as e:
            print ('EXC {}'.format(e))

# Convert testing data to 8kHz
for filename in os.listdir('data/test/'):
    try:
        output = subprocess.check_output(["sox", "-r", "16000", "-b", "16", "-c", "1", "-e", "signed-integer", "-t", "raw",
                                         'data/test/' + filename, "-r", "8000", "-t", "raw", 'data/test_8k/' + filename])
        test_in_file.write('data/test_8k/' + filename + '\n')
        test_out_file.write('data/test_8k_noise/' + filename + '\n')

    except subprocess.CalledProcessError as e:
            print ('EXC {}'.format(e))
os.system("pwd")
os.system("/home/gene/Documents/NCTU/Year4Sem2/Speech_Processing/HW5/tools/fant/filter_add_noise -i train_in.list -o train_out.list -n /home/gene/Documents/NCTU/Year4Sem2/Speech_Processing/HW5/tools/fant/example/subway.raw -f g712 -s 20")
os.system("/home/gene/Documents/NCTU/Year4Sem2/Speech_Processing/HW5/tools/fant/filter_add_noise -i test_in.list -o test_out.list -n /home/gene/Documents/NCTU/Year4Sem2/Speech_Processing/HW5/tools/fant/example/subway.raw -f g712 -s 20")
