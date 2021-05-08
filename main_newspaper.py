from flask import Flask, render_template, request
import logic
import newspaper
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/NewsCompressor')
def method1():
	hru,title=logic.processing()
	return render_template("my_html.html",hru=hru,title=title) 

@app.route('/business')
def business():
	hru,title=logic.processing()
	return render_template("my_html.html",hru=hru,title=title) 

# @app.route('/health')
# def health():
# 	hru=logic.processing()
# 	return render_template("my_html.html",hru=hru) 

# @app.route('/entertainment')
# def entertainment():
# 	hru=logic.processing()
# 	return render_template("my_html.html",hru=hru) 

# @app.route('/politics')
# def politics():
# 	hru=logic.processing()
# 	return render_template("my_html.html",hru=hru)

@app.route('/home')
def onclicknewsbutton():
	return render_template('index.html')


if __name__ == '__main__':
	app.run()