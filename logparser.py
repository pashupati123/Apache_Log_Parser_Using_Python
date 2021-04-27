from collections import Counter
import simplejson
def generate_report(report_data):
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

    #Top 10 requested pages and the number of requests made for each
    print("##############################################################")
    print("Requirement 1")
    print("##############################################################")
    print()
    top_10_requested_pages = url_counter.most_common(10)
    for item in top_10_requested_pages:
        print(item)
    print()
    result_ouput.append(url_counter.most_common(10))

    # printing Percentage of successful requests (anything in the 200s and 300s range)
    print("##############################################################")
    print("Requirement 2 and 3")
    print("##############################################################")
    print()
    print("Total Request: "+ str(Total_request))
    print("Successful Request: "+ str(successful_status_count))
    print("Failure Request: " + str(unsuccessful_status_count))
    print("Percentage of Successful Request is: " + str(successful_status_count/Total_request*100))
    print("Percentage of UnSuccessful Request is: " + str(unsuccessful_status_count/Total_request*100))
    print()
    result_ouput.append((successful_status_count/Total_request)*100)
    result_ouput.append((unsuccessful_status_count/Total_request)*100)

    #Printing Top 10 unsuccessful page requests
    print("##############################################################")
    print("Requirement 4")
    print("##############################################################")
    print()
    top_10_unsuccessful_url= list_of_unsuccessful_url.most_common(10)
    for item in top_10_unsuccessful_url:
        print(item)
    print()
    result_ouput.append(list_of_unsuccessful_url.most_common(10))

    #Printing The top 10 hosts making the most requests, displaying the IP address and number of requests made.
    print("##############################################################")
    print("Requirement 5")
    print("##############################################################")
    print()
    top_10_host_making_most_req = dict_of_most_rquested_ip.most_common(10)
    for item in top_10_host_making_most_req:
        print(item)
    print()
    result_ouput.append(dict_of_most_rquested_ip.most_common(10))
    return result_ouput





def apache_output(line):
    split_line = line.split()
    return {'ip_host': split_line[0],
            'log_status': split_line[8],
            'url': split_line[10],
    }

    
def final_report(filename):
    report_data = []
    with open(filename) as f:
        for line in f:
            line_dict = apache_output(line)
            report_data.append(line_dict)
    
    result_output=generate_report(report_data)
    return result_output


if __name__ == '__main__':
    logfile='/Users/z004lc8/Desktop/LogScrapping/Apache_Log_Parser_Using_Python/sample_input.log'
    result_output=final_report(logfile)
    f = open('result_output.txt', 'w')
    simplejson.dump(result_output, f)
    f.close()
