import logging.config
from flask import Flask, request, render_template
from calculate.calculating import Calculator
from match_keyword.dataset import Matcher

logging.config.fileConfig('logging.conf')

app = Flask(__name__)
app.static_folder = 'static'

pythonCalculator = Calculator()
matcher = Matcher()

up_button_is_sum, up_sum_result, expression_check_res = False, "", True


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    ''' Main Function that checks for the server requests,
    takes the given variables from the server and uses them in a conditional statement,
    uses the Calculator class in a try statement,
    handles exceptions and renders the variables on the HTML Page'''

    expression = ''
    result = ''
    global up_button_is_sum, up_sum_result, expression_check_res
    if request.method == 'POST':
        expression = request.form.get('expression', '')
        button = request.form.get('button', '')

        if button == 'C':
            expression = ''
            result = ''
            pythonCalculator.clear()
            up_button_is_sum, up_sum_result = False, ""
        elif button == '=':
            up_button_is_sum = True
            split_expression = ''.join(char for char in expression)
            try:
                result, expression_check_res = pythonCalculator.calculate_expression(split_expression)
                up_sum_result = result
                if expression_check_res is False:
                    result = result
            except Exception as e:
                result = ''
        elif up_button_is_sum and not expression_check_res:  # 上一次按钮是等号 并且表达式不合理
            expression = expression + button
            up_button_is_sum, up_sum_result = False, ""
        elif up_button_is_sum and button in '+-*/.^√()' and expression_check_res:  # 上一次按钮是等号 并且表达式合理，这次是符号 需要在上一次的结果上继续加
            expression = str(up_sum_result) + button
            up_button_is_sum, up_sum_result = False, ""

        elif up_button_is_sum and button.isdigit() and expression_check_res:  # 上一次按钮是等号并且表达式合理，这次是数字，直接开始重新计算
            expression = button
            result = ''
            pythonCalculator.clear()
            up_button_is_sum, up_sum_result = False, ""
        else:
            expression += button
            up_button_is_sum, up_sum_result = False, ""
    return render_template('index.html', expression=expression, result=result)


@app.route('/qa_healthy', methods=['GET', 'POST'])
def query_answer():
    question, answer = "", ""
    if request.method == 'POST':
        question = request.form.get('question')
        # 在这里处理问题，例如通过调用机器学习模型或其他逻辑
        question, answer = matcher.match_query(question)
    return render_template('qa.html', question=question, answer=answer)


if __name__ == '__main__':
    app.run(debug=True, port=8088)

