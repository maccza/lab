def count_letters(msg):
    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """
    msg_ = []
    count = []
    
    for i in msg:
        msg_.append(ord(i))

    compartment = list(range(0,max(msg_)+1))
    for i in compartment:
        count.append(0)
    for ii in msg_:
        count[ii]+=1
    max_char = count.index(max(count))           
    return (chr(max_char),count[max_char])

if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)