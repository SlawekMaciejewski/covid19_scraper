import re
import requests

def get_number_of_infected():
    page = requests.get('https://www.worldometers.info/coronavirus/country/poland/')
    pattern = r'Poland Coronavirus: (\d,{0,1}\d{0,})'

    obj = re.search(pattern, page.text)
    print(f'Poland Coronavirus: {obj.group(1)}')


# print(page.text)
# f = open('data.txt', 'w', encoding='utf8')
# f.write(page.text)
if __name__ == '__main__':
    get_number_of_infected()