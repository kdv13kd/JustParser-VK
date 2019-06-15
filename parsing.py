import without_vk_lib as vk2
import time
from operator import itemgetter

token = ""      #вставить свой токен
#session = vk.Session(access_token='')      #вставить свой токен
#api = vk.API(session)


#запросы к API могут совершаться как при помощи сторонних библиотек (например, библиотека vk), так и при помощи самолично написанных запросов к API без сторонней библиотеки
#все данные возвращаются в формате JSON
#нужен токен вк для разработчика
#описание представленных методов можно найти по ссылке https://vk.com/dev/groups  , там же можно получить токен для работы с API


def checkText(field, stroka):
    if (type(stroka) == tuple):
        stroka = ' '.join(map(str, stroka))
    field = field + stroka
    return field

def userInfo(user):           #здесь 2 пути реализовано. Закомментированный запрос - это запрос через библиотеку vk, а user = vk2.UsersGet(token, user) - это
                            #запрос через функции собственного модуля without_vk_lib.py. Данный модуль был написан, как аналог в случае, если библиотека vk откажет в работе
                            #остальные запросы в данном модуле реализованы аналогичным образом

    #user = api.users.get(user_ids=str(user1),fields={'sex','bdate','city','country','home_town','has_mobile','contacts',
                #'site','education','followers_count','activities','interests','music','movies','tv','books','games','about'}, v = 5.78)
    user = vk2.UsersGet(token, user)
    retStr = ''
    for i in user[0]:
        if ((i!='university')and(i!='faculty')and(i!='graduation')and(i!='has_mobile')):
            if (i=='city'):
                stroka = ('Город:\t\t ' + ((user[0][i]).get('title')))
            elif (i=='country'):
                stroka = ('Страна:\t\t ' + ((user[0][i]).get('title')))
            elif (i == 'followers_count'):
                stroka = ('Количество подписчиков:  ', user[0].get(i))
            elif (i == 'university_name'):
                stroka = ('Университет:\t\t', user[0].get(i))
            elif ((i=='mobile_phone')):
                stroka = ('Мобильный телефон:\t', user[0].get(i))
            elif ((i == 'home_phone')):
                stroka = ('Домашний телефон:\t', user[0].get(i))
            elif ((i == 'faculty_name')):
                stroka = ('Факультет:\t\t', user[0].get(i))
            elif ((i == 'first_name')):
                stroka = ('Имя:\t\t', user[0].get(i))
            elif ((i == 'last_name')):
                stroka = ('Фамилия:\t\t', user[0].get(i))
            elif ((i == 'bdate')):
                stroka = ('Дата рождения:\t', user[0].get(i))
            elif ((i == 'site')):
                stroka = ('Веб-сайт:\t\t', user[0].get(i))
            elif ((i == 'university_name')):
                stroka = ('Университет:\t\t', user[0].get(i))
            elif ((i == 'home_town')):
                stroka = ('Родной город:\t', user[0].get(i))
            elif ((i == 'interests')):
                stroka = ('Интересы:\t\t', user[0].get(i))
            elif ((i == 'activities')):
                stroka = ('Деятельность:\t', user[0].get(i))
            elif (i == 'music'):
                stroka = ('Музыка:\t\t', user[0].get(i))
            elif (i == 'movies'):
                stroka = ('Фильмы:\t\t', user[0].get(i))
            elif (i == 'tv'):
                stroka = ('Тв:\t\t', user[0].get(i))
            elif (i == 'books'):
                stroka = ('Книги:\t\t', user[0].get(i))
            elif (i == 'games'):
                stroka = ('Игры:\t\t', user[0].get(i))
            elif (i == 'about'):
                stroka = ('Обо мне:\t\t', user[0].get(i))
            elif ((i == 'sex')):
                if (user[0].get(i) == 1):
                    stroka = 'Пол:\t\t Женщина'
                else:
                    stroka = 'Пол:\t\t Мужчина'
            else:
                stroka = (i +'\t\t', user[0].get(i))
            retStr = checkText(retStr, stroka)
            retStr = retStr + '\n'
    return retStr

