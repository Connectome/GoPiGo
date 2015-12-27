from flask import Flask, Response

import main

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/stream')
def stream_yielded_values():
    # def generate():
    #     for row in iter_all_rows():
    #         yield ','.join(row) + '\n'
    return Response(main.main(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)


