"""
Na (1 pkt.):
Napisz program do sprawdzenia poprawności skompresowanego wyjścia poprzedniej
funkcji.
Funkcja MUSI w swej implementacji korzystać z wyrażeń regularnych.

Funkcja na wejściu przyjmuje nazwę pliku do sprawdzenia, na wyjściu zwraca
dwuelementową tuplę zawierającą liczbę poprawnych wierszy:
- na indeksie 0 płeć F
- na indeksie 1 płeć M
"""
import re


def check_animal_list(file_path):
    with open(file_path) as file_:
        file_.readline()
        correct_f = 0
        correct_m = 0

        for line in file_:
            string_f = r'^[A-Fa-f0-9]{8}\-[A-Fa-f0-9]{4}\-[A-Fa-f0-9]{4}\-[A-Fa-f0-9]{4}\-[A-Fa-f0-9]{12}_F_[0-9]\.[0-9]{3}e[\+\-][0-9]{2}'
            string_m = r'^[A-Fa-f0-9]{8}\-[A-Fa-f0-9]{4}\-[A-Fa-f0-9]{4}\-[A-Fa-f0-9]{4}\-[A-Fa-f0-9]{12}_M_[0-9]\.[0-9]{3}e[\+\-][0-9]{2}'
            is_correct_f = re.findall(string_f,line)
            is_correct_m = re.findall(string_m,line)
            
            if len(is_correct_f) > 0:
                correct_f = correct_f + 1
            if len(is_correct_m) > 0:
                correct_m = correct_m + 1
   
    return (correct_f,correct_m)
            


if __name__ == '__main__':
    assert check_animal_list('s_animals_sce.txt') == (2, 2)
    assert check_animal_list('animals_sc_corrupted.txt') == (5, 1)