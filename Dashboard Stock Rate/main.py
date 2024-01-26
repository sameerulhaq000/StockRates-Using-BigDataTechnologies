from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

#Load the CSV data into a DataFrame
data1 = pd.read_csv('HSI.csv')
data2 = pd.read_csv('N225.csv')
data3 = pd.read_csv('GSPTSE.csv')

@app.route('/')

def dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard1')
def dashboard1():
    return render_template('dashboard1.html', data=data1)

@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html', data=data2)

@app.route('/dashboard3')
def dashboard3():
    return render_template('dashboard3.html', data=data3)

if __name__ == '__main__':
    app.run(debug=True)