import unittest
from source.filter import filter_error


class ErrorFilterTests(unittest.TestCase):

    def setUp(self):
        self.error_dict = {"user": 'cnelson', "error": '_NULL_',
                           'traceback': '_NULL_', 'name_of_error': '_NULL_',
                           'workspace_id': '_NULL_', "app_id": "_NULL_",
                           'type': 'ee2errorlogs', "job_id": '71777',
                           'timestamp': 'now', "err_prefix": "_NULL_",
                           'error_code': '_NULL_', 'obj_references': "_NULL_"}

    def test_easy_input(self):
        test_error_1 = ()
        test_error_2 = ''
        self.assertEqual(filter_error(test_error_1, self.error_dict), self.error_dict)
        self.assertEqual(filter_error(test_error_2, self.error_dict), self.error_dict)

    def test_medium_input(self):
        string = 'No such file or directory'
        test_error_3 = (string)
        self.error_dict['error'] = self.error_dict['err_prefix'] = "No such file or directory"
        D2 = self.error_dict
        self.assertEqual(filter_error(test_error_3, self.error_dict), D2)
        test_error_4 = " ([ {404}"
        self.error_dict['error'] = self.error_dict['err_prefix'] = 404
        D3 = self.error_dict
        self.assertEqual(filter_error(test_error_4, self.error_dict), D3)

    def test_hard_input(self):
        str1 = "no such file or directory"
        bytes_obj = bytes(str1, 'ascii', errors='strict')
        test_error_med_1 = (2, bytes_obj)
        self.error_dict['error'] = self.error_dict['err_prefix'] = "no such file or directory"
        D4 = self.error_dict
        self.assertEqual(filter_error(test_error_med_1, self.error_dict), D4)
        test_error_med_2 = '[\is not a FASTQ file***'
        self.error_dict['error'] = self.error_dict['err_prefix'] = '[\is not a FASTQ file***'
        D5 = self.error_dict
        self.assertEqual(filter_error(test_error_med_2, self.error_dict), D5)
        
