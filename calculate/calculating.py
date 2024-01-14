import logging
from expresssion_check import ExpressionCheck
logger = logging.getLogger(__name__)


class Calculator:
    '''
    计算器内核
    '''

    def __init__(self):
        self.result = None
        self.expression_check = ExpressionCheck()

    @staticmethod
    def _calculate(num1, num2, operator):
        num1, num2 = float(num1), float(num2)
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("被除数不能是0")
        elif operator == "^":
            return num1 ** num2
        elif operator == "√":
            if num2 == 0:
                raise ZeroDivisionError("不能开0次方")
            return num1 ** (1 / num2)
        else:
            raise TypeError("错误操作")
        return num1 / num2

    def bracket_calculate(self, expression):
        """
        :param expression: 表达式
        :return: 结果
        """
        while "(" in expression or ")" in expression:
            bracket_start, bracket_end = 0, len(expression)
            for index in range(len(expression)):
                if expression[index] == "(":
                    bracket_start = index
                elif expression[index] == ")":
                    bracket_end = index
                    break
            assert bracket_end > bracket_start
            bracket_expression_list = self.expression_split(expression[bracket_start + 1: bracket_end])
            bracket_expression_list = self.power_calculate(bracket_expression_list)
            bracket_expression_list = self.multiplication_division_calculate(bracket_expression_list)
            bracket_sum = self.add_subtraction_calculate(bracket_expression_list)
            expression = expression[0:bracket_start] + "{:+}".format(bracket_sum) + expression[bracket_end + 1:]
        return expression

    def expression_split(self, expression):
        """
        :param expression: 表达式
        :return: 结果
        """
        expression_list = []
        start = 0
        for index, char in enumerate(expression):  # 按符号拆分
            if char in "+-*/()^√":
                if index == 0:
                    continue
                expression_list.append(expression[start:index])
                expression_list.append(char)
                start = index + 1
        expression_list.append(expression[start:len(expression)])  # 增加最后一个token
        expression_list = [x for x in expression_list if x]
        return expression_list

    def power_calculate(self, expression_list):
        """
        :param expression_list:
        :return:
        """
        while "^" in expression_list or "√" in expression_list:  # 有序计算乘除
            expression_list_update = []
            index = 1
            while index < len(expression_list):
                pre = expression_list[index]
                if pre == "^" or pre == "√":
                    expression_list_update = expression_list[:index - 1] + [
                        self._calculate(expression_list[index - 1], expression_list[index + 1], pre)] + expression_list[
                                                                                                        index + 2:]
                    index += 3
                else:
                    index += 1
            expression_list = expression_list_update
        return expression_list

    def multiplication_division_calculate(self, expression_list):
        """
        :param expression_list: 表达式拆分
        :return: 结果
        """
        # 表达式拆分

        while "*" in expression_list or "/" in expression_list:  # 有序计算乘除
            expression_list_update = []
            index = 1
            while index < len(expression_list):
                pre = expression_list[index]
                if pre == "*" or pre == "/":
                    expression_list_update = expression_list[:index - 1] + [
                        self._calculate(expression_list[index - 1], expression_list[index + 1], pre)] + expression_list[
                                                                                                        index + 2:]
                    index += 3
                else:
                    index += 1
            expression_list = expression_list_update
        return expression_list

    def add_subtraction_calculate(self, expression_list):
        """
        :param expression_list: 表达式拆分
        :return: 结果
        """
        expression_sum = expression_list[0]
        for index in range(1, len(expression_list), 2):  ## 顺序计算结果
            expression_sum = self._calculate(expression_sum, expression_list[index + 1], expression_list[index])
        return expression_sum

    def calculate_expression(self, expression):
        """
        重写表达式，使其符合先乘除后加减的运算规则
        :param expression: 原始表达式
        :return: 重写后的表达式
        """
        expression_check_message = self.expression_check.is_valid(expression)
        if expression_check_message != "成功":
            return expression_check_message, False
        # 优先级计算先计算括号
        expression = self.bracket_calculate(expression)
        # 拆分表达式
        expression_list = self.expression_split(expression)
        # 计算幂次
        expression_list = self.power_calculate(expression_list)
        # 计算乘除
        expression_list = self.multiplication_division_calculate(expression_list)
        # 计算加减
        expression_sum = self.add_subtraction_calculate(expression_list)
        # self.result = eval(expression)
        self.result = expression_sum
        ## 结果格式
        self.result = round(self.result, 2)
        # self.result = "{:.2f}".format(self.result)
        # self.result = "{:.1e}".format(self.result)  # 输出：1.234568e+09
        return self.result, True

    def clear(self):
        """
        清除所有
        :return:
        """
        self.result = None
        logger.info("Result has been cleared!")
