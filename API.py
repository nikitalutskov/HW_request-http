import requests, os
from pprint import pprint
#
                #TASK 1

class Hero_card:
    def __init__(self, url, name):
        self.id_hero = name
        self.url_hero = url + '/search/' + name
        self.error_message = {'error': 'invalid id', 'response': 'error'}
        if self.isnot_error():
            got_intel = self.resource["powerstats"]["intelligence"]
            self.intel = int(got_intel) if got_intel != 'null' else 0

    def get_stats(self, dict=dict(), list=list()):
        list.append(self.intel)
        dict_value = dict.get(self.intel, [])
        dict_value.append(self.id_hero)
        dict[self.intel] = dict_value
        return dict, list

    def isnot_error(self):
        self.resource = requests.get(self.url_hero).json()['results'][0]
        return True if self.resource != self.error_message else False


url_for_search = "https://superheroapi.com/api/2619421814940190"


def find_hero_cards(name_list, url=url_for_search):
    hero_list = {}
    for hero in name_list:
        hero_list[hero] = Hero_card(url, hero)
        hero_intel_dict, hero_intel_list = hero_list[hero].get_stats()
    return hero_intel_dict, hero_intel_list

def find_smart(dict, list):
    intelligence = sorted(list)[-1]
    smartest = dict[intelligence]
    text_message = 'Самый умный герой: ' if len(smartest) == 1 else 'Самые умные герои: '
    winner_str = f'{text_message}{smartest}, intelligence = {intelligence}'
    return winner_str

dict1, list1 = find_hero_cards(['Hulk', 'Captain America', 'Thanos'])
pprint(find_smart(dict1, list1))

                # TASK 2
# import requests, os
#
# class YaUploader:
#     def __init__(self, token: str):
#         self.token = token
#
#     def get_headers(self):
#         return {
#             "Authorization": "OAuth " + self.token,
#             "Accept": "application/json",
#         }
#
#     def get_upload_link(self, file_path):
#         response = requests.get(url="https://cloud-api.yandex.net:443", headers=self.get_headers(), params={
#             "path": os.path.basename(file_path),
#             "overwrite": True
#         })
#         return response.json().get("href")
#
#     def upload(self, file_path: str):
#         requests.put(url=self.get_upload_link(file_path), data=open(file_path, "rb"))
#
#
# if __name__ == '__main__':
#
#     path_to_file = input("Введите путь к вашему  файлу: ")
#     token = ""
#     uploader = YaUploader(token)
#     result = uploader.upload(path_to_file)
#     print(result)
# def get_stackoverflow():
#     files_url = 'https://api.stackexchange.com/questions/'
#     params = {'order': 'desc', 'min': '1668902400', 'max': '1669075200', 'sort': 'creation', 'tagged': 'python', 'site': 'stackoverflow'}
#     response = requests.get(files_url, params = params)
#     r = response.json()
#
#     for key in r['items']:
#         pprint(key['title'])

                # 3 TASK. Оно вроде ненужное же?

# def get_stackoverflow():
#     files_url = 'https://api.stackexchange.com/docs'
#     params = {'order': 'desc', 'min': '1668902400', 'max': '1669075200', 'sort': 'creation', 'tagged': 'python', 'site': 'stackoverflow'}
#     response = requests.get(files_url, params = params)
#     r = response.json()
#
#     for key in r['items']:
#         pprint(key['title'])

