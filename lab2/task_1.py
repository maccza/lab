def counting_sort(values, _max, _min=0):
    """
    Function returns sorted list.

    Sortowanie przez zliczanie to metoda polegajaca na sortowaniu wąskiego zakresu wartości
    (około 1000 kolejnych elementów) poprzez zliczenie wystąpeiń elementów w podanej liście
    i wypisania ich w kolejności.

    :param values: List of values to sort.
    :type values: List[int]
    :param _max: Maximum value in list.
    :type _max: int
    :param _min: Maximum value in list.
    :type _min: int
    :return:
    """
    compartment = list(range(_min,_max))
    count = []
    sort = []
    for i in compartment:
        count.append(0)
    for ii in values:
        count[ii]+=1   
    for iii in range(len(count)):
        if count[iii]!=0:
            for u in range(count[iii]):
                sort.append(iii)
    print(sort)               
    return sort


if __name__ == '__main__':
    assert counting_sort(
        [99, 4, 33, 2, 2, 1, 65, 3, 97, 53],
        100,
    ) == [1, 2, 2, 3, 4, 33, 53, 65, 97, 99]
