from collections import Counter

def generate_report(report_data):
    url_lst = []
    unsuccessful_url = []
    most_requested_ip = []
    successful_status_count=0
    unsuccessful_status_count=0
    Total_request=0
    for data in report_data:
        Total_request+=1
        if(int(data['log_status'])>=200 and int(data['log_status'])<=300):
            successful_status_count+=1

        if(int(data['log_status'])<200 or int(data['log_status'])>300):
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
    print("1. Top 10 requested pages and the number of requests made for each")
    print(url_counter.most_common(10))
    print()

    # printing Percentage of successful requests (anything in the 200s and 300s range)
    print("2. Percentage of successful requests (anything in the 200s and 300s range)")
    print((successful_status_count/Total_request)*100)
    print()

     # printing Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)
    print("3. Percentage of unsuccessful requests (anything that is not in the 200s or 300s range)")
    print((unsuccessful_status_count/Total_request)*100)
    print()

    #Printing Top 10 unsuccessful page requests
    print("4. Top 10 unsuccessful page requests")
    print(list_of_unsuccessful_url.most_common(10))
    print()

    #Printing The top 10 hosts making the most requests, displaying the IP address and number of requests made.
    print("5. The top 10 hosts making the most requests, displaying the IP address and number of requests made.")
    print(dict_of_most_rquested_ip.most_common(10))
    print()





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
    
    generate_report(report_data)
    


if __name__ == '__main__':
    logfile='/Users/z004lc8/Desktop/LogScrapping/Apache_Log_Parser_Using_Python/sample_input.log'
    final_report(logfile)

