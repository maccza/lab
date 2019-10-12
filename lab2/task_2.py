def stack_operation(stack_commands):
    """
    Funkcja przyjmuję listę jedno i dwu elementowych krotek - operacji na stosie.
    Pierwszy element krotki to operacja, drugi wartość (opcjonalnie). Operacje:
    push - dodaj element do stosu
    pop - usuń element ze stosu
    show_max - wypisz maksymalny element w stosie
    Uzupełnij funkcje tak, by dla podanej zwróciła ciąg maksymalnych elementów (zgodny z liczbą operacj 3).

    :param stack_commands: List of tuples of stack commands.
    :type stack_commands: list
    :return: List of outputs from commands.
    :rtype: list
    """
    commend=''
    stack = []
    for i in range(len(stack_commands)):
        if(len(stack_commands[i])>1):
            command,value=stack_commands[i]
            #print(command,value)
            if(command=='push'):
                stack.append(value)

        else:
            command,=stack_commands[i]
            if(command=='pop'):
                stack.pop()
            if(command=='show_max'):
                print(max(stack))
    #print(stack)
    return stack                

if __name__ == "__main__":
    commands = [
        ('push', 97),
        ('pop',),
        ('push', 20), 
        ('pop',), 
        ('push', 26), 
        ('push', 20), 
        ('pop',), 
        ('show_max',), 
        ('push', 91), 
        ('show_max',)
    ]
    stack_operation(commands)
    assert stack_operation(commands) == [26, 91]
