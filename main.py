from flask import Flask, render_template
app= Flask(__name__, template_folder='template')
@app.route("/")
def index():
  return render_template('index.html')
@app.route("/signin")
def connec():
  return render_template('signin.html')
if __name__=='__main__':
  app.run(debug=True)