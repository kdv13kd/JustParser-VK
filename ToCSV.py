import vk
import csv

session = vk.Session(access_token='')   #вставить свой токен
api = vk.API(session)

#в данном модуле реализована функция, получающая информацию о пользователях и сохраняющая ее в файл формата csv

def UserInfoCSV(p):
    data = [("id;Имя;Фамилия;Пол;Дата рождения;Город;Страна;Мобильный телефон;Домашний телефон;"+
            "Веб-сайт;Количество подписчиков;Университет;Факультет;Родной город;Интересы;Музыка;"+
            "Деятельность;Фильмы;Тв;Книги;Игры;Обо мне").split(";")]
    userI = api.users.get(user_ids=p, fields={'sex', 'bdate', 'city', 'country', 'home_town','has_mobile', 'contacts', 'site', 'education',
                      'followers_count', 'activities', 'interests','music', 'movies', 'tv', 'books', 'games', 'about'}, v=5.78)
    j=0
    k = 1
    a=0
    for a in range(len(userI)):
        data.append([])
        for i in userI[0]:
            if ((i != 'university') and (i != 'faculty') and (i != 'graduation') and (i != 'has_mobile')):
                if (i == 'city'):
                    data[k].append((userI[a][i]).get('title'))
                elif (i == 'country'):
                    data[k].append((userI[a][i]).get('title'))
                elif (i == 'followers_count'):
                    data[k].append(str(userI[a].get(i)))
                elif (i == 'university_name'):
                    data[k].append(str(userI[a].get(i)))
                elif ((i == 'mobile_phone')):
                    data[k].append(str(userI[a].get(i)))
                elif ((i == 'home_phone')):
                    data[k].append(str(userI[a].get(i)))
                elif ((i == 'faculty_name')):
                    data[k].append(str(userI[a].get(i)))
                elif ((i == 'first_name')):
                    data[k].append(str(userI[a].get(i)))
                elif ((i == 'last_name')):
                    data[k].append(str(userI[a].get(i)))
                elif ((i == 'bdate')):
                    data[k].append(str(userI[a].get(i)))
                elif ((i == 'site')):
                    data[k].append(str(userI[a].get(i)))
                elif ((i == 'university_name')):
                    data[k].append(str(userI[a].get(i)))
                elif ((i == 'home_town')):
                    data[k].append(str(userI[a].get(i)))
                elif ((i == 'interests')):
                    data[k].append(str(userI[a].get(i)))
                elif ((i == 'activities')):
                    data[k].append(str(userI[a].get(i)))
                elif (i == 'music'):
                    data[k].append(str(userI[a].get(i)))
                elif (i == 'movies'):
                    data[k].append(str(userI[a].get(i)))
                elif (i == 'tv'):
                    data[k].append(str(userI[a].get(i)))
                elif (i == 'books'):
                    data[k].append(str(userI[a].get(i)))
                elif (i == 'games'):
                    data[k].append(str(userI[a].get(i)))
                elif (i == 'about'):
                    data[k].append(str(userI[a].get(i)))
                elif ((i == 'sex')):
                    if (userI[a].get(i) == 1):
                        data[k].append('Женщина')
                    else:
                        data[k].append('Мужчина')
                else:
                    data[k].append(userI[a].get(i))
            j = j + 1
        k = k + 1
        a = a + 1
    path = "Output.csv"
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in data:
            writer.writerow(line)
