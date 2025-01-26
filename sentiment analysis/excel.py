from xlwt import Workbook

def Excel(
    data: list,
    output: list
):
    wb = Workbook()

    sheet1 = wb.add_sheet('Sheet 1')

    for i, row in enumerate(output):
        sheet1.write(0, i, row)

    for i, row in enumerate(data):
        for j, cell in enumerate(output):
            print(row)
            sheet1.write(i+1, j, row[cell])

    wb.save('Tweets23-22.xls')


