import openpyxl

files = ['E:\Python\Python_Projects\Projects\Excel_Automation\SampleData.xlsx', 'E:\Python\Python_Projects\Projects\Excel_Automation\SampleData2.xlsx']

for file in files:
    wb = openpyxl.load_workbook(file)
    worksheet = wb['SalesOrders']
    worksheet['G46'] = '=AVERAGE(G3:G45)'
    wb.save(file)