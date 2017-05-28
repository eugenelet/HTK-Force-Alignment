import subprocess
import matplotlib.pyplot as plt
import numpy as np

correct_accu = []
accuracy_accu = []
for i in range(0, 400, 10):
    vite_str = "HVite -H hmm8/macros -H hmm8/hmmdefs -S test.scp -l '*' -i recout.mlf -w wdnet -p -" + str(i) + " -s 5.0 dict monophone1.lst"
    proc = subprocess.Popen(vite_str, shell=True, stdout=subprocess.PIPE)
    proc.wait()
    proc = subprocess.Popen('HResults -I test.mlf monophone1.lst recout.mlf', shell=True, stdout=subprocess.PIPE)
    proc.wait()
    output = proc.stdout.read()

    correct_str = output.split("WORD: %Corr=", 1)[1]
    correct_str = correct_str.split(", Acc", 1)[0]
    correct = float(correct_str)
    correct_accu.append(correct)

    acc_str = output.split("Acc=", 1)[1]
    acc_str = acc_str.split(" [H", 1)[0]
    accuracy = float(acc_str)
    accuracy_accu.append(accuracy)

x = np.arange(0, 400, 10)
plt.plot(x, correct_accu)
plt.plot(x, accuracy_accu, '--')
plt.legend(['Correct', 'Accuracy'], loc='upper right')
plt.show()
# print output
# print correct
# print accuracy