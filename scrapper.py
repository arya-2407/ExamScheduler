import requests

def fetch_html(url):
    html_text=requests.get(url,verify=False).text
    return html_text

def write_file(text):
    with open('output.txt','w',encoding='utf-8') as file:
        file.write(text)
    file.close()



url='https://heat.csc.uvic.ca/coview/course/2024091/CSC370?unp=t'
text=fetch_html(url)
write_file(text)
