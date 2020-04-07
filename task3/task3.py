import sys
import argparse as argp

def createParser ():
    parser = argp.ArgumentParser()
    parser.add_argument('--dir', required=True)
    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    fData1 = [float(line.rstrip('\n')) for line in open(namespace.dir + "/Cash1")]
    fData2 = [float(line.rstrip('\n')) for line in open(namespace.dir + "/Cash2")]
    fData3 = [float(line.rstrip('\n')) for line in open(namespace.dir + "/Cash3")]
    fData4 = [float(line.rstrip('\n')) for line in open(namespace.dir + "/Cash4")]
    fData5 = [float(line.rstrip('\n')) for line in open(namespace.dir + "/Cash5")]

    dataSum = []
    count = 0
    while (count < 16):
        dataSumTemp = fData1[count] + fData2[count] + fData3[count] + fData4[count] + fData5[count]
        dataSum.append(dataSumTemp)
        count += 1
    print(dataSum.index(max(dataSum)) + 1)