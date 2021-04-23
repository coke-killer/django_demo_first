# __author__: "Yu Dongyue"
# date: 2021/4/23
from django import template
# 语义化标签
from django.utils.safestring import mark_safe

register = template.Library()  # register的名字是固定的，不可改变的


# 利用装饰器自定义过滤器，参数最多有两个
@register.filter()
def my_filter(v1, v2):
    return v1 * v2


# 利用装饰器自定义标签
@register.simple_tag()
def my_tag1(v1, v2, v3):
    return v1 * v2 * v3


#  在使用自定义标签和过滤器前，要在html文件body的最上方导入该py文件
# {load my_tags}
@register.simple_tag()
def my_tag2(v1, v2):
    temp_html = "<input type='text' id='%s' class='%s' />" % (v1, v2)
    return mark_safe(temp_html)
