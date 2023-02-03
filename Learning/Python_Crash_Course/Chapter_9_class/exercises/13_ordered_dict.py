# 使用有序字典

from collections import OrderedDict

glossary = OrderedDict()
glossary['key'] = '键'
glossary['value'] = '值'
glossary['min'] = '最小'
glossary['max'] = '最大'
glossary['sum'] = '求和'

for key, value in glossary.items():
    print(key + ": " + value)
