'''
Created on 06-April-2019

@author: ankit.deswal
'''
import faker
import xlwt

    
data =faker.Faker()
wk = xlwt.Workbook()
ws = wk.add_sheet("Test Data")
for i in range(1,10):
    ws.write(i,0,data.name())
    ws.write(i,1,data.email())
    ws.write(i,2,data.city())

wk.save("D:\TestDataPython\Result.xls")

