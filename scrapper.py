import requests
import re
import random
import os

def fetch_html(url):
    html_text=requests.get(url,verify=False).text
    return html_text

def write_file(text,file_path):
    with open(file_path,'w',encoding='utf-8') as file:
        file.write(text)
    file.close()

def get_filepath(url):
    match = re.search(r'/course/\d+/(CSC\d+)', url)
    if match:
        course_code = match.group(1)
        print(course_code)
    else:
        rand_int=random.randint(1,100)
        course_code='Random'+rand_int
    filename=f"{course_code}.txt"
    output_dir="outputs"
    filepath=os.path.join(output_dir,filename)
    return filepath
    


url='https://heat.csc.uvic.ca/coview/course/2024091/CSC370?unp=t'
text=fetch_html(url)
file_path=get_filepath(url)
write_file(text,file_path)
