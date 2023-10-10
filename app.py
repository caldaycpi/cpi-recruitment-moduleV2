from flask import Flask, render_template ,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title':'Data Scientist',
        'location':'Manila Philippines',
        'salary': '20,000'
    },
    {
        'id' : 2,
        'title':'Human Resource',
        'location':'Manila Philippines',
        'salary': '25,000'
    },
    {
        'id' : 3,
        'title':'Data Analysis',
        'location':'Manila Philippines',
        'salary': '30,000'
    },
    {
        'id' : 4,
        'title':'Human Resource',
        'location':'Manila Philippines',
        'salary': '20,000'
    }
    
]

@app.route("/")
def hello_world():
    return render_template('home.html' ,jobs = JOBS,company_name = "CRECIENDO PHILLIPINES INC.")

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__' :
    app.run(host='0.0.0.0', debug=True)