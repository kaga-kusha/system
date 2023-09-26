import xlwt
from xlwt import Workbook
wb = Workbook()
mc = wb.add_sheet('1006')
mc.write(0,0,'0,0')
mc.write(0,1,'0,1')
mc.write(0,2,'0,2')
mc.write(0,3,'0,3')
wb.save('0.xls')