def groupInfo(group):
    #   group = api.groups.getById(group_id=str(group1),fields={'city','country','description','members_count','start_date',
                                #'finish_date','links','site','age_limits','activity','status','verified'},v=5.78)
    group = vk2.GroupsGetById(token, group)
    retStr = ''
    for i in group[0]:
        if ((i != 'is_admin') and (i != 'is_member') and (i != 'admin_level') and (i != 'photo_50') and (
                i != 'photo_100')):
            if (i == 'country'):
                stroka = ('Cтрана:\t         ' + ((group[0][i]).get('title')))
            elif (i == 'city'):
                stroka = ('Город:\t         ' + ((group[0][i]).get('title')))
            elif (i == 'links'):
                stroka = ('Ссылки:\t\t ' + group[0][i][0].get('url'))
            elif (i == 'members_count'):
                stroka = ('Количество участников:    ', group[0][i])
            elif (i == 'screen_name'):
                stroka = ('Название в URL:                ', group[0][i])
            elif (i == 'id'):
                stroka = (i + '\t\t', group[0][i])
            elif (i == 'name'):
                stroka = ('Название:\t\t', group[0][i])
            elif (i == 'activity'):
                stroka = ('Род деятельности:\t', group[0][i])
            elif (i == 'site'):
                stroka = ('Веб-сайт:\t\t', group[0][i])
            elif (i == 'description'):
                stroka = ('Описание:\t\t', group[0][i])
            elif (i == 'verified'):
                stroka = ('Верификация:\t', group[0][i])
            elif (i == 'status'):
                stroka = ('Статус:\t\t', group[0][i])
            elif (i == 'type'):
                stroka = ('Тип:\t\t', group[0][i])
            elif (i == 'photo_200'):
                stroka = ('Картинка:\t\t', group[0][i])
            elif (i == 'start_date'):
                stroka = str(group[0][i])
                stroka = stroka[6:len(stroka)] + '/' + stroka[4:6] + '/' + stroka[0:4]
                stroka = ('Дата создания:\t ' + stroka)
            elif (i == 'is_closed'):
                stroka = 'Закрытое сообщество:\t', group[0][i]
            elif ((i == 'age_limits')):
                if (group[0][i] == 1):
                    stroka = 'Возврастное ограничение:\t Нет'
                elif (group[0][i] == 2):
                    stroka = 'Возврастное ограничение:\t 16+'
                else:
                    stroka = 'Возврастное ограничение:\t 18+'
            else:
                stroka = (i + ':\t        ', group[0][i])
            retStr = checkText(retStr, stroka)
            retStr = retStr + '\n'
    retStr = retStr + ('URL:\t\t https://vk.com/club' + str(group[0]['id']))
    return retStr

def userGr(user):
    #   user = api.groups.get(user_id=str(user1),extended=1,fields={'id', 'name'}, v=5.78)
    user = vk2.GroupsGet(token, user)
    retStr = ("Название\t\t"+"Тип\t"+"Закрытое\tURL\n\n")
    for i in range(user.get('count')):
        itdict = user.get('items')[i]
        if (itdict.get('is_closed') == 0):
            stroka = (itdict.get('name') + '\t\t' + itdict.get('type') + '      open      ')
        else:
            stroka = (itdict.get('name') + '\t\t' + itdict.get('type') + '      close      ')
        stroka = stroka + 'https://vk.com/club' + str(itdict.get('id')) + '\n'
        retStr = checkText(retStr, stroka)
    return retStr

def GetComments(gr):
    # posts = api.wall.get(owner_id='-' + str(group1), count=100, extended=0, filter=all, v=5.78)
    posts = vk2.WallGet(token, gr)
    postID = []
    for i in range(len(posts.get('items'))):
        postID.append(posts.get('items')[i].get('id'))
    dictID = {}
    maxPost = {}
    for i in range(len(postID)):
        #commes = api.wall.getComments(owner_id='-' + str(group1),post_id=str(postID2[i]),sort='asc' ,count=100,v=5.78)
        commes = vk2.WallGetComments(token, gr, postID[i])
        if not commes.get('items'):
            pass
        else:
            if (i == 0):
                dictID = dict.fromkeys([commes.get('items')[i].get('from_id')], 1)
                maxPost = dict.fromkeys([postID[i]], commes.get('count'))
                for j in range(len(commes.get('items'))):
                    dictID[(commes.get('items')[j].get('from_id'))] = 1
            else:
                maxPost[postID[i]] = commes.get('count')
                for g in range(len(commes.get('items'))):
                    if (((commes.get('items')[g].get('from_id')) in dictID) == True):
                        dictID[commes.get('items')[g].get('from_id')] = dictID.get(commes.get('items')[g].get('from_id')) + 1
                    else:
                        dictID[(commes.get('items')[g].get('from_id'))] = 1
        time.sleep(0.3)
    dictID = sorted(dictID.items(), key=itemgetter(1), reverse=True)
    maxPost = sorted(maxPost.items(), key=itemgetter(1), reverse=True)
    return (dictID, maxPost)

