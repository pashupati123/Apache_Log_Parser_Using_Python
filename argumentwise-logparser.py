from collections import Counter
import sys, getopt
# import simplejson
def generate_report(report_data,option):
    result_ouput = []
    url_lst = []
    unsuccessful_url = []
    most_requested_ip = []
    successful_status_count=0
    unsuccessful_status_count=0
    Total_request=0
    for data in report_data:
        Total_request+=1
        if(int(data['log_status'])>=200 and int(data['log_status'])<=399):
            successful_status_count+=1

        if(int(data['log_status'])<200 or int(data['log_status'])>=400):
            unsuccessful_status_count+=1

        url=data['url'].strip('"')
        if(url=='' or  url =='-'):
            continue
        else:
            url_lst.append(url)
        
        if(int(data['log_status'])<200 or int(data['log_status'])>300):
            if(url=='' or  url =='-'):
                continue
            else:
                unsuccessful_url.append(url)

        ip=data['ip_host'].strip('"')
        most_requested_ip.append(ip)

    url_counter = Counter()
    for lst in url_lst:
        url_counter[lst]+=1
    
    list_of_unsuccessful_url = Counter()
    for lst in unsuccessful_url:
        list_of_unsuccessful_url[lst]+=1
    
    dict_of_most_rquested_ip = Counter()
    for lst in most_requested_ip:
        dict_of_most_rquested_ip[lst]+=1

    result_ouput.append(url_counter.most_common(10))
    result_ouput.append((successful_status_count/Total_request)*100)
    result_ouput.append((unsuccessful_status_count/Total_request)*100)
    result_ouput.append(list_of_unsuccessful_url.most_common(10))
    result_ouput.append(dict_of_most_rquested_ip.most_common(10))

    if(option==0):
        # Top 10 Requested Pages and the number of Requests made for Each URL
        print()
        print("###########################################################################################")
        print("Requirement 1")
        print("Top 10 Requested Pages and the Number of Requests made for each Page")
        print("###########################################################################################")
        print()
        for count in url_counter.most_common(10):
            print(str(count[0]) + " (" + str(count[1]) + " Requests)")
        
        # Printing Percentage of Successful Requests (Any request with a Response Code in the range 2xxx and 3xxx)
        print()
        print("###########################################################################################")
        print("Requirement 2 ")
        print("Percentage of Successful Requests - Anything in the 200s and 300s range")
        print("###########################################################################################")
        print()
        print("Total Request: "+ str(Total_request))
        print("Successful Request: "+ str(successful_status_count))
        print("Percentage of Successful Requests is: " + str(successful_status_count/Total_request*100)+" %")
        print()
        
        # Printing Percentage of Failure Requests (Any request with a Response Code Not In the range 2xxx and 3xxx)
        print()
        print("###########################################################################################")
        print("Requirement 3 ")
        print("Percentage of UnSuccessful Requests - Anything that is not in the 200s or 300s range")
        print("###########################################################################################")
        print()
        print("Total Request: "+ str(Total_request))
        print("Failure Request: " + str(unsuccessful_status_count))
        print("Percentage of UnSuccessful Requests is: " + str(unsuccessful_status_count/Total_request*100)+" %")
        print()
        
        # Printing Top 10 Unsuccessful Page Requests
        print("###########################################################################################")
        print("Requirement 4")
        print("Top 10 Unsuccessful Page Requests")
        print("###########################################################################################")
        print()
        for count in list_of_unsuccessful_url.most_common(10):
            print(str(count[0]) + " (" + str(count[1]) + " Requests)")
        
        
        # Printing The Top 10 Hosts making the most number of requests and also the Count of Requests
        print()
        print("###########################################################################################")
        print("Requirement 5")
        print("Top 10 hosts making the most requests, displaying the IP address and number of requests made.")
        print("###########################################################################################")
        print()
        for count in dict_of_most_rquested_ip.most_common(10):
            print(str(count[0]) + " (" + str(count[1]) + " Requests)")
        print()
    
    elif(option==1):
        # Top 10 Requested Pages and the number of Requests made for Each URL
        print()
        print("###########################################################################################")
        print("Requirement 1")
        print("Top 10 Requested Pages and the Number of Requests made for each Page")
        print("###########################################################################################")
        print()
        for count in url_counter.most_common(10):
            print(str(count[0]) + " (" + str(count[1]) + " Requests)")
    
    elif(option==2):
        # Printing Percentage of Successful Requests (Any request with a Response Code in the range 2xxx and 3xxx)
        print()
        print("###########################################################################################")
        print("Requirement 2 ")
        print("Percentage of Successful Requests - Anything in the 200s and 300s range")
        print("###########################################################################################")
        print()
        print("Total Request: "+ str(Total_request))
        print("Successful Request: "+ str(successful_status_count))
        print("Percentage of Successful Requests is: " + str(successful_status_count/Total_request*100)+" %")
        print()
    
    elif(option==3):
        # Printing Percentage of Failure Requests (Any request with a Response Code Not In the range 2xxx and 3xxx)
        print()
        print("###########################################################################################")
        print("Requirement 3 ")
        print("Percentage of UnSuccessful Requests - Anything that is not in the 200s or 300s range")
        print("###########################################################################################")
        print()
        print("Total Request: "+ str(Total_request))
        print("Failure Request: " + str(unsuccessful_status_count))
        print("Percentage of UnSuccessful Requests is: " + str(unsuccessful_status_count/Total_request*100)+" %")
        print()
    
    elif(option==4):
        # Printing Top 10 Unsuccessful Page Requests
        print("###########################################################################################")
        print("Requirement 4")
        print("Top 10 Unsuccessful Page Requests")
        print("###########################################################################################")
        print()
        for count in list_of_unsuccessful_url.most_common(10):
            print(str(count[0]) + " (" + str(count[1]) + " Requests)")
    
    elif(option==5):
        # Printing The Top 10 Hosts making the most number of requests and also the Count of Requests
        print()
        print("###########################################################################################")
        print("Requirement 5")
        print("Top 10 hosts making the most requests, displaying the IP address and number of requests made.")
        print("###########################################################################################")
        print()
        for count in dict_of_most_rquested_ip.most_common(10):
            print(str(count[0]) + " (" + str(count[1]) + " Requests)")
        print()





    
    return result_ouput

