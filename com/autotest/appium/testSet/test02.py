import paramunittest

from com.autotest.appium.testSet.bsns.bsnsCommon import *

loginCls = getLoginCls()

@paramunittest.parametrized(
        *loginCls
    )

class TestBar(paramunittest.ParametrizedTestCase):


    def setParameters(self, userName,password,result):
        self.userName = userName
        self.password = password
        self.result = result


    def runTest(self):
        print(self.userName, self.password, self.result)
