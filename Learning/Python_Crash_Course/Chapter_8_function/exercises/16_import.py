# 多种方式导入模块与函数

# import printing_functions
from printing_functions import print_models
from printing_functions import show_completed_models as scm
# import printing_functions as pf
# from printing_functions import *

unprinted_designs = ['iphone case', 'robot pendat', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
scm(completed_models)
