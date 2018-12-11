from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)