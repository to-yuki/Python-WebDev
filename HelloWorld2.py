from flask import Flask, escape, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    title = 'INPUT TEST'
    return render_template('form.html',title=title)
    
@app.route('/input')
def hello():
    name = request.args.get('name','')
    print(escape(name))
    return render_template('hello.html',name=escape(name))
	
if __name__ == "__main__":
    app.run(debug=True)