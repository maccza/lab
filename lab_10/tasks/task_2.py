import pathlib
from typing import Optional, Union, List
from urllib.parse import urljoin
import requests
import csv
import os
API_URL = 'https://www.metaweather.com/api/'


def get_city_data(
        woeid: int, year: int, month: int,
        path: Optional[Union[str, pathlib.Path]] = None,
        timeout: float = 5.) -> (str, List[str]):
    
    if path == None:
        if month < 10:
            path_ = f"{woeid}_{year}_0{month}/"
        else:
            path_ = f"{woeid}_{year}_{month}/"
    else:
        if month < 10:
            path_ = path + "/" + f"{woeid}_{year}_0{month}/"
        else:
            path_ = path + "/" + f"{woeid}_{year}_{month}/"
    
    if not os.path.exists(path):
         os.mkdir(path)
    if not os.path.exists(path_):
        print(path_)
        os.mkdir(path_)
    
    number_days = None
    if month == 2:
        if year% 4 == 0:
            number_days = 29
        else:
            number_days = 28
    if month in [1,3,5,7,8,10,12]:
        number_days = 31
    else:
        number_days = 30 
    
    
    
    session = requests.session()
    for day in range(1,number_days+1):
        location_url = urljoin(API_URL, f"location/{woeid}/{year}/{month}/{day}")
        response = session.get(location_url, timeout=timeout)
        file_paths = None
        if month < 10 and day < 10:
            file_paths = path_ + f'{year}_0{month}_0{day}.csv'
        if month < 10 and day >= 10:
            file_paths = path_ + f'{year}_0{month}_0{day}.csv'
        if month >= 10 and day < 10:
            file_paths = path_ + f'{year}_{month}_0{day}.csv'
        if response.json():
            with open(file_paths,mode='w+') as f:
                writer = csv.writer(
                    f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
                )
                writer.writerow(response.json()[0].keys())
               
                for row in response.json():

                    writer.writerow(row.values())

    
    return str(path_),file_paths


if __name__ == '__main__':
    # _path = pathlib.Path.cwd()
    # expected_path = _path / '523920_2017_03'
    # dir_path, file_paths = get_city_data(523920, 2017, 3)
    # assert len(file_paths) == 31
    # assert pathlib.Path(dir_path).is_dir()
    # assert str(expected_path) == dir_path

    expected_path = 'weather_data/523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3, path='weather_data')
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path

    expected_path = 'weather_data/523920_2012_12'
    dir_path, file_paths = get_city_data(523920, 2012, 12, path='weather_data')
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path
