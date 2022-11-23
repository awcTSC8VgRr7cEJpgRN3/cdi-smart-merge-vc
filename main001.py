#!/usr/bin/env python

from os import listdir
from os.path import isfile, join, splitext
from sys import argv
# import csv
from shutil import copy2

def main():
    # 將CrystalDiskInfo的S.M.A.R.T.紀錄合併更新（以硬碟名稱為單位）
    # print(sys.argv[1]) 係欲更新的檔案所在目錄
    # print(sys.argv[2]) 係更新的檔案所在目錄
    # Smart.ini 不理他(禮呈口吻)

    fpath_updated = argv[1]
    fpath_updater = argv[2]
    fnames_updated = set(f for f in listdir(fpath_updated) if isfile(join(fpath_updated, f)) and splitext(f)[1] == '.csv')
    fnames_updater = set(f for f in listdir(fpath_updater) if isfile(join(fpath_updater, f)) and splitext(f)[1] == '.csv')

    for f in fnames_updated & fnames_updater:
        with open(join(fpath_updated, f)) as f1, open(join(fpath_updater, f)) as f2:
            lines_updated = set(f1.readlines())
            lines_updater = set(f2.readlines())
            if lines_updated != lines_updater:
                lines_updated |= lines_updater
                with open(join(fpath_updated, f), mode='w', newline='\r\n') as f1_w:
                    f1_w.writelines(sorted(lines_updated))

    for f in fnames_updater - fnames_updated:
        copy2(join(fpath_updater, f), join(fpath_updated, f))

if __name__ == '__main__':
    main()
