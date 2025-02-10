#!/usr/bin/env python3
# Author ID: omelnic

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    fileText = f.read()
    f.close()
    return fileText

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    out = f.read().splitlines()
    f.close()
    return out

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name, 'w')
    for line in list_of_lines:
        f.write(line + '\n')
    f.close()


def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    fin = open(file_name_read)
    fout = open(file_name_write, 'w')
    for i, line in enumerate(fin.readlines()):
        fout.write(str(i+1) + ':' + line)
    fin.close()
    fout.close()


if __name__ == '__main__':
    file_name = 'data.txt'
    copy_file_add_line_numbers('data.txt', 'test.txt')