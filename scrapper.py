import requests

url='https://heat.csc.uvic.ca/coview/course/2024091/CSC370?unp=t'
html_text=requests.get(url,verify=False).text
print(html_text)