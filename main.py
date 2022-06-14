# @Author: Southseast
# @Date: 2022-06-14 18:28
import argparse
import binascii
import os
import struct


class Steg():

    def __init__(self, source_path, target_path):
        self.suffix = ".png"
        self.source_path = source_path
        self.target_path = target_path

    def check_png(self, path):
        if path.endswith(self.suffix):
            return True
        else:
            return False

    def find_all_file(self):
        for root_name, middle_name_list, file_name_list in os.walk(self.source_path):
            for file_name in file_name_list:
                fullname = os.path.join(root_name, file_name)
                yield fullname

    def traverse(self):
        if self.check_png(self.source_path):
            target_file = os.path.basename(self.source_path)
            self.recovery(self.source_path, self.target_path + target_file)
        for i in self.find_all_file():
            target_path = i.replace(self.source_path, self.target_path)
            target_dir = os.path.dirname(target_path)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            if self.check_png(i):
                self.recovery(i, target_path)

    def recovery(self, source_path, target_path):
        m = open(source_path, "rb").read()
        crc32 = int(m[29:33].hex(), 16)
        for i in range(0, 65535):
            height = struct.pack('>i', i)
            data = m[12:20] + height + m[24:29]
            res = binascii.crc32(data) & 0xffffffff
            if res == crc32:
                with open(target_path, "wb") as f:
                    f.write(m[0:20] + height + m[24:-1])
                    print("success in %s" % target_path)
                    break


if __name__ == '__main__':
    prefix_path = os.getcwd() + "/"
    parser = argparse.ArgumentParser(description='PNG_Height_Steganography')
    parser.add_argument('--source_path', '-s', help='图片输入路径，默认为source文件夹', default=prefix_path + "source/")
    parser.add_argument('--target_path', '-t', help='图片输出路径，默认为target文件夹', default=prefix_path + "target/")
    args = parser.parse_args()
    steg = Steg(args.source_path, args.target_path)
    steg.traverse()
