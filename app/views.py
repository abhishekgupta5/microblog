from app import app

@app.route('/')
@app.route('/index')
def index():
    return "This is flask"

