# -*- coding: utf-8 -*- 
import requests
import re

url = 'https://www.sweetscape.com/010editor/repository/templates/'

response = requests.get(url)

# r = '<a href="../files/CDA.bt">CDA.bt</a>'


tmp = re.findall(r'\.\./files/\w*\.bt',response.text)


for i in tmp:
    file_name = i[9:]
    tmp_name = i[2:]
    print tmp_name
    url = 'https://www.sweetscape.com/010editor/repository' + tmp_name
    response = requests.get(url)
    f = open(file_name,'w+')
    f.write(response.text.encode('utf-8'))
    f.close()
