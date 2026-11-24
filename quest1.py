import math
import sys

def main():
    print("Start")
    read_file("inputexample.txt")
    
def read_file(input_file):
    with open(input_file) as f:
        sum = 0
        for i in f.read().split(','):
            s = math.sqrt(float(i))
            term = s/int(s)
            if(term != 1):
                print("Number %s is not a square" % i)
                print("Closest square above: %d | Its number of cells: %d" % (math.ceil(s), pow(math.ceil(s), 2)))
                sum += (pow(math.ceil(s), 2) - int(i))
                print("Current sum: %d" % sum)
        f.close()
    
    print("TOTAL SUM: %d" % sum)
main()