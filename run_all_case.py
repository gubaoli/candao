import unittest
from common.HTMLReport import HTMLTestRunner #导入测试报告模块
import os
curdir = os.path.dirname(os.path.realpath(__file__))#获取当前路径
print(curdir)
casepath = os.path.join(curdir,"cases")#测试用例路径
reportpath = os.path.join(curdir,"baogao","candao.html") #生成测试报告路径

d = unittest.defaultTestLoader.discover(start_dir=casepath,
                                        pattern="test*.py")
print(d)
#reportpath = "D:\\candao\\baogao\\candaodenglu.html"  #测试报告模块路径
fp = open(reportpath,"wb")#二进制写入
runner = HTMLTestRunner(fp,
                        verbosity=2,
                        title="禅道登录")#报告名称
runner.run(d)
fp.close()
