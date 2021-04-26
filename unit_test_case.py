import pytest
from logparser import apache_output
from logparser import generate_report

#testing the apache_output method from logparser.py file
def test_for_apache_output():
    test_logfile='/Users/z004lc8/Desktop/Apache_Log_Parser_Using_Python/test_input.log'
    testing_report_data = [{'ip_host': '45.138.145.131', 'log_status': '200', 'url': '"-"'}]
    actual_report_data = []
    with open(test_logfile) as f:
        for line in f:
            line_dict = apache_output(line)
            actual_report_data.append(line_dict)
    assert actual_report_data == testing_report_data, "test_passed"


#testing the generate_report method from logparser.py file
def test_for_generate_report():
    test_logfile='/Users/z004lc8/Desktop/Apache_Log_Parser_Using_Python/test_input.log'
    testing_result = [[], 100.0, 0.0, [], []]
    actual_report_data = []
    with open(test_logfile) as f:
        for line in f:
            line_dict = apache_output(line)
            actual_report_data.append(line_dict)
    actual_result=generate_report(actual_report_data)
    assert actual_result == testing_result
    