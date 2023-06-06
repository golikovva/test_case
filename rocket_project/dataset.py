import pandas as pd
import numpy as np
from scipy.io import arff


class HamDataset:
    def __init__(self, data_path):
        data_frame = pd.DataFrame(arff.loadarff(data_path)[0])
        self.data = data_frame.iloc[:, :-1].to_numpy()
        self.target = data_frame.iloc[:, -1].astype(int).to_numpy()

    def sample_bootstrap(self, sample_size):
        """
        Одним из способов оценивать доверительные интервалы модели является
        разбиение выборки на тренировочную и тестовую методом bootstrap
        Однако раз разбиение уже задано, менять его думаю неправильно,
        поэтому bootstrap-ом пользоваться не будем
        :param sample_size: размер bootstrap выборки
        :return: x, y - bootstrap. на них тренируемся
                 x, y - OOB. на них тестируемся
        """
        idxs = np.random.choice(len(self), sample_size)
        x_bootstrap = self.data[idxs]
        y_bootstrap = self.data[idxs]

        mask = np.ones(len(self), dtype=bool)
        mask[idxs] = False
        x_oob = self.data[mask]
        y_oob = self.data[mask]
        return x_bootstrap, y_bootstrap, x_oob, y_oob

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.target[idx]
