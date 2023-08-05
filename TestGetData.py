import openpyxl
import datetime
workbook=openpyxl.load_workbook('absen.xlsm')
sheet = workbook['Sheet1']

JumlahData = len(sheet['A'])
a=2
while a <= JumlahData:
    date    = sheet['A'+str(a)].value
    date2   = sheet['B'+str(a)].value
    jam1    = sheet['C'+str(a)].value
    jam     = sheet['D'+str(a)].value
    work    = sheet['F'+str(a)].value
    project = sheet['G'+str(a)].value
    a+=1
    jam2=jam1.strftime('%H:%M')
    jam3=jam.strftime('%H:%M')
    print(date, date2, jam2)