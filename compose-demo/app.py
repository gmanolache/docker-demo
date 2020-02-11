from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379, decode_responses=True)

@app.route("/")
def hello():
    redis.incr('hits')
    return '<p style="color:red;"> Page has been viewed %s time(s).</p>' % redis.get('hits')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
