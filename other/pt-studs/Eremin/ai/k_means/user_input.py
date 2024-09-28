import os
import time
from sys import maxsize as ms

from colorama import Fore, Style, init

from clustering import visualize_plane, generate_points, k_means_n_trials

init(autoreset=True)


def get_points_group_dict(count, x_min, x_max, y_min, y_max):
    return {
        'bounds': {'x_min': x_min, 'x_max': x_max, 'y_min': y_min, 'y_max': y_max},
        'points': generate_points(count, x_min, x_max, y_min, y_max)
    }


def update_global_bounds(gb, x_min, x_max, y_min, y_max):
    gb['x_min'] = min(gb['x_min'], x_min)
    gb['x_max'] = max(gb['x_max'], x_max)
    gb['y_min'] = min(gb['y_min'], y_min)
    gb['y_max'] = max(gb['y_max'], y_max)


def format_bounds(x_min, x_max, y_min, y_max):
    return f'{x_min} < x < {x_max}; {y_min} < y < {y_max}'


def format_points_list(points_list):
    if not points_list:
        return 'Пусто'
    return '\n'.join(f'{i + 1}) [{format_bounds(**pl["bounds"])}] - {", ".join(str(p) for p in pl["points"])}' for i, pl in enumerate(points_list))


def format_k_means_models(models):
    if not models:
        return 'Решения отсутствуют'
    return '\n'.join(f'{i + 1}) WCSS = {m["wcss"]}, Центроиды - {", ".join(str(c["centroid"]) for c in m["clusters"].values())}' for i, m in enumerate(models))


def print_error(message, color=Fore.RED, seconds=3):
    print(f'{color}{message}{Style.RESET_ALL}', end='')
    for _ in range(seconds):
        time.sleep(1)
        print(f'{color}.{Style.RESET_ALL}', end='')
    time.sleep(1)


def validate_index(index, length):
    if index < 1:
        print_error('Индекс не может быть меньше единицы')
        return False
    if index >= length + 1:
        print_error('Группа с таким индексом отсутствует')
        return False
    return True


def main_loop():
    points_list = []
    global_bounds = {'x_min': ms, 'x_max': -ms, 'y_min': ms, 'y_max': -ms}
    clusters_count, n_trials = None, None

    while True:
        os.system('cls')
        print(f'{Fore.LIGHTGREEN_EX}Кластеризация методом k-средних{Style.RESET_ALL}', end='\n\n')
        print(f'{Fore.GREEN}Ваши группы точек:{Style.RESET_ALL}', format_points_list(points_list), sep='\n', end='\n\n')
        print(f'{Fore.GREEN}Действия:{Style.RESET_ALL}',
              f'{Fore.LIGHTBLUE_EX}add {Fore.MAGENTA}count x_min x_max y_min y_max{Style.RESET_ALL} - Добавить группу точек',
              f'{Fore.LIGHTBLUE_EX}remove {Fore.MAGENTA}index{Style.RESET_ALL} - Удалить точки (если индекс не указан, то удаляются все группы)',
              f'{Fore.LIGHTBLUE_EX}show {Fore.MAGENTA}index{Style.RESET_ALL} - Посмотреть точки на графике (если индекс не указан, то выводятся все группы)',
              f'{Fore.LIGHTBLUE_EX}k_means {Fore.MAGENTA}clusters_count n_trials{Style.RESET_ALL} - Начать процесс кластеризации',
              sep='\n', end='\n\n')
        user_input = input(f'{Fore.GREEN}Ввод: {Style.RESET_ALL}').split()

        try:
            match user_input[0]:
                case 'add' | 'a':
                    count, x_min, x_max, y_min, y_max = int(user_input[1]), float(user_input[2]), float(user_input[3]), float(user_input[4]), float(user_input[5])
                    if x_min > x_max:
                        print_error('x_min должно быть меньше x_max')
                        continue
                    if y_min > y_max:
                        print_error('y_min должно быть меньше y_max')
                        continue
                    points_list.append(get_points_group_dict(count, x_min, x_max, y_min, y_max))
                    update_global_bounds(global_bounds, x_min, x_max, y_min, y_max)
                case 'remove' | 'r':
                    index = int(user_input[1]) if len(user_input) > 1 else None
                    if not index:
                        points_list.clear()
                    elif validate_index(index, len(points_list)):
                        points_list.pop(index - 1)
                case 'show' | 's':
                    if not points_list:
                        print_error('Вы еще не указывали точек', Fore.YELLOW)
                        continue
                    index = int(user_input[1]) if len(user_input) > 1 else None
                    if not index:
                        visualize_plane([pl['points'] for pl in points_list], **global_bounds, title='Все группы точек')
                    elif validate_index(index, len(points_list)):
                        visualize_plane([points_list[index - 1]['points']], **global_bounds, title=f'Группа точек {index}')
                case 'k_means' | 'k':
                    clusters_count, n_trials = int(user_input[1]), int(user_input[2])
                    if clusters_count < 2:
                        print_error('Кластеров должно быть хотя бы 2')
                        continue
                    if n_trials < 1:
                        print_error('Количество инициализаций метода должно быть больше нуля')
                        continue
                    break
                case _:
                    print_error('Такого действия не существует')
        except (ValueError, TypeError, IndexError):
            print_error('Ошибка ввода. Убедитесь, что правильно указали параметры')

    print()
    models = k_means_n_trials(n_trials, sum([pl['points'] for pl in points_list], start=[]), clusters_count)
    second_loop(sorted(models, key=lambda m: m['wcss']), global_bounds)


def second_loop(models, global_bounds):
    while True:
        os.system('cls')
        print(f'{Fore.LIGHTGREEN_EX}Кластеризация методом k-средних{Style.RESET_ALL}', end='\n\n')
        print(f'{Fore.GREEN}Найденные модели {Fore.LIGHTBLACK_EX}(только уникальные){Fore.GREEN}:{Style.RESET_ALL}', format_k_means_models(models), sep='\n', end='\n\n')
        print(f'{Fore.GREEN}Действия:{Style.RESET_ALL}',
              f'{Fore.LIGHTBLUE_EX}show {Fore.MAGENTA}index{Style.RESET_ALL} - Посмотреть модель',
              f'{Fore.LIGHTBLUE_EX}restart{Style.RESET_ALL} - Перезапуск программы',
              f'{Fore.LIGHTBLUE_EX}close{Style.RESET_ALL} - Завершение программы',
              sep='\n', end='\n\n')
        user_input = input(f'{Fore.GREEN}Ввод: {Style.RESET_ALL}').split()

        try:
            match user_input[0]:
                case 'show' | 's':
                    index = int(user_input[1])
                    if not validate_index(index, len(models)):
                        continue
                    model = models[index - 1]
                    wcss, clusters = model['wcss'], model['clusters']
                    centroids, points = zip(*[(c['centroid'], c['points']) for c in clusters.values()])
                    visualize_plane(points, **global_bounds, title=f'Модель {index}', centroids=centroids)
                case 'restart' | 'r':
                    main_loop()
                    break
                case 'close' | 'c':
                    break
                case _:
                    print_error('Такого действия не существует')
        except (ValueError, TypeError, IndexError):
            print_error('Ошибка ввода. Убедитесь, что правильно указали параметры')
