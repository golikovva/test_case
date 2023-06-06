import torch
import numpy as np
from sklearn.linear_model import RidgeClassifierCV
from kernel_functions import generate_kernels, apply_kernels


class ROCKET:
    """
    Модель ROCKET для классификации одномерных временных рядов
    num_kernels - количество сверточных ядер
    Поддерживается несколько видов генерации весов сверточных ядер.
    Можно выбрать тип во время инициализации класса, либо поменять его в любой момент
    Виды генерации:
        normal - веса порождаются из нормального распределения N(0, 1)
        uniform - веса порождаются равномерным распределением от 0 до 1
        binary - однородная выборка целочисленных весов из {−1, 1}.
        ternary - однородная выборка целочисленных весов из {−1, 0, 1}.
    """
    def __init__(self, num_kernels=1000, kernel_weights_distribution='normal'):
        self.num_kernels = num_kernels
        self.kernels = None
        self.classifier = RidgeClassifierCV(alphas=np.logspace(-3, 3, 10))
        self.weights_distribution_id = None
        self.set_kernel_weights_distribution(kernel_weights_distribution)

    def fit(self, x, y):
        self.kernels = generate_kernels(x.shape[-1], self.num_kernels, self.weights_distribution_id)
        features = apply_kernels(x, self.kernels)
        self.classifier.fit(features, y)
        return self

    def eval(self, x, y):
        features = apply_kernels(x, self.kernels)
        scores = self.classifier.score(features, y)
        return scores

    def set_kernel_weights_distribution(self, distribution_type):
        if distribution_type == 'normal':
            self.weights_distribution_id = 1
        elif distribution_type == 'uniform':
            self.weights_distribution_id = 2
        elif distribution_type == 'binary':
            self.weights_distribution_id = 3
        elif distribution_type == 'ternary':
            self.weights_distribution_id = 4
        else:
            raise Exception('YOUR DISTRIBUTION IS NOT SUPPORTED')
