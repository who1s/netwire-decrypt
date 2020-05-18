#!/usr/bin/env python3
#
# MIT License
# 
# Copyright (c) 2020 Juho Jauhiainen
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description="Python script that parses NetWire keylogger logs. NetWire logs are typically in C:\\Users\\[username]\\AppData\\Roaming\\Logs directory. Script by whois (Twitter: @JuhoJauhiainen)")
    parser.add_argument("-o", "--output", dest="filename", help="Output file (default stdout)", metavar="OUTPUT")
    parser.add_argument("logfile", help="NetWire keylogger log file", metavar="INPUT")
    args = parser.parse_args()
    if args.logfile:
        print("[!] Reading logs from {}".format(args.logfile))
    if args.filename:
        print("[i] Writing output to file {}".format(args.filename))
    return args

def decrypt_character(byte):
    result = chr(int(hex((int(byte.hex(),16) - 0x24^0x9D)&0xFF), 16))
    return result

def main():
    args=get_arguments()
    decrypted_log=[]
    with open(args.logfile, 'rb') as f:
        byte = f.read(1)
        while byte != b"":
            try:
                decrypted_log.append(decrypt_character(byte))
            except:
                pass
            byte=f.read(1)
    if args.filename:
        with open(args.filename, 'w') as foo:
            foo.write("".join(decrypted_log))
    else:
        print("".join(decrypted_log))
    print("[!] {} EOF".format(args.logfile))

if __name__ == "__main__":
    main()

