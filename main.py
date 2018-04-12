#!/usr/bin/env python3
#-*- coding:utf-8 -*-


import requests
import re

GFWLIST_CONTENT_URL = 'https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt'
KEY_STR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
SAVE_PATH = '/Users/yangruihan/.ShadowsocksX-NG/user-rule.txt'

def decode64(input_str):
    """
    解析GFWList算法
    """
    input_str = re.sub(r'[^A-Za-z0-9\+\/\=]', "", input_str)
    i = 0
    output_str = ''
    while i < len(input_str):
        enc1 = KEY_STR.index(input_str[i])
        i += 1
        enc2 = KEY_STR.index(input_str[i])
        i += 1
        enc3 = KEY_STR.index(input_str[i])
        i += 1
        enc4 = KEY_STR.index(input_str[i])
        i += 1

        chr1 = (enc1 << 2) | (enc2 >> 4)
        chr2 = ((enc2 & 15) << 4) | (enc3 >> 2)
        chr3 = ((enc3 & 3) << 6) | enc4

        output_str += chr(chr1)

        if enc3 != 64:
            output_str += chr(chr2)

        if enc4 != 64:
            output_str += chr(chr3)

    return output_str

if __name__ == '__main__':
    raw_content = requests.get(GFWLIST_CONTENT_URL).text

    print("raw text get success!")

    temp_str = decode64(raw_content)

    with open(SAVE_PATH, 'w') as file:
        file.write(temp_str)

    print("Finish!")
