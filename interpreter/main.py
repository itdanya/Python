import requests


URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'past you key'

headers_auth = {'Authorization': 'Basic ' + KEY}
auth = requests.post(URL_AUTH, headers=headers_auth)
print("Возвращаемый код запроса: " + str(auth.status_code))

if auth.status_code == 200:
    token = auth.text

    while True:
        word = input('Введите слово для перевода: ')
        if word:
            headers_translate = {
            'Authorization': 'Bearer ' + token
            }
            params = {
            'text': word,
            'srcLang': 1033,
            'dstLang': 1049
            }
            r = requests.get(URL_TRANSLATE, headers=headers_translate,
                            params=params)
            res = r.json()
            try:
                print(res['Translation']['Translation'])
            except:
                print('Не найден вариант перевода')
else:
    print("Error . . . !")
