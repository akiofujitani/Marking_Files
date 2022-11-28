from codecs import ignore_errors
import csv
import os
from ntpath import join
from datetime import datetime
from datetime import datetime
import time, os.path

'''
fileList
listFilesInDirSubDir
fileListFullPath
CSVtoList
listToCSV
dictToDictWriter
file_finder
file_reader
file_writer
listByDate
fileCreationDate
'''


def fileList(path, file_extention):
    return [file for file in os.listdir(path) if file.lower().endswith(f'.{file_extention}')]


def listFilesInDirSubDir(pathRoot, extention):
    fileList = []
    for root, dir, files in os.walk(pathRoot):
        for file in files:
            if file.lower().endswith(f'{extention}'):
                fileList.append(os.path.join(root, file))
    print(f'Listing for {pathRoot} done')
    return fileList


def fileListFullPath(path, file_extention):
    return [os.path.join(path, file) for file in os.listdir(path) if file.lower().endswith(f'.{file_extention}')]


def CSVtoList(filePath, case_upper=True, delimeter_char='\t'):
    with open(filePath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimeter_char)

        header = []
        header = next(csv_reader)

        csv_contents = []
        for row in csv_reader:
            row_Contents = {}
            for key in range(len(header)):
                if case_upper:
                    header_value = header[key].upper()
                else:
                    header_value = header[key]
                row_Contents[header_value] = row[key]        
            csv_contents.append(row_Contents)
    return csv_contents


def listToCSV(valuesList, filePath, errors='raise'):
    with open(filePath, 'w', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=list(valuesList[0].keys()), quoting=csv.QUOTE_ALL, extrasaction=errors)
        writer.writeheader()
        writer.writerows(valuesList)
    return


def dictToDictWriter(dictValues):
    listDictWriter = []
    for key in dictValues.keys():
        tempDict = {}
        tempDict['NUMBER'] = key
        for keyValue in dictValues[key].keys():
            tempDict[keyValue] = dictValues[key][keyValue]
        listDictWriter.append(tempDict)
    return listDictWriter


def file_finder(file_list, file_name, start_pos=0, end_pos=None):
    for file in file_list:
        cropped_name = file[start_pos:end_pos]
        if file_name in cropped_name:
            print(f'{file_name} found')
            return file
    return False


def file_reader(file_path):
    with open(file_path) as file:
        return file.readlines()


def file_writer(file_path, string_values):
    with open(file_path, 'w') as writer:
        writer.write(string_values)
        return


def listByDate(filesList, dateStart, dateEnd):
    listByDate = []
    for file in filesList:
        fileDate = fileCreationDate(file)
        if fileDate >= dateStart and fileDate <= dateEnd if dateEnd else dateStart:
            listByDate.append(file)
    print(f'Listing by date {dateStart} / {dateEnd} done')
    return listByDate


def fileCreationDate(file):
    strSplit = time.ctime(os.path.getmtime(file)).split(' ')
    for item in strSplit:
        if len(item) == 0:
            strSplit.remove(item)
    return datetime.strptime(f'{strSplit[4]}/{strSplit[1]}/{strSplit[2]}', '%Y/%b/%d').date()