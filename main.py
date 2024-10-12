import os
from openai import OpenAI 
from scrapper import *
from dotenv import load_dotenv

def main():
    url='https://heat.csc.uvic.ca/coview/course/2024091/CSC360?unp=t'
    filepath=generate_file(url=url)
    information=read_file(filepath=filepath)
    generate_response(information)
    response=generate_response(information=information)
    print(response)

def generate_file(url):
    html_text=fetch_html(url)
    file_path=make_filepath(url=url)
    write_file(text=html_text,file_path=file_path)
    return file_path

def read_file(filepath):
    with open(filepath,"r",encoding='utf-8') as file:
        information=file.read()
    return information

def generate_response(information):
    load_dotenv()
    api_key=os.getenv("API_KEY")
    client=OpenAI(api_key=api_key)
    prompt="Highligth midterm dates and assignment due dates from this : \n" + information  
    chat_completion=client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content": prompt
            
            }
        ],
        model="gpt-4"
    )
    response=chat_completion.choices[0].message.content
    return response






if __name__ == "__main__":
    main()