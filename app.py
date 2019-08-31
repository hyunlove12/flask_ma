from flask import Flask
from flask import render_template, request, jsonify
from calculator.controller import CalculatorController
import re
app = Flask(__name__)

@app.route("/ui_calc")
def ui_calc():
    stmt = request.args.get('stmt','NONE')
    if(stmt == 'NONE'):
        print('넘어 온 값이 없음')
    else:
        print('넘어온  : {}'.format(stmt))
        #'[0-9]+' -> 0~9까지 한개 이상
        patt = '[0-9]+'
        op = re.sub(patt, '', stmt)
        print('넘어온 연산자:{}'.format(op))
        nums = stmt.split(op)
        result = 0
        n1 = int(nums[0])
        n2 = int(nums[1])
        if op == '+': result = n1 + n2
        elif op == '-': result = n1 - n2
        elif op == '*': result = n1 * n2
        elif op == '/': result = n1 / n2
    return jsonify(result = result)

@app.route('/ai_calc', method=['post'])
def ai_calc():
    num1 = request.form['num1']
    num2 = request.form['num2']
    opcode = request.form['opcode']


@app.route('/')
def index():
    return render_template('index.html')

#주소부분을 변수처리
@app.route('/move/<path>')
def move(path):
    return render_template('{}.html'.format(path))

if __name__ == "__main__":
    app.run()
