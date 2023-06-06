import numpy as np
import pandas as pd


class ModelProcessor:
    """
    Класс для применения различных моделей и аккумуляции результатов их работы
    Для сравнения в итоговую таблицу результатов можно добавить результаты работы других методов
    После сбора всех необходимых результатов, их можно сохранить в DataFrame таблицу
    """
    def __init__(self):
        self.scores = []
        self.result_table = []

    def process_model(self, model,
                      train_dataset,
                      test_dataset,
                      num_runs=64, ):
        """
        Обучает и тестирует модель
        :param model: Модель для прогона
        :param train_dataset: Набор данных для тренировки
        :param test_dataset: Набор данных для тестирования
        :param num_runs: Количество прогонов
        :return: Метрика качества для каждого прогона
        """
        scores = []
        for run in range(num_runs):
            train_x, train_y, = train_dataset.data, train_dataset.target
            model.fit(train_x, train_y)

            test_x, test_y = test_dataset.data, test_dataset.target
            score = model.eval(test_x, test_y)

            scores.append(score)
        self.scores.append(scores)
        return scores

    def show_results(self, scores, method=None):
        """
        :param scores: результаты работы моделей
        :param method: название метода которым получены результаты
        :return:
        """
        mean = np.round(np.array(scores).mean(), 4)
        std = np.round(np.array(scores).std(), 4)
        self.result_table.append([method, mean, std])
        if method:
            print(f'Accuracy of {method} is {mean} ±{std}')
            return method, mean, std
        else:
            print(f'Accuracy is {mean} ±{std}')
            return mean, std

    def add_result_to_compare(self, method, accuracy, std=0):
        """
        Добавить метод для сравнения
        :param method: название метода
        :param accuracy: Точность работы
        :param std: Неопределенность
        """
        self.result_table.append([method, accuracy, std])

    def create_result_table(self):
        """
        На основе аккумулированных результатов создать таблицу
        :return: DataFrame с результатами
        """
        df = pd.DataFrame(self.result_table, columns=['Method', 'accuracy', 'uncertainty'])
        return df