def apache_output(line):
    split_line = line.split()
    return {'ip_host': split_line[0],
            'log_status': split_line[8],
            'url': split_line[10],
    }

    
def final_report(filename,option):
    report_data = []
    with open(filename) as f:
        for line in f:
            line_dict = apache_output(line)
            report_data.append(line_dict)
    
    result_output=generate_report(report_data,option)
    return result_output

def usage():
    print("python logparser.py --top-request=10 --success-request-in-percentage")

def main():
    argumentList = sys.argv[1:]

    # Options
    options = "hts:"

    # Long options
    long_options = [
        "Help",
        "top-request=",
        "success-request-in-percentage",
        "unsuccess-request-in-percentage"
    ]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

        # checking each argument
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--Help"):
                usage()
            
            elif currentArgument in ("--top-request"):
                option=1
                logfile='/Users/z004lc8/Desktop/Apache_Log_Parser_Using_Python-main/sample_input.log'
                result_output=final_report(logfile,option)
            
            elif currentArgument in ("--success-request-in-percentage"):
                option=2
                logfile='/Users/z004lc8/Desktop/Apache_Log_Parser_Using_Python-main/sample_input.log'
                result_output=final_report(logfile,option)

            elif currentArgument in ("--unsuccess-request-in-percentage"):
                option=3
                logfile='/Users/z004lc8/Desktop/Apache_Log_Parser_Using_Python-main/sample_input.log'
                result_output=final_report(logfile,option)

            elif currentArgument in ("--top-unsuccessful-request"):
                option=4
                logfile='/Users/z004lc8/Desktop/Apache_Log_Parser_Using_Python-main/sample_input.log'
                result_output=final_report(logfile,option)

            elif currentArgument in ("--top-host-request_page"):
                option=5
                logfile='/Users/z004lc8/Desktop/Apache_Log_Parser_Using_Python-main/sample_input.log'
                result_output=final_report(logfile,option)
            
        if not len(arguments):
            option=0
            logfile='/Users/z004lc8/Desktop/Apache_Log_Parser_Using_Python-main/sample_input.log'
            result_output=final_report(logfile,option)
            

    except getopt.GetoptError:
        usage()
        sys.exit(2)


if __name__ == '__main__':
    main()
    
    #f = open('result_output.txt', 'w')
    #simplejson.dump(result_output, f)
    #f.close()
