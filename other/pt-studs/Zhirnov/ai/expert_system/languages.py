import json

json_raw = open('languages.json', 'r', encoding='utf-8')
json_dict = json.load(json_raw)
languages = {_['name']: _['characteristics'] for _ in json_dict['languages']}
paradigms = json_dict['paradigms']
run_types = json_dict['run_types']
typing_strengths = json_dict['typing_strengths']
typing_statics = json_dict['typing_statics']
use_cases = json_dict['use_cases']


def analyze(user_requirements):
    possible_languages = [*languages.keys()]
    for requirement in user_requirements:
        for language in reversed(possible_languages):
            characteristics = languages[language]
            if requirement not in characteristics:
                possible_languages.remove(language)

    return possible_languages
