#coding=utf-8
import os
import openai
import flask
from flask import Flask

proxies = {'http': 'socks5h://127.0.0.1:1086',
'https': 'socks5h://127.0.0.1:1086'}
openai.proxy = proxies

# Your Open API-KEY HERE ↓
openai.api_key = "Your Open API-KEY HERE"  # ← Your Open API-KEY HERE
# Your Open API-KEY HERE ↑

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
        <body>
        <h1>response:</h1>
        <div id="result"></div>
        <script>
        var source = new EventSource("/chat");
        source.onmessage = function(event) {
            if (event.data === '[DONE]' || event.data == null) {
              source.close()
            } else {
              document.getElementById("result").innerHTML += event.data;
            }
        };
        </script>
        </body>
    </html>
    """

# gpt-3.5-turbo API
@app.route('/chat', methods=['GET'])
def chat_api():
    def stream():
        # send a ChatCompletion request to count to 100
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'user', 'content': 'Count to 25, with a comma between each number and no newlines. E.g., 1, 2, 3, ...'}
            ],
            temperature=0,
            stream=True  # again, we set stream=True
        )

        # iterate through the stream of events
        for chunk in response:
            chunk_message = chunk['choices'][0]['delta']  # extract the message
            content = chunk_message.get('content')
            finish_reason = chunk['choices'][0]['finish_reason']
            print(finish_reason)
            if finish_reason == 'stop':
                # although api doc shows api will response [DONE] but it doesn't, add this tag here
                yield 'data: %s\n\n' % '[DONE]'
            if content:
                content = content.replace('\n\n', '<br><br>')
                yield 'data: %s\n\n' % content

    return flask.Response(stream(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run('0.0.0.0', '5002')