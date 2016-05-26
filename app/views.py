from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me="%s"' %(form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])
