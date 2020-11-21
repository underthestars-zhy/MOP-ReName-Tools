#! /usr/local/bin/python3

import argparse
import shelve
import os
import sys
import re
import shutil
import json

# 多语言设置
file_lists = os.listdir(os.path.expanduser('~'))
if 'mop.json' in file_lists:
    file = open(os.path.expanduser('~/mop.json'), 'r')
    mop_db_path = json.load(file)
    file.close()
    mop_db = shelve.open(mop_db_path + 'mop')
    if mop_db['language'] == 'en':
        rename_help = 'Input source folder and converted file(Starting number optional)'
        r_num_1 = 'Putting the folder'
        r_num_2 = 'Rename and save to'
        r_num_dir_exists = 'Checking to see if the folder exists'
        r_num_error_1 = 'he conversion folder could not be obtained'
        r_num_dir_make = 'Successful creation of accept transformation folder'
        r_num_txt = '  to  '
    elif mop_db['language'] == 'cn':
        rename_help = '输入源文件夹和转换后的文件夹(开始数字可选)'
        r_num_1 = '正在把文件夹'
        r_num_2 = '重命名并储存到'
        r_num_dir_exists = '正在检查文件夹是否存在'
        r_num_error_1 = '无法获得转换文件夹'
        r_num_dir_make = '创建接受转换文件夹成功'
        r_num_txt = '  到  '
    mop_db.close()
else:
    print('Error|出错')
    sys.exit()

# 命令参数设置
parser = argparse.ArgumentParser(description='ReNameTool-MacOS-11')

parser.add_argument('-r_num', type=str, help=rename_help, nargs='+')

args = parser.parse_args()

# 名字转换
if args.r_num and len(args.r_num) >= 2:
    print(r_num_1+args.r_num[0]+r_num_2+args.r_num[1])
    from_dir = os.path.abspath(args.r_num[0])
    to_dir = os.path.abspath(args.r_num[1])
    if not os.path.exists(from_dir):
        print(r_num_error_1)
        sys.exit()
    if not os.path.exists(to_dir):
        os.makedirs(to_dir)
        print(r_num_dir_make)
    try:
        i = args.r_num[2]
    except:
        i = 0
    file_lists = os.listdir(from_dir)
    find_re = re.compile(r'(.*)\.(.*)')
    for file in file_lists:
        if file == '.DS_Store':
            continue
        file_re = find_re.search(file)
        file_name, file_suffix = file_re.groups()
        new_file = str(i) + "." + file_suffix
        shutil.move(from_dir + "/" + file, to_dir + "/" + new_file)
        print(from_dir + file + r_num_txt + to_dir + new_file)
        i += 1
    print('OK')
