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
