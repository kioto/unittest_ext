"""
Unit test extension
"""
import unittest
import csv

class TestCase(unittest.TestCase):
    """Extended TestCase class
    """
    # Test result
    __result = None

    # CSV log file
    __csv_file = None
    __csv_writer = None

    #
    # Log file control
    #
    @classmethod
    def open_csv_log(cls, filename):
        try:
            cls.__csv_file = open(filename, 'w')
            cls.__csv_writer = csv.writer(cls.__csv_file, lineterminator='\n')
        except IOError:
            print('%s: could not open' % (filename,))
            
    @classmethod
    def write_csv_log(cls, item_list):
        if cls.__csv_writer:
            cls.__csv_writer.writerow(item_list)
        
    @classmethod
    def close_csv_log(cls):
        if cls.__csv_file:
            cls.__csv_file.close()

    #
    # Test result accessor
    #
    def get_test_method_name(self):
        return self._testMethodName

    def get_test_result(self):
        """Get the test result (OK/FAIL/ERROR)
        """
        failure_info_list = self._outcome.errors[1][1]
        if not failure_info_list:
            return 'OK'
        elif failure_info_list[0].__name__ == 'AssertionError':
            return 'FAIL'
        else:                   # 'NameError'
            return 'ERROR'

    def get_test_message(self):
        """Get the ERROR/FAIL message
        """
        if hasattr(self, '_outcome'):
            # for Python3
            failure_info_list = self._outcome.errors[1][1]
            if failure_info_list:
                return failure_info_list[1]
            else:
                return ''
        else:
            # for Python2
            return 'Not supported'

def main():
    return unittest.main()

# end of file
