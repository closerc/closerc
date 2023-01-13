# 循环遍历字典的键和值

glossary = {
    'print': '打印',
    'for': '循环',
    'if': '条件测试',
    'list': '列表',
    'dict': '字典',
}

glossary['key'] = '键'
glossary['value'] = '值'
glossary['min'] = '最小'
glossary['max'] = '最大'
glossary['sum'] = '求和'

for key, value in glossary.items():
    print(key + ": " + value)
