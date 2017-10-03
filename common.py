#截取url，保留其访问传参方式（POST/GET/PUT/DELETE）,保留url的头与尾
def deal_url(url):
    url_str = url.replace(' HTTP/1.1','')
    if url_str.find(' ') > -1:
        url_type = url_str[0 : url_str.find(' ')+1]
    if url_str.find('/') > -1 and url_str.find('?') > -1:
        url_str = url_type + url_str[url_str.find('/')+1 : url_str.find('?')]
    if url_str.find('/') > -1 and url_str.find(';jsessionid') > -1:
        url_str = url_type + url_str[url_str.find('/')+1 : url_str.find(';jsessionid')]
    if url_str.find('/') > -1 and url_str.rfind('/') > -1:
        url_str = url_str[0 : url_str.find('/')] + '/.../' + url_str[url_str.rfind('/')+1 : ]
    return url_str

#根据日志内容，创建一个信息的op_detail
def create_op_detail(row_log):
    op_detail = dict()
    op_detail['start_time'] = row_log['@timestamp']
    op_detail['end_time'] = row_log['@timestamp']
    op_detail['urls'] = list()
    op_detail['urls'].append(deal_url(row_log['request']))
    print (row_log['@timestamp'])
    return op_detail