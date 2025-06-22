def main(input_list):
    sum = 0
    for num in input_list:
        sum += num
    if not input_list:
        result = None
    else:
        result = float(format(sum / len(input_list), '.2f'))
    if result is None:
        print(f'Список пуст')
        print('by Kirsanov Platon')
        return None
    else:
        print(f'Среднее арифметическое - {result}')
        print('by Kirsanov Platon')
        return result
