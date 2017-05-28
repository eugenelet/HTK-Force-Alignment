import sys
import os
from HTK import HCopy

print(sys.version)

mfc_train_filename = "mfc_train.scp"
mfc_test_filename = "mfc_test.scp"
mfc_train_file = open(mfc_train_filename, "w")
mfc_test_file = open(mfc_test_filename, "w")

train_filename = "train.scp"
test_filename = "test.scp"
train_file = open(train_filename, "w")
test_file = open(test_filename, "w")

# here we use HTK to calculate the same thing
for filename in os.listdir('data/train_8k/'):
    HCopy('wav_config', 'data/train_8k_noise/' + filename, 'mfc/train/' + os.path.splitext(filename)[0] + '.mfc')
    mfc_train_file.write("./data/train_8k_noise/" + filename + " ./mfc/train/" + os.path.splitext(filename)[0] + ".mfc\n")
    train_file.write("./mfc/train/" + os.path.splitext(filename)[0] + ".mfc\n")

for filename in os.listdir('data/test_8k/'):
    HCopy('wav_config', 'data/test_8k_noise/' + filename, 'mfc/test/' + os.path.splitext(filename)[0] + '.mfc')
    mfc_test_file.write("./data/test_8k_noise/" + filename + " ./mfc/test/" + os.path.splitext(filename)[0] + ".mfc\n")
    test_file.write("./mfc/test/" + os.path.splitext(filename)[0] + ".mfc\n")
