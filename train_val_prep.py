import os.path
import sys
import random

if __name__ == '__main__':
    train = open("train.txt", "w")
    val = open("val.txt", "w")

    random.seed('1214')

    with open(test.txt) as f:
       files = (os.path.basename(filepath) for file in f.readlines())

    for i in sys.argv[1:]:
        with open('test.txt') as f:
            if os.path.basename(1) in files:
                pass
            else:
                i = os.path.abspath(i)
                monRand = random.random()
                if monRand <= 0.1:
                    val.write(i+"\n")
                else:
                    train.write(i+"\n")

    val.close()
    train.close()
    print("Dataset created")
