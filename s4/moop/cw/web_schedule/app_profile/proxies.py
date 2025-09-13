import json
import variables as VAR

from datetime import datetime
from requests import api


class ApiKey:
    id: int
    user_id: int
    key: str
    is_master: bool
    is_active: bool
    read_access: bool
    write_access: bool
    created_date: str
    expired_date: str

    @property
    def created_fdate(self):
        month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        dt = datetime.strptime(self.created_date, '%Y-%m-%d')
        return dt.strftime(f'%d {month_list[dt.month - 1]} %Y г.')

    @property
    def expired_fdate(self):
        month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
        dt = datetime.strptime(self.expired_date, '%Y-%m-%d')
        return dt.strftime(f'%d {month_list[dt.month - 1]} %Y г.')

    def __init__(self, id, user_id, key, is_master, is_active, read_access, write_access, created_date, expired_date):
            """ DON'T USE IT OUT OF CLASS! \n You must get or create users with ApiKey.get or ApiKey.new methods """
            self.id = id
            self.user_id = user_id
            self.key = key
            self.is_master = is_master
            self.is_active = is_active
            self.read_access = read_access
            self.write_access = write_access
            self.created_date = created_date
            self.expired_date = expired_date
            self._actual = True

    def __str__(self):
        if not self._actual: return 'This api key is deprecated. You must update it with ApiKey.get'
        else:
            return json.dumps({
                'id': self.id,
                'user_id': self.user_id,
                'key': self.key,
                'is_master': self.is_master,
                'is_active': self.is_active,
                'read_access': self.read_access,
                'write_access': self.write_access,
                'created_date': self.created_date,
                'expired_date': self.expired_date
            }, indent=2)

    @staticmethod
    def get(key):
        """ Success -> ApiKey \n Key doesn't exist -> 404 \n Wrong master key -> 403 """
        params = {'master_key': VAR.API_MASTER_KEY, 'key': key}
        response = api.get(url=VAR.API_URL + VAR.API_KEY_GET, params=params)
        if response.status_code != 200: return response.status_code
        else:
            key = response.json().get('response')
            return ApiKey(
                id=key.get('id'),
                user_id=key.get('user_id'),
                key=key.get('key'),
                is_master=key.get('master_key'),
                is_active=key.get('status'),
                read_access=key.get('read'),
                write_access=key.get('write'),
                created_date=key.get('created_date'),
                expired_date=key.get('expired_date')
            )

    @staticmethod
    def new(email):
        """ Success -> ApiKey \n User doesn't exist -> 500 \n Wrong master key -> 403 \n SQL Constraints Error -> 400 """
        params = {'master_key': VAR.API_MASTER_KEY, 'user_email': email}
        response = api.get(url=VAR.API_URL + VAR.API_KEY_NEW, params=params)
        if response.status_code != 200: return response.status_code
        else:
            key = response.json().get('response').get('key')
            return ApiKey.get(key)

    def toggle(self):
        """ Success -> ApiKey \n Key doesn't exist -> 404 \n Wrong master key -> 403  """
        if not self._actual: raise ReferenceError('This api key is deprecated. You must update it with ApiKey.get')
        params = {'master_key': VAR.API_MASTER_KEY, 'key': self.key}
        response = api.patch(url=VAR.API_URL + VAR.API_KEY_TOGGLE, params=params)
        if response.status_code != 200: return response.status_code
        else:
            self._actual = False
            return ApiKey.get(self.key)


class ApiUser:
    id: int
    first_name: str
    last_name: str
    email: str
    is_staff: bool
    is_active: bool

    def __init__(self, id, first_name, last_name, email, is_staff, is_active):
        """ DON'T USE IT OUT OF CLASS! \n You must get or create users with ApiUser.get or ApiUser.new methods """
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_staff = is_staff
        self.is_active = is_active
        self._actual = True

    def __str__(self):
        if not self._actual: return 'This api user is deprecated. You must update it with ApiUser.get'
        else:
            return json.dumps({
                'id': self.id,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'is_staff': self.is_staff,
                'is_active': self.is_active
            }, indent=2)

    @staticmethod
    def get(email):
        """ Success -> ApiUser \n User doesn't exist -> 404 \n Wrong master key -> 403 """
        params = {'key': VAR.API_MASTER_KEY, 'email': email}
        response = api.get(url=VAR.API_URL + VAR.API_USER_GET, params=params)
        if response.status_code != 200: return response.status_code
        else:
            user = response.json().get('response')
            return ApiUser(
                id=user.get('user_id'),
                first_name=user.get('user_name'),
                last_name=user.get('user_surname'),
                email=user.get('user_email'),
                is_staff=user.get('user_type') == 1,
                is_active=user.get('user_status')
            )

    @staticmethod
    def new(first_name, last_name, email, is_staff=False):
        """ Success -> ApiUser \n Wrong master key -> 403 \n SQL Constraints Error -> 400 """
        data = json.dumps({'info': {'key': VAR.API_MASTER_KEY}, 'account': {'user_name': first_name, 'user_surname': last_name, 'user_email': email, 'user_type': 2 - int(is_staff), 'user_status': True}})
        response = api.post(url=VAR.API_URL + VAR.API_USER_NEW, data=data)
        if response.status_code == 200: return ApiUser.get(email)
        else: return response.status_code

    def keys(self):
        """ Success -> list[ApiKeys] \n Wrong master key -> 403 """
        if not self._actual: raise ReferenceError('This api user is deprecated. You must update it with ApiUser.get')
        params = {'key': VAR.API_MASTER_KEY, 'email': self.email}
        response = api.get(url=VAR.API_URL + VAR.API_USER_KEYS, params=params)
        if response.status_code != 200:
            if response.status_code != 404: return response.status_code
            else: return []
        else:
            keys = []
            for api_key in response.json().get('response'):
                keys.append(ApiKey.get(api_key.get('key')))
            return keys

    def edit(self, first_name=None, last_name=None, is_staff=None):
        """ Success -> ApiUser \n User doesn't exist -> 404 \n Wrong master key -> 403 """
        if not self._actual: raise ReferenceError('This api user is deprecated. You must update it with ApiUser.get')
        data = json.dumps({'info': {'key': VAR.API_MASTER_KEY}, 'account': {'user_name': first_name if first_name is not None else self.first_name, 'user_surname': last_name if last_name is not None else self.last_name, 'user_email': self.email, 'user_type': 2 - int(is_staff if is_staff is not None else self.is_staff), 'user_status': self.is_active}})
        response = api.put(url=VAR.API_URL + VAR.API_USER_EDIT, data=data)
        if response.status_code != 200: return response.status_code
        else:
            self._actual = False
            return ApiUser.get(self.email)

    def toggle(self):
        """ Success -> ApiUser \n User doesn't exist -> 404 \n Wrong master key -> 403 """
        if not self._actual: raise ReferenceError('This api user is deprecated. You must update it with ApiUser.get')
        params = {'key': VAR.API_MASTER_KEY, 'w_user_id': self.id}
        response = api.patch(url=VAR.API_URL + VAR.API_USER_TOGGLE, params=params)
        if response.status_code != 200: return response.status_code
        else:
            self._actual = False
            return ApiUser.get(self.email)
