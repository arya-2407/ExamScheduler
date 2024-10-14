import os
from openai import OpenAI 
from scrapper import *
from dotenv import load_dotenv
from flask import Flask, render_template, request

app = Flask(__name__)

def main(url):
    information=fetch_html(url=url)
    response=generate_response(information=information)
    print(response)

def generate_response(information):
    load_dotenv()
    api_key=os.getenv("API_KEY")
    client=OpenAI(api_key=api_key)
    prompt='''Highlight midterm dates and assignment due dates from this. 
            Give response as dict with key-value pair. 
            Key being midterm or assignment and value being the list of dates: \n''' + information  
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

@app.route('/', methods=['GET', 'POST'])
def index():
    url = None
    response=None
    if request.method == 'POST':
        url = request.form.get('url')  # Get URL from form
        if url:
            response = main(url)  # Call main function with the URL
    return render_template('index.html', url=url, response=response)


if __name__ == "__main__":
    app.run(debug=True)