import json
import sys

# global file syntax
function_def_head = '\ndef '
bracket_without_params = '():'
for_base_syntax = 'for i in range('


def input_formatter(input_text):
    return 'raw_input(\"' + input_text + '\")'


def generate_for_loop(print_obj, list_len):
    for_loop = for_base_syntax
    for_loop += list_len + '):' + double_new_line()
    for_loop += print_something(print_obj, False) + new_line()
    return for_loop


def generate_for_loop_with_format(print_obj, var, list_len):
    for_loop = for_base_syntax
    for_loop += list_len + '):' + double_new_line()
    for_loop += print_something_with_format(print_obj, var, False)
    return for_loop


def print_something(print_obj, is_list_length, list_len=0):
    if is_list_length and list_len > 0:
        return generate_for_loop(print_obj, list_len)
    else:
        return 'print(\"' + print_obj + '\")'


def print_something_with_format(print_obj, var, is_list_length, list_len=0):
    if is_list_length and list_len > 0:
        return generate_for_loop_with_format(print_obj, var, list_len)
    else:
        base_string = '\"' + print_obj + '\" % ('
        size = len(var)
        for i in range(size - 1):
            base_string += var[i] + ', '
        base_string += var[size - 1] + ')'
        return 'print( ' + base_string + ' )'


def get_input_writer(var, msg):
    return var + ' = ' + input_formatter(msg)


def get_input_writer_with_option(var, msg, options):
    size = len(options)
    option_string = '( '
    for i in range(0, size - 1):
        option_string += options[i] + '/'
    option_string += options[size - 1] + ' )'
    return var + ' = ' + input_formatter(msg + option_string)


def new_line():
    return '\n\t'


def double_new_line():
    return '\n\t\t'


def write_conditions(var, msg, conditions):
    final_condition_statement = 'while '
    size_1 = len(conditions)
    for i in range(0, size_1 - 1):  # or condition
        final_condition_statement += '( '
        size_2 = len(conditions[i])
        for j in range(0, size_2 - 1):  # and condition
            final_condition_statement += '( ' + conditions[i][j] + ' )' + ' and '
        final_condition_statement += '( ' + conditions[i][size_2 - 1] + ' )'
        final_condition_statement += ' ) or'
    final_condition_statement += '( '
    size_2 = len(conditions[size_1 - 1])
    for j in range(0, size_2 - 1):  # and condition
        final_condition_statement += '( ' + conditions[size_1 - 1][j] + ' )' + ' and '
    final_condition_statement += '( ' + conditions[size_1 - 1][size_2 - 1] + ' )'
    final_condition_statement += ' )'
    final_condition_statement += ':' + double_new_line()
    final_condition_statement += get_input_writer(var, msg) + new_line()
    return final_condition_statement


def write_formula(var, formula):
    return var + ' = ' + formula + new_line()


def write_bot_backend_from_rules(rules_in_json):
    backend_file_path = 'backend/handler.py'
    with open(backend_file_path, 'a') as file_writer:
        file_writer.write(function_def_head + '' + rules_in_json['function'] + bracket_without_params + new_line())
        file_writer.write('response = {}' + new_line() +
                          'calc_stage = 0' + new_line())  # creating dict for saving response series
        for rule in rules_in_json['questions']:
            print(rule)
            # local variables to identify the rule type
            is_instruction = False
            is_condition = False
            is_text = False
            is_options = False
            is_instruction_var = False
            is_formula = False
            is_list_length = False

            for r_name, r_value in rule.iteritems():
                if r_name == 'instruction':
                    is_instruction = True
                if r_name == 'conditions':
                    is_condition = True
                if r_name == 'text':
                    is_text = True
                if r_name == 'options':
                    is_options = True
                if r_name == 'instruction_var':
                    is_instruction_var = True
                if r_name == 'formula':
                    is_formula = True
                if r_name == 'list_length':
                    is_list_length = True

            if is_instruction:
                list_length = 0
                if is_list_length:
                    list_length = rule['list_length']
                if is_instruction_var:
                    file_writer.write(print_something_with_format(rule['instruction'], rule['instruction_var'],
                                                                  is_list_length, list_len=list_length)
                                      + new_line())
                else:
                    file_writer.write(print_something(rule['instruction'], is_list_length, list_len=list_length)
                                      + new_line())
                continue
            elif is_condition:
                file_writer.write(write_conditions(rule['var'], rule['text'], rule['conditions']))
                continue
            elif is_text and is_options:
                file_writer.write(get_input_writer_with_option(rule['var'], rule['text'], rule['options'])
                                  + new_line())
                continue
            elif is_text:
                file_writer.write(get_input_writer(rule['var'], rule['text']) + new_line())
                continue
            elif is_formula:
                file_writer.write(write_formula(rule['var'], rule['formula']))

        file_writer.write('\n')  # ending file
        file_writer.close()


if __name__ == '__main__':
    file_path = sys.argv[1]  # considering relative path
    with open(file_path, 'r') as r_file:
        rules = json.loads(r_file.read())
        r_file.close()
        write_bot_backend_from_rules(rules)
