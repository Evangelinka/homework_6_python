# Есть список из слов разной длины. Необходимо вернуть список из слов такой же длины. 
# Если слово короче, чем самое длинное слово, дополнить "*" недостающие буквы с правого края до максимальной длины
# Пример: ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'] --> ['a****', 'aa***', 'aaa**', 'aaaa*', 'aaaaa']

def all_len_row(my_list):
    max_item = max(my_list, key=lambda x: len(x))
    max_len = len(max_item)
    return [item.ljust(max_len, '*') for item in my_list]
print(all_len_row(['qwerty', 'qwert', 'qwer', 'qwe', 'qw', 'q']))