
class ExpressionCheck:
    def __init__(self):
        self.error_message = ""

    def operate_check(self, expression):
        """
        校验表达式是否正确
        :param expression: 表达式
        :return: message
        """
        char_list = list(expression)
        for index, char in enumerate(char_list):
            if index == 0 or index == len(char_list) - 1:
                continue
            if char in '+-*/.^√':
                if not ((char_list[index - 1].isdigit() or char_list[index - 1] in ")") and (
                        char_list[index + 1].isdigit() or char_list[index + 1] == "(")):
                    self.error_message = "表达式错误"
                    return False
                elif char == "/" and char_list[index + 1] == "0":
                    self.error_message = "被除数不能是0"
                    return  False
        print(AN)
        return True

    def bracket_check(self, expression):
        brackets = []  #stack
        for char in expression:
            if char == "(":
                brackets.append("(")
            elif char == ")":
                if brackets:
                    brackets.pop()
                else:
                    self.error_message = "右括号多"
                    return False
        if brackets:
            self.error_message = "左括号多"
            return False
        return True

    def special_check(self, expression):
        if expression.isdigit():
            return True
        if not (expression[0].isdigit() or expression[0] == "-" or expression[0] == "("):
            self.error_message = "开头字符错误"
            return False
        elif not (expression[-1].isdigit() or expression[-1] == ")"):
            self.error_message = "结尾字符错误"
            return False
        return True

    def is_valid(self, expression):
        """
        表达式是否可用
        :param expression: 表达式
        :return: message
        """
        if not all(char.isdigit() or char in '+-*/.()^√' for char in expression):
            return "表达式错误"
        if self.operate_check(expression) and self.bracket_check(expression) and self.special_check(expression):
            return "成功"
        else:
            return self.error_message

if __name__ == '__main__':
    expression_check = ExpressionCheck()
    expression = "-2+(3-1)+(1*3)"
    print(expression_check.is_valid(expression))



