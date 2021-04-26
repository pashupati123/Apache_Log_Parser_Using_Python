# Apache_Log_Parser_Using_Python

Run the logparser.py file using below command

        python3 logparser.py
       
It will Read Apache log file(access.log)

        Provide the log file path in the main functon to the variable logfile

Calling the method final_report by passing the logfile to generate the result

Creating the report_data from the logfile list of dict, where each dict have field "ip_host", "log_status" and "url" 

passing the result_data list to the generate_report method for finding the below detail and printing 

      1. Top 10 requested pages and the number of requests made for each
      2. Percentage of successful requests (anything in the 200s and 300s range)
      3. Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)
      4. Top 10 unsuccessful page requests
      5. The top 10 hosts making the most requests, displaying the IP address and number of requests made.

Finally attached the result_output.txt file for reference 



-------------------------------------------------------------------------------
To Run the test cases

install pytest which I have used for testing framework

     pip3 install pytest pytest-timeout pytest-xdist

Run the testcases using below command

     python3 -m pytest unit_test_case.py
     
Two test case implemented 
     
     1. To test the format of logfile which i am using to generate the output from logfile(access.log) 
         apache_output method tested from logparser.py file using tested data from test_input.log which will give actual result_data 
         and asserted against mock data 
     2. To test the output generated 
         generate_result method tested from logparser.py file using tested data from test_input.log which will generate expected ouput
         result and asserted against mock data
    
