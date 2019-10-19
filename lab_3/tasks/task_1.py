def parse_input(input):
    """
    Splits multiline string into list of lists with integers.

    Napisz funkcję przymującą wielolinijkowy ciąg znaków.
    a zwracającą listę list liczb całkowitych znajdujących się w podanym ciągu znaków.
    Nie używaj pętl for i while.
    String może zawierać puste linie na początku i końcu.

    :param input: string to parse
    :type input: str
    :return: list of parsed list of integers
    :rtype: list
    """
    parse_string = []
    #input = list(filter(lambda x: x != '\n',input))
    input = input.split('\n')
    input = list(filter(lambda x: x != '',input))
    input = list(filter(lambda x: x != '    ',input))
    input = list(filter(lambda x: x != ' ',input))
    
    input = list(map(lambda x: x.split(), input))
    
    list(map(lambda external:parse_string.append(list(map(lambda internal: int(internal),external))), input))
    print(parse_string)
    return parse_string
if __name__ == '__main__':
    _input = """
1 5
1 6 7
3 2
1 10
1 10
1 6
2 5
3 2
    
    
    """
    assert parse_input(_input) == [
        [1, 5], [1, 6, 7], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]
    ]
