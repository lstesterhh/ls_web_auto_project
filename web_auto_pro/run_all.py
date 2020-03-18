import unittest
from common import HTMLTestRunner_cn

#用例路径
casePath="G:\\web_auto_pro\\case"
rule="test*.py"
discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

reportPath="G:\\web_auto_pro\\report\\"+"report.html"
fp=open(reportPath,"wb")
runner=HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title="报告的title",description="描述你的报告干什么用的",retry=1)
runner.run(discover)
fp.close()