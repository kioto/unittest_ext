#!/usr/bin/python3

import ut_ext

class SampleTest_1(ut_ext.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.open_csv_log(cls.__name__+'.csv')
        
    @classmethod
    def tearDownClass(cls):
        cls.close_csv_log()

    def setUp(self):
        pass

    def tearDown(self):
        self.write_csv_log((self.get_test_method_name(),
                            self.get_test_result(),
                            self.get_test_message(),))
            
    def test_001_OK(self):
        self.assertTrue(True)

    def test_002_OK(self):
        self.assertTrue(True)
        
    def test_003_FALSE(self):
        self.assertTrue(False)
        
    def test_004_ERROR(self):
        self.assertTrue(aaa)
        
    def test_005_OK(self):
        self.assertTrue(True)
        
    def test_006_FAIL(self):
        self.assertTrue(False)

    def test_007_OK(self):
        self.assertTrue(True)

"""        
class SampleTest_2(ut_ext.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.open_csv_log(cls.__name__+'.csv')
        
    @classmethod
    def tearDownClass(cls):
        cls.close_csv_log()

    def setUp(self):
        pass

    def tearDown(self):
        self.write_csv_log((self.get_test_method_name(),
                            self.get_test_result(),
                            self.get_test_message(),))
        
    def test_001_OK(self):
        self.assertTrue(True)

    def test_002_OK(self):
        self.assertTrue(True)
        
    def test_003_OK(self):
        self.assertTrue(True)
        
    def test_004_FAIL(self):
        self.assertTrue(False)
        
    def test_005_OK(self):
        self.assertTrue(True)
"""        
        
if __name__ == '__main__':
    ut_ext.main()

# end of file
