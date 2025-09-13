### SSH properties ###
SSH_ADDRESS = ('89.208.105.233', 22)
SSH_REMOTE_BIND_ADDRESS = ('172.18.0.5', 5432)
SSH_LOCAL_BIND_ADDRESS = ('127.0.0.2', 3306)
SSH_USERNAME = 'root'
SSH_PASSWORD = '5lwkBIS3u7WW'
# SSH tunnel
# from sshtunnel import SSHTunnelForwarder
# SSH_TUNNEL = SSHTunnelForwarder(
#     ssh_address_or_host=SSH_ADDRESS,
#     remote_bind_address=SSH_REMOTE_BIND_ADDRESS,
#     local_bind_address=SSH_LOCAL_BIND_ADDRESS,
#     ssh_username=SSH_USERNAME,
#     ssh_password=SSH_PASSWORD
# )
# SSH_TUNNEL.start()

### API properties ###
API_URL = 'https://api-first.ruslansoloviev.ru'
API_MASTER_KEY = 'T4L94ICxFrqzgIT5CyeL0a39Rf6jVAvuPDwhTKcIYGJr8Nj6ohPLxM1Tgti4r8HjeoCADw03ui6Wx2pw6OaVguw=='
# User methods
API_USER_GET = '/w_user/info'
API_USER_NEW = '/w_user/new'
API_USER_KEYS = '/w_user/get_keys'
API_USER_CHANGE_PASSWORD = '/w_user/change_password'
API_USER_EDIT = '/w_user/edit'
API_USER_TOGGLE = '/w_user/toggle'
# Key methods
API_KEY_GET = '/key/info'
API_KEY_NEW = '/key/get'
API_KEY_TOGGLE = '/key/toggle'
# Struct methods
API_STRUCT_ALL = '/struct/all'
API_STRUCT_DEPARTMENTS = '/struct/departments'
API_STRUCT_GROUPS = '/struct/groups'
API_STRUCT_GROUP_INFO = '/struct/group_info'
# Timetable methods
API_TIMETABLE_GROUP = '/timetable/group'
API_TIMETABLE_TEACHER = '/timetable/teacher'
API_TIMETABLE_ALL_TEACHERS = '/timetable/all_teachers'
API_TIMETABLE_TEACHERS_BY_SURNAME = '/timetable/teachers_by_surname'
