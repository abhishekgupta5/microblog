from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'Abhishek'}
    posts = [
            {
	        'author': {'nickname':'Nippo'},
		'body': 'Best goddamn roller in town!'
	    },
	    {
 	        'author': {'nickname':'Mamma'},
		'body': 'Ahhhhh!'
	    },
	    {
 	        'author': {'nickname':'Akhil'},
		'body': 'I am a great farter!'
	    },
	    {
 	        'author': {'nickname':'Yash'},
		'body': 'I am the most logical man ever!'
	    }	    	    	    
              ]
    return render_template('index.html',title='Home',user=user,posts=posts)

