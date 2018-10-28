#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 方法一
# from package_my_print import print_one
# from package_my_print import print_two

# 方法二
#from package_my_print import print_one, print_two

# 方法三
# from package_my_print import *

# 方法四
import package_my_print.print_one as print_one
import package_my_print.print_two as print_two

from package_my_print.print_three import *


print_one.print_string('Hello, world!')
print 'PI:', print_one.PI
print_two.print_number(123)
print 'print_one all functions:', dir(print_one)
print print_one.__file__
print 'PI: %f from print_three.' % PI
a()
