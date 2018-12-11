from app import app
from redis import Redis


redis = Redis(host='redis', port=6379)

@app.route('/')
@app.route('/index')
def index():
    redis.incr('hits')
    return "Hello, World! for the %s time" % redis.get('hits')
'''
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
'''
