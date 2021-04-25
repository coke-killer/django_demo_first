# __author__: "Yu Dongyue"
# date: 2021/4/23
from django.http import HttpResponse
from TestModel.models import Test


# 数据库操作
# 添加数据
def testdb(request):
    test1 = Test(name='小王')
    test1.save()
    return HttpResponse("数据添加成功")
# 查询数据

