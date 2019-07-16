# -*- coding: utf-8 -*-
import binascii
import struct
import sys
import getopt


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "i:o:", ["h"])
    except getopt.GetoptError:
        print('GetoptError: python main.py -i <input_filename> -o <output_filename>')
        print('For example: python main.py -i 1.png -o 2.png')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h"):
            print('python main.py -i <input_filename> -o <output_filename>')
            print('For example: python main.py -i 1.png -o 2.png')
            sys.exit()
        elif opt in ("-i"):
            input = arg
        elif opt in ("-o"):
            output = arg

    change(input, output)


def change(input, output):
    m = open(input, "rb").read()
    crc32 = int(m[29:33].encode('hex'), 16)
    for i in range(0, 65535):
        height = struct.pack('>i', i)
        data = m[12:20] + height + m[24:29]
        res = binascii.crc32(data) & 0xffffffff
        if res == crc32:
            with open(output, "w") as f:
                f.writelines(m[0:20] + ''.join(map(lambda c: "%02X" % ord(c), height)).decode('hex') + m[24:-1])
                print "Congratulation!"
                break


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except UnboundLocalError:
        print('UnboundLocalError: python main.py -i <input_filename> -o <output_filename>')
        print('For example: python main.py -i 1.png -o 2.png')
        sys.exit(2)
