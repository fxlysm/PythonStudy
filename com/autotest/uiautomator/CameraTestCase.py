from uiautomator import device as d
import unittest
import time

class LauncherTest(unittest.TestCase):

    def setUp(self):
        d.server.sdk_version()
        self.seq = range(10)
        d.press.back()
        time.sleep(2)
        d.press.home()
        time.sleep(2)


class MessageTest(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def addmessage(self):
        d.press.home()


class CameraTest(unittest.TestCase):
    def setUp(self):
        self.seq = range(10)

    def test_take_picture(self):
        d.press.back()

if __name__ == '__main__':
    unittest.main()
    suite1 = unittest.TestLoader().loadTestsFromTestCase(LauncherTest)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(MessageTest)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(CameraTest)


    suite = unittest.TestSuite([suite1, suite2,suite3])
    unittest.TextTestRunner(verbosity=3).run(suite)
