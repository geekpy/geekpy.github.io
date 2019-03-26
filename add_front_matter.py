#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Develop By: Liu Ziqian
Created Date: 2018.08.11
File Name: add_fron_matter.py
File Description: to add front matter in the md posts files
"""
import sys
import glob
import os


FRONT_MATTER_TEMPLATE = """
title:
date: 2018-08-12 18:18:18
layout: page
comments: true\n
"""


def is_folder(folder_path):
    if os.path.isdir(folder_path):
        return True
    else:
        return False


def is_md_file(file_path):
    if file_path[-3:] == ".md" and os.path.exists(file_path):
        return True
    else:
        return False


def get_md_files(folder_path):
    md_path = os.path.join(folder_path, "*.md")
    files = glob.glob(md_path)
    return files


def add_front_matter(file_path):
    with open(file_path, "r+") as f:
        f.write(FRONT_MATTER_TEMPLATE)


def main():
    arguments = sys.argv
    if len(arguments) == 0:
        print "You need input folder name or name!"
    elif len(arguments) == 1:
        # judge whether it is folder or file
        path_str = arguments[0]
        if is_folder(path_str):
            files = get_md_files(path_str)
            if len(files) == 0:
                print "there is no md files in the folder<%s>" % path_str
            for file_path in files:
                add_front_matter(file_path)
        elif is_md_file(path_str):
            add_front_matter(path_str)
        else:
            print "the path<%s> is neither a folder nor a md file" % path_str
    else:
        for file_paht in arguments:
            if is_md_file(file_path):
                add_front_matter(file_path)
            else:
                print "the file<%s> is not a md file or exists" % file_path


if __name__ == '__main__':
    main()


