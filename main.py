import time
import sys


def main(argv):
    start_time = time.time()
    printRunTime(start_time)


def printRunTime(strat_time):
    with open('output\\runTime.txt', 'a') as file:
        file.write("Run time: " + str((time.time() - strat_time)) + " Seconds" + '\n')
    print("file output\\runTime.txt was updated")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)
