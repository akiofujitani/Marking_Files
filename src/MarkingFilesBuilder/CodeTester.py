from datetime import date, datetime
import os, time


# def fileCreationDate(file):
#     strSplit = time.ctime(os.path.getmtime(file)).split(' ')
#     for item in strSplit:
#         if len(item) == 0:
#             strSplit.remove(item)
#     return datetime.strptime(f'{strSplit[4]}/{strSplit[1]}/{strSplit[2]}', '%Y/%b/%d').date()


# filePath = r'C:\Users\Calculo\OneDrive - RENOVATE COM.DE MAT.E PROD OPTICOS LTDA\Documentos\Development\LMS_File_Volpe\LMS_Compare\20220606.TXT'

# at_now = date.today()

# print(at_now)

# data_string = f'{at_now.day}/{at_now.month}/{at_now.year}'
# print(data_string)

# date_in_text = at_now.strftime('%d/%m/%Y')

# print(date_in_text)
# print('')

# date_and_time = datetime.now()
# date_and_time_text = date_and_time.strftime('%d/%m/%Y')

# print(date_and_time)
# print(date_and_time_text)

# date_with_hour = date_and_time.strftime('%d/%m/%Y %H:%M')

# print(date_with_hour)
# print(type(date_with_hour))

# justdate = date_and_time.strftime('%d/%m/%Y')
# print(f'just date {justdate}')

# stringDate = '05/02/2022 14:57'

# print(stringDate)

# convertToDate = datetime.strptime(stringDate, '%d/%m/%Y %H:%M:%S')
# convertToDate = datetime.strptime(stringDate, '%d/%m/%Y %H:%M')
# print(convertToDate)

