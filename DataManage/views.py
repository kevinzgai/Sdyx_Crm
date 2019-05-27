import datetime

import xlrd
from django.http import HttpResponse
from django.template import loader

from DataManage.models import yueke
from DataManage.Excel.ExcelTodo import ExcelToDo

# Create your views here.
def uploadDate(request):
    starttime = datetime.datetime.now()

    # long running
    ExcelToDo.readXls('/Users/kevin/Desktop/Sdyx_Crm/Data/粤科/线上影票订单表2019-04-01 06_00_00-2019-04-08 05_59_59.xls')
    endtime = datetime.datetime.now()

    t = loader.get_template("index.html")
    c = {"foo": "用时："+str((endtime - starttime).seconds)}
    return HttpResponse(t.render(c, request))


def GetsaleNameList(request):
    salelist= yueke.objects.order_by('saleName').distinct('saleName')
    #for name in salelist.all():
    print(salelist.all())
    return HttpResponse(salelist)


def readXls(filePath):
    data = xlrd.open_workbook(r'' + filePath + '')
    # 获取所有sheet
    # print(data.sheet_names())  # [u'sheet1', u'sheet2']
    table1 = data.sheet_by_index(0)  # 得到第一个表格
    listData = list()
    for row in range(5,table1.nrows):
        order = table1.row_values(row)
        # print(order)

        yuekeOrder = yueke(
            cinemaName=order[0],
            saleName=order[1],
            tranType=order[2],
            orderNum=order[3],
            tranTime=datetime.datetime.strptime(order[4], "%Y-%m-%d %H:%M:%S"),
            movieName=order[5],
            showTime=datetime.datetime.strptime(order[6], "%Y-%m-%d %H:%M:%S"),
            seatNum=order[7],
            voteNum=order[8],
            totalAmount=float(order[9]),
            priceAmount=float(order[10]),
            lowFare=float(order[11]),
            handFee=float(order[12]),
            alwayHandFee=float(order[13]),
            subsidies=float(order[14]),
            subsidiesParty=order[15]
        )
        listData.append(yuekeOrder)

        # yuekeModel=yueke
        # yueke.cinemaName
        # print(table1.row_values(row))  # 遍历所有表格
    yueke.objects.bulk_create(listData)
