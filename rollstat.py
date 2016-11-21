from flask import Flask, jsonify, render_template, request
import random

#Set the app name
app = Flask(__name__)

#set the homepage
@app.route('/')
def initial_load():
    return render_template('roll.html',rolls=None)

@app.route('/test_roll')
def test_roll():
    return render_template('roll.html',rolls=roll())

@app.route('/final_roll', methods=['POST'])
def final_roll():
    result=roll()
    name=request.form['name']
    with open("results.txt",'a',encoding='utf-8') as file:
        file.write(str(name)+': '+', '.join(result)+'\n')
    return render_template('roll.html',rolls=result)

def single_roll():
    roll=[random.randint(1,6) for x in range(4)]
    return sum(roll)-min(roll)

def roll():
    return [str(single_roll()) for x in range(6)]



#run everything
if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=8000)