def GetLikes(gr):
    #posts = api.wall.get(owner_id='-' + str(group1), count=100, extended=0, filter=all, v=5.78)
    posts = vk2.WallGet(token, gr)
    postID = []
    for i in range(len(posts.get('items'))):
        postID.append(posts.get('items')[i].get('id'))
    dictID = {}
    maxPost = {}
    for i in range(len(postID)):
        #likes = api.likes.getList(type='post',owner_id='-' + str(group1),item_id=str(postID[i]),count=1000, v=5.78)
        likes = vk2.LikesGetList(token, gr, postID[i])
        if not likes.get('items'):
            pass
        else:
            if (i == 0):
                dictID = dict.fromkeys([likes.get('items')[0]], 1)
                maxPost = dict.fromkeys([postID[i]], likes.get('count'))
                for j in range(len(likes.get('items'))):
                    dictID[(likes.get('items')[j])] = 1
            else:
                maxPost[postID[i]] = likes.get('count')
                for g in range(len(likes.get('items'))):
                    if ((likes.get('items')[g] in dictID) == True):
                        dictID[likes.get('items')[g]] = dictID.get(likes.get('items')[g]) + 1
                    else:
                        dictID[(likes.get('items')[g])] = 1
            time.sleep(0.3)
    dictID = sorted(dictID.items(), key=itemgetter(1), reverse=True)
    maxPost = sorted(maxPost.items(), key=itemgetter(1), reverse=True)
    return (dictID, maxPost)

def GetNetworkUser(id):
    #   user = api.friends.get(user_id=id, fields={'name', 'deactivated'},count=5000, v=5.78)
    user = vk2.FriendsGet(token, id)
    Frid = []
    for i in user.get('items'):
        if ('deactivated' in i):
            pass
        else:
            Frid.append(i.get('id'))
    Frid.append(id)
    file = open('Vertex.txt', 'wt', encoding='utf8')
    for i in user.get('items'):
        if ('deactivated' in i):
            pass
        else:
            file.write(str(i.get('id')) + '\t' + str(i.get('first_name') + ' ' + i.get('last_name') + '\n'))
    #   user = api.users.get(user_id=id, v=5.78)
    user = vk2.UsersGetId(token, id)
    file.write(str(id + '\t' + user[0].get('first_name')) + ' ' + str(user[0].get('last_name') + '\n'))
    file.close()
    file = open('Edges.txt', 'wt')
    for i in Frid:
        f = []
        #getF = api.friends.get(user_id=i, fields={'name', 'deactivated'}, count=5000, v=5.78)
        getF = vk2.FriendsGet(token, i)
        for j in getF.get('items'):
            if ('deactivated' in j):
                pass
            else:
                if j.get('id') in Frid:
                    f.append(str(j.get('id')))
        for index in f:
            file.write(str(i) + '\t' + index + '\n')
        time.sleep(0.33)
    file.close()

def GetNetworkGroup(id):
    #   member = api.groups.getMembers(group_id=id, fields='name', count=1000, v=5.78)
    member = vk2.GroupsGetMembers(token, id)
    count = member.get('count')
    cl = 0
    while (count > 0):
        count = count - 1000
        cl = cl + 1
    time.sleep(0.33)
    offs = 0
    Frid = []
    file = open('Vertex.txt', 'wt', encoding='utf8')
    for i in range(cl):
        #   member = api.groups.getMembers(group_id=id, fields='name', offset=offs, count=1000, v=5.78)
        member = vk2.GroupsGetMembersOffset(token, id, offs)
        for i in member.get('items'):
            if ('deactivated' in i):
                pass
            else:
                Frid.append(i.get('id'))
        for i in member.get('items'):
            if ('deactivated' in i):
                pass
            else:
                file.write(str(i.get('id')) + '\t' + str(i.get('first_name') + ' ' + i.get('last_name') + '\n'))
        offs = offs + 1000
    file.close()
    file = open('Edges.txt', 'wt')
    for i in Frid:
        f = []
        #   member = api.friends.get(user_id=i, fields={'name', 'deactivated'}, count=5000, v=5.78)
        member = vk2.FriendsGet(token, i)
        for j in member.get('items'):
            if ('deactivated' in j):
                pass
            else:
                if j.get('id') in Frid:
                    f.append(str(j.get('id')))
        for j in f:
            file.write(str(i) + '\t' + str(j) + '\n')
        file.write(str(i) + '\t' + str(id) + '\n')
        time.sleep(0.33)
    file.close()