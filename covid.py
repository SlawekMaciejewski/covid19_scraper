import re
import requests


def get_number_of_infected():
    page = requests.get('https://www.worldometers.info/coronavirus/country/poland/')
    pattern = r'Poland Coronavirus: (\d,{0,1}\d{0,})'
    obj = re.search(pattern, page.text)

    return obj.group(1)


# print(page.text)
# f = open('page.txt', 'w', encoding='utf8')
# f.write(page.text)
if __name__ == '__main__':
    print(f'From the website "Poland Coronavirus" : {get_number_of_infected()} persons')

    with open('data.txt', 'r') as f:
        SAVED_DATA = f.readline()

    CURRENT_DATA = get_number_of_infected()

    if SAVED_DATA != CURRENT_DATA:
        with open('data.txt', 'w') as f:
            f.write(str(CURRENT_DATA))
        print(f'New data from file, infected are {CURRENT_DATA} persons')
    else:
        print('No new infected')
