import openpyxl

def read_data(file,sheetname,row_number,col_number):
    workbook = openpyxl.load_workbook(filename=file)
    sheet = workbook[sheetname]
    return sheet.cell(row=row_number,column=col_number)

# print(read_data("TestData/logindata.xlsx",'Sheet1',1,1))