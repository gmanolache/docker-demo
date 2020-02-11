from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379, decode_responses=True)

@app.route("/")
def hello():
    """We increment the page hits and return the body of the page"""
    redis.incr('hits')

    text = '''
    <p style="color:red;">
        Page has been viewed %s time(s).
    </p>'''

    return text % redis.get('hits')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
