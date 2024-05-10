import mysql.connector


def calculation(expression):
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            values.append(left / right)

    def greater_precedence(op1, op2):
        precedences = {'+': 1, '-': 1, '/': 2, '*': 2}
        return precedences[op1] > precedences[op2]

    operators = []
    values = []
    i = 0
    expression = expression.replace(" ", "")
    while i < len(expression):
        if expression[i] in '0123456789':
            j = i
            while j < len(expression) and expression[j] in '0123456789':
                j += 1
            values.append(int(expression[i:j]))
            i = j
        else:
            while operators and greater_precedence(operators[-1], expression[i]):
                apply_operator(operators, values)
            operators.append(expression[i])
            i += 1

    while operators:
        apply_operator(operators, values)
    return values[0]


def update_data(expression,result):

    try:
        connect_db = mysql.connector.connect(
            user='root', password='root',
            host='localhost',
            database='testDB')

        cursor = connect_db.cursor()

        table_query = '''
            create table if not exists testDB.calculator
            ( ID int not null AUTO_INCREMENT,
            expression varchar(50) default null,
            result int default null,
            PRIMARY KEY(ID)
            );
            '''
        cursor.execute(table_query)
        insert_query = """ insert into calculator (expression, result) VALUES (%s, %s); """
        cursor.execute(insert_query,(expression,result))

    except Exception as e:
        print(str(e))

    finally:
        connect_db.commit()
        connect_db.close()


expression = " 3 * 4 - 2"
calc_result = calculation(expression)
update_data(expression,calc_result)

