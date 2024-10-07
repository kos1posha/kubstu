import json
import time
from collections import Counter


class DiagnosisSystem:
    def __init__(self, data):
        self.data = data
        self.diseases = data['болезни']
        self.symptoms = self.sort_symptoms_by_rarity(self.diseases)
        self.constraints = data['ограничения']

    def sort_symptoms_by_rarity(self, diseases):
        symptom_counter = Counter()
        for disease in diseases:
            symptom_counter.update(disease['распространенные_симптомы'])
            symptom_counter.update(disease['редкие_симптомы'])

        sorted_common_symptoms = sorted(self.data['симптомы']['распространенные'], key=lambda x: symptom_counter[x], reverse=True)
        sorted_rare_symptoms = sorted(self.data['симптомы']['редкие'], key=lambda x: symptom_counter[x], reverse=True)
        return {'распространенные': sorted_common_symptoms, 'редкие': sorted_rare_symptoms}

    def ask_symptom(self):
        print('Пожалуйста, укажите симптом, который вас беспокоит: ', end='')
        while True:
            symptom = input()
            if symptom in self.symptoms['распространенные'] + self.symptoms['редкие']:
                break
            print('Такой симптом не найден. Повторите попытку...', end='')

        self.ask_additional_symptoms(symptom)

    def ask_additional_symptoms(self, current_symptom):
        current_symptoms = [current_symptom]
        possible_diseases = self.get_possible_diseases(current_symptoms)

        for get_next_symptoms in (self.get_next_common_symptoms, self.get_next_rare_symptoms):
            asked = [current_symptom]
            gns_args = possible_diseases, current_symptoms  # don't even ask...
            next_symptoms = get_next_symptoms(*gns_args)
            if not possible_diseases:
                print('\nНе удалось определить болезнь на основе введенных симптомов.')
                return
            while next_symptoms:
                print(f'Есть ли у вас симптом "{next_symptoms[0]}"? (да/нет): ', end='')
                while True:
                    response = input().lower()
                    if response == 'да':
                        asked.append(next_symptoms[0])
                        current_symptoms.append(next_symptoms[0])
                        possible_diseases = self.get_possible_diseases(current_symptoms, len(current_symptoms) // 3)
                        gns_args = possible_diseases, asked
                        next_symptoms = get_next_symptoms(*gns_args)
                        break
                    elif response == 'нет':
                        asked.append(next_symptoms[0])
                        next_symptoms.pop(0)
                        break
                    print('Неверный ввод. Повторите попытку...', end='')

        print('\nУ нас есть некоторые предположения. Давайте кое-что проверим...\n')
        self.ask_tests(possible_diseases)

    def ask_tests(self, possible_diseases):
        results = {}
        for disease in possible_diseases:
            tests = next(d for d in self.diseases if d['название'] == disease)['показатели'].keys()
            for test in tests:
                if test in results:
                    continue
                test_data = self.constraints[test]
                type_is_equal = test_data['тип'] == 'соответствие'
                help_prompt = ', '.join(test_data['возможные результаты']) if type_is_equal \
                    else f'{test_data["минимум"]} - {test_data["максимум"]} {test_data["мера исчисления"]}'
                print(f'Введите значение для "{test}" ({help_prompt}): ', end='')
                while True:
                    response = input()
                    if self.validate_test(test, response, type_is_equal):
                        results[test] = response if type_is_equal else float(response)
                        break
                    print(f'Значение для "{test}" не валидно. Повторите попытку...', end='')

        self.make_diagnosis(possible_diseases, results)

    def get_possible_diseases(self, symptoms=None, error=0):
        if symptoms:
            symptom_set = set(symptoms)
            result = []
            for d in self.diseases:
                common_symptoms = set(d['распространенные_симптомы'])
                rare_symptoms = set(d['редкие_симптомы'])
                if (len(symptom_set.intersection(common_symptoms)) +
                        len(symptom_set.intersection(rare_symptoms)) >= len(symptom_set) - error):
                    result.append(d['название'])
            return result
        else:
            return [d['название'] for d in self.diseases]

    def _get_next_symptoms(self, diseases, symptoms, prevalence):
        next_symptoms = set()
        for disease in diseases:
            disease_data = next(d for d in self.diseases if d['название'] == disease)
            next_symptoms.update(disease_data[f'{prevalence}_симптомы'])

        next_symptoms.difference_update(symptoms)
        if not next_symptoms:
            return None

        order_dict = {symptom: index for index, symptom in enumerate(self.symptoms[prevalence])}
        sorted_symptoms = sorted(next_symptoms, key=lambda symptom: order_dict.get(symptom, float('inf')))
        return sorted_symptoms

    def get_next_common_symptoms(self, diseases, symptoms):
        return self._get_next_symptoms(diseases, symptoms, 'распространенные')

    def get_next_rare_symptoms(self, diseases, symptoms):
        return self._get_next_symptoms(diseases, symptoms, 'редкие')

    def get_disease_symptoms(self, disease):
        disease_data = next(d for d in self.diseases if d['название'] == disease)
        return disease_data['распространенные_симптомы'] + disease_data['редкие_симптомы']

    def validate_test(self, test, value, type_is_equal):
        if type_is_equal:
            return value in self.constraints[test]['возможные результаты']
        value = float(value)
        min_value = self.constraints[test]['минимум']
        max_value = self.constraints[test]['максимум']
        return min_value <= value <= max_value

    def check_disease_conditions(self, disease_data, test_results):
        for test in test_results:
            condition = disease_data['показатели'].get(test, {})
            if condition:
                if condition['условие'] == 'больше' and test_results[test] <= condition['диапазон']:
                    return False
                elif condition['условие'] == 'меньше' and test_results[test] >= condition['диапазон']:
                    return False
                elif condition['условие'] == 'равно' and test_results[test] != condition['диапазон']:
                    return False
                elif condition['условие'] == 'входит' and not (condition['диапазон'][0] <= test_results[test] <= condition['диапазон'][1]):
                    return False
        return True

    def make_diagnosis(self, possible_diseases, test_results):
        final_diagnosis = []

        for disease in possible_diseases:
            disease_data = next(d for d in self.diseases if d['название'] == disease)
            if self.check_disease_conditions(disease_data, test_results):
                final_diagnosis.append(disease)

        if final_diagnosis:
            print('\nВозможные диагнозы: ', ', '.join(final_diagnosis))
        else:
            print('\nУ нас были некоторые подозрения, но результаты тестов показали, что вы здоровы.')

        time.sleep(2.5)
        print('\nПерезапуск системы', end='')
        for _ in range(4):
            time.sleep(1.5)
            print('.', end='')
        print('\n')
        self.ask_symptom()


if __name__ == '__main__':
    with open('knowledge.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    diagnosis_system = DiagnosisSystem(data)
    diagnosis_system.ask_symptom()
