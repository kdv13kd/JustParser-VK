import urllib.request
import json

VERS = '5.78'

#запросы к API без сторонней библиотеки напрямую
#все данные возвращаются в формате JSON
#нужен токен вк для разработчика
#описание представленных методов можно найти по ссылке https://vk.com/dev/groups  , там же можно получить токен для работы с API

def UsersGet(token, user_ids):
    fields = "sex,bdate,city,country,home_town,has_mobile,contacts,site,education,followers_count,activities,interests,music,movies,tv,books,games,about"   #поля, которые нужно достать
    REQ = "users.get"                           #наименование метода API
    URL = ("https://api.vk.com/method/" + REQ +
            "?user_ids=" + user_ids +
            "&fields=" + fields +
            "&access_token=" + token +
            "&v=" + VERS)                               #ссылка запрос на получение данных
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())                      #возврат в формате JSON
    return data.get('response')

def GroupsGetById(token, group_id):
    fields = "city,country,description,members_count,start_date,finish_date,links,site,age_limits,activity,status,verified"
    REQ = "groups.getById"
    URL = ("https://api.vk.com/method/" + REQ +
           "?group_id=" + group_id +
           "&fields=" + fields +
           "&access_token=" + token +
           "&v=" + VERS)
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
    return data.get('response')

def GroupsGet(token, user_id):
    fields = ('id,name')
    REQ = "groups.get"
    EXT = "1"
    URL = ("https://api.vk.com/method/" + REQ +
           "?user_id=" + user_id +
           "&fields=" + fields +
           "&extended=" + EXT +
           "&access_token=" + token +
           "&v=" + VERS)
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
    return data.get('response')

def WallGet(token, owner_id):
    owner_id = '-' + str(owner_id)
    COUNT = '100'
    EXT = '0'
    FILT = 'all'
    REQ = "wall.get"
    URL = ("https://api.vk.com/method/" + REQ +
           "?owner_id=" + owner_id +
           "&count=" + COUNT +
           "&extended=" + EXT +
           "&filter=" + FILT +
           "&access_token=" + token +
           "&v=" + VERS)
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
    return data.get('response')

def WallGetComments(token, owner_id, post_id):
    owner_id = '-' + str(owner_id)
    post_id = str(post_id)
    SORT = 'asc'
    COUNT = '100'
    REQ = "wall.getComments"
    URL = ("https://api.vk.com/method/" + REQ +
           "?owner_id=" + owner_id +
           "&post_id=" + post_id +
           "&sort=" + SORT +
           "&count=" + COUNT +
           "&access_token=" + token +
           "&v=" + VERS)
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
    return data.get('response')

def LikesGetList(token, owner_id, item_id):
    owner_id = '-' + str(owner_id)
    item_id = str(item_id)
    TYPE = 'post'
    COUNT = '1000'
    REQ = "likes.getList"
    URL = ("https://api.vk.com/method/" + REQ +
           "?owner_id=" + owner_id +
           "&item_id=" + item_id +
           "&type=" + TYPE +
           "&count=" + COUNT +
           "&access_token=" + token +
           "&v=" + VERS)
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
    return data.get('response')

def FriendsGet(token, user_id):
    fields = 'name,deactivated'
    user_id = str(user_id)
    COUNT = '5000'
    REQ = "friends.get"
    URL = ("https://api.vk.com/method/" + REQ +
           "?user_id=" + user_id +
           "&count=" + COUNT +
           "&fields=" + fields +
           "&access_token=" + token +
           "&v=" + VERS)
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
    return data.get('response')

def UsersGetId(token, user_id):
    REQ = "users.get"
    URL = ("https://api.vk.com/method/" + REQ +
           "?user_id=" + user_id +
           "&access_token=" + token +
           "&v=" + VERS)
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
    return data.get('response')

def GroupsGetMembers(token, group_id):
    fields = 'name'
    group_id = str(group_id)
    COUNT = '1000'
    REQ = "groups.getMembers"
    URL = ("https://api.vk.com/method/" + REQ +
           "?group_id=" + group_id +
           "&count=" + COUNT +
           "&fields=" + fields +
           "&access_token=" + token +
           "&v=" + VERS)
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
    return data.get('response')

def GroupsGetMembersOffset(token, group_id, offs):
    fields = 'name'
    group_id = str(group_id)
    offs = str(offs)
    COUNT = '1000'
    REQ = "groups.getMembers"
    URL = ("https://api.vk.com/method/" + REQ +
           "?group_id=" + group_id +
           "&offset=" + offs +
           "&count=" + COUNT +
           "&fields=" + fields +
           "&access_token=" + token +
           "&v=" + VERS)
    with urllib.request.urlopen(URL) as url:
        data = json.loads(url.read().decode())
    return data.get('response')