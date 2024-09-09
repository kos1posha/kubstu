import json
import os


def get_languages(from_file):
    json_raw = open(from_file, 'r', encoding='utf-8')
    json_dict = json.load(json_raw)
    languages = {_['name']: _['characteristics'] for _ in json_dict}
    return languages


def print_user_requirements(paradigms=None, run_type=None, typing_strength=None, typing_static=None, use_cases=None):
    if paradigms is not None:
        print('Парадигмы:', ', '.join(paradigms) if paradigms else 'не важно')
    if run_type is not None:
        print('Механизм выполнения кода:', run_type if run_type else 'не важно')
    if typing_strength is not None or typing_static is not None:
        typing = (f'{typing_strength if typing_strength is not None else ""} '
                  f'{typing_static if typing_static is not None else ""}').strip()
        if not typing:
            typing = 'не важно'
        print('Типизация:', typing)
    if use_cases is not None:
        print('Области применения:', ', '.join(use_cases) if use_cases else 'не важно')
    print()


def input_user_requirements(title, choices, many_input):
    print(
        title,
        *[f'{i}) {p}' for i, p in enumerate(choices, 1)],
        '\nОставьте поле пустым, если не важно.',
        sep='\n'
    )
    user_input = input(f'Ввод ({"номера через пробел" if many_input else "номер"}): ')
    if not user_input:
        return ''

    user_requirement = [choices[int(i) - 1] for i in user_input.split()]
    return user_requirement if many_input else user_requirement[0]


def get_user_requirements():
    user_requirements = []

    paradigms = [
        'объектно-ориентированное программирование',
        'функциональное программирование',
        'императивное программирование',
        'generic-программирование',
        'конкурентное программирование'
    ]
    required_paradigms = input_user_requirements('Выберите поддерживаемые парадигмы программирования:', paradigms, True)
    user_requirements.extend(required_paradigms)
    os.system('cls')
    print_user_requirements(required_paradigms)

    run_types = [
        'компиляция',
        'интерпретация'
    ]
    required_run_type = input_user_requirements('Выберите механизм выполнения кода:', run_types, False)
    if required_run_type:
        user_requirements.append(required_run_type)
    os.system('cls')
    print_user_requirements(required_paradigms, required_run_type)

    typing_strengths = [
        'строгая',
        'слабая'
    ]
    required_typing_strength = input_user_requirements('Выберите строгую/слабую типизацию:', typing_strengths, False)
    if required_typing_strength:
        user_requirements.append(required_typing_strength)
    os.system('cls')
    print_user_requirements(required_paradigms, required_run_type, required_typing_strength)

    typing_statics = [
        'статическая',
        'динамическая'
    ]
    required_typing_static = input_user_requirements('Выберите статическую/динамическую типизацию:', typing_statics, False)
    if required_typing_static:
        user_requirements.append(required_typing_static)
    os.system('cls')
    print_user_requirements(required_paradigms, required_run_type, required_typing_strength, required_typing_static)

    use_cases = [
        'анализ данных',
        'веб-разработка',
        'десктопные приложения',
        'корпоративные системы',
        'математические вычисления',
        'машинное обучение',
        'мобильные приложения',
        'написание скриптов',
        'разработка игр',
        'распределенные системы',
        'системное программирование',
        'статистические вычисления'
    ]
    required_use_cases = input_user_requirements('Выберите области применения языка:', use_cases, True)
    user_requirements.extend(required_use_cases)
    os.system('cls')
    print_user_requirements(required_paradigms, required_run_type, required_typing_strength, required_typing_static, required_use_cases)
    return user_requirements


def analyze(user_requirements, languages):
    possible_languages = [*languages.keys()]
    for requirement in user_requirements:
        for language in reversed(possible_languages):
            characteristics = languages[language]
            if requirement not in characteristics:
                possible_languages.remove(language)

    return possible_languages


def main():
    languages = get_languages('languages.json')
    user_requirements = get_user_requirements()
    results = analyze(user_requirements, languages)

    if not results:
        print('Не удалось найти языки программирования на основе введенных требований.')
        return

    print('Рекомендуемые языки программирования:')
    for language in results:
        print(f'- {language}')


if __name__ == '__main__':
    main()
