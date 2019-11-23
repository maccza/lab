"""
Jesteś informatykiem w firmie Noe's Animals Redistribution Center.
Firma ta zajmuje się międzykontynentalnym przewozem zwierząt.
---------
Celem zadania jest przygotowanie funkcji pozwalającej na przetworzenie
pliku wejściowego zawierającego listę zwierząt do trasnportu.
Funkcja ma na celu wybranie par (samiec i samica) z każdego gatunku,
tak by łączny ładunek był jak najlżeszy (najmniejsza masa osobnika
rozpatrywana jest względem gatunku i płci).
---------
Na 1 pkt.
Funkcja ma tworzyć plik wyjściowy zwierający listę wybranych zwierząt
w formacie wejścia (takim samym jak w pliku wejściowym).
Wyjście ma być posortowane alfabetycznie względem gatunku,
a następnie względem nazwy zwierzęcia.
---------
Na +1 pkt.
Funkcja ma opcję zmiany formatu wejścia na:
"<id>_<gender>_<mass>"
(paramter "compressed") gdzie:
- "id" jest kodem zwierzęcia (uuid),
- "gender" to jedna litera (F/M)
- "mass" zapisana jest w kilogramach w notacji wykładniczej
z dokładnością do trzech miejsc po przecinku np. osobnik ważący 456 gramów
ma mieć masę zapisaną w postaci "4.560e-01"
---------
Na +1 pkt.
* Ilość pamięci zajmowanej przez program musi być stałą względem
liczby zwierząt.
* Ilość pamięci może rosnąć liniowo z ilością gatunków.
---------
UWAGA: Możliwe jest wykonanie tylko jednej opcji +1 pkt.
Otrzymuje się wtedy 2 pkt.
UWAGA 2: Wszystkie jednoski masy występują w przykładzie.
"""
from pathlib import Path
from collections import namedtuple
import  csv
def select_animals(input_path, output_path, compressed=False):
    
    animal_list = []
    animal = namedtuple('animal',['id','mass','unit','genus','name','gender'])
    with open(input_path) as file_opened:
        file_opened.readline()
        for i in file_opened:
                temp = i.split(',')
                animal_list.append(animal(temp[0],
                temp[1].split(' ')[0],
                temp[1].split(' ')[1],
                temp[2],
                temp[3],
                temp[4].split("\n")[0]))
    animal_list = sorted(animal_list,key=lambda animal: (animal.genus,animal.name))
   
    famale_animal = list(filter(lambda y:y.gender!='male',animal_list))
    male_animal = list(filter(lambda y:y.gender!='female',animal_list))
    male_animal = sorted(male_animal,
        key = lambda y:(float(y.mass) if y.unit in ['KG',"Kg","kg"] 
        else (float(y.mass)*0.001 if y.unit in ['G',"g"] else (float(y.mass)*0.001 if y.unit =='mg' else float(y.mass)*1000))
        ,y.genus))
    famale_animal = sorted(famale_animal,
        key = lambda y:
        ((float(y.mass) if y.unit in ['KG',"Kg","kg"] else (float(y.mass)*0.001 if y.unit in ['G',"g"] else (float(y.mass)*0.001 if y.unit =='mg' else float(y.mass)*1000))),y.genus))
    selected_female = []
    selected_male = []
    selected_female.append(famale_animal[0])
    selected_male.append(male_animal[0])
    temp_genus_female = {selected_female[0].genus}
    temp_genus_male = {selected_male[0].genus}
    for i in famale_animal:
        if i.genus not in temp_genus_female:
            selected_female.append(i)
        temp_genus_female.add(i.genus)
    for i in male_animal:
        if i.genus not in temp_genus_male:
            selected_male.append(i)
        temp_genus_male.add(i.genus)
    selected_animal = selected_female + selected_male
    selected_animal = sorted(selected_animal,key = lambda animal:(animal.genus,animal.name))
    if compressed == False:
            with open(output_path, 'w') as _file:
                _file.write('id,mass,genus,name,gender\n')
                for i in selected_animal:
                    _file.write(i[0]+","+
                    i[1]+" "+
                    i[2]+","+
                    i[3]+","+
                    i[4]+","+
                    i[5]+"\n")
    else:
        multiplier = {
            'mg': 0.000001,
            'g': 0.001,
            'kg': 1.,
            'Mg': 1000.,
        }
        gender = {
            'female':'F',
            'male':'M'
        }
        with open(output_path, 'w') as _file:
            _file.write('uuid_gender_mass\n')
            for i in selected_animal:
                uuid = i.id
                gender_ = gender[i.gender]
                mass = float(i.mass)*multiplier[i.unit]
                _file.write(uuid+'_'+gender_+'_'+'%.3e' % mass+'\n') 
if __name__ == '__main__':
    input_path = Path('s_animals.txt')
    output_path = Path('s_animals_s.txt')
    select_animals(input_path, output_path)
    with open(output_path) as generated:
        with open('s_animals_se.txt') as expected:
            assert generated.read() == expected.read()

    output_path = Path('s_animals_sc.txt')
    select_animals(input_path, output_path, True)
    with open(output_path) as generated:
        with open('s_animals_sce.txt') as expected:
            assert generated.read() == expected.read()
