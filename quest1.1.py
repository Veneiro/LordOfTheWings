import math
import sys

def main():
    print("----------------------------------")
    print("--------------START---------------")
    print("----------------------------------")
    read_file("inputexample.txt")
    
def read_file(input_file):
    with open(input_file) as f:
        sum = 0
        for i in f.read().split(','):
            i1 = int(i)
            i2 = int(i)-2
            print("Side: %d - %d" % (i1, i2))
            s = math.sqrt(float(i1))
            s2 = math.sqrt(float(i1)-2)
            print("%f - %f" % (s, s2))
            term = s/int(s)
            print("----------------------------------")
            if(term != 1):
                while(math.ceil(s) - 2 <= 0):
                    s += 1
                print("Number %s is not a square" % i)
                print("Closest square above: %d | Its number of cells: %d" % (math.ceil(s), pow(math.ceil(s), 2)))
                sum += (pow(math.ceil(s), 2) - i1 - i2)
                print("Current sum: %d" % sum)
                '''
                clos_square = pow(clos_square_side, 2)
                i_square = clos_square - 2
                print("Can be? %d - 2 = %d > 0?" % (clos_square_side, i_square))
                print("----------------------------------")
                print("Number %s is not a square" % i)
                print("Closest square above: %d | Its number of cells: %d" 
                      % (clos_square, pow(clos_square, 2)))
                new_square = i_square + 1
                print("Closest square not valid so new is %d" % new_square)
                aux = (pow(clos_square, 2) - int(i)) - pow(new_square - 2, 2)
                print("Aux is %d" % aux)
                sum += aux
                print("Current sum: %d" % sum)
                '''
        f.close()
    
    print("TOTAL SUM: %d" % sum)
main()