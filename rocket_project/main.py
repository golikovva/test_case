from dataset import HamDataset
from model_processor import ModelProcessor
from model import ROCKET

train_set = HamDataset('./Ham/Ham_TRAIN.arff')
test_set = HamDataset('./Ham/Ham_TEST.arff')

model = ROCKET()

mp = ModelProcessor()
# Для каждого типа ядер посчитаем несколько запусков модели и представим результат с доверительными интервалами
for kernel_type in ['binary', 'ternary', 'normal', 'uniform']:
    model.set_kernel_weights_distribution(kernel_type)
    scores = mp.process_model(model,
                              train_dataset=train_set,
                              test_dataset=test_set,
                              num_runs=100)

    mp.show_results(scores, kernel_type)

# добавим результаты других методов для сравнения
mp.add_result_to_compare('ROCKET_orig', 0.7257)
mp.add_result_to_compare('ResNet', 0.7571)

# выводим все результаты в таблицу
results = mp.create_result_table()
print(results)
results.to_csv('./results.csv')

"""
Статистической разницы в зависимости от способа генераци весов ядер нет
Как правило mean(accuracy)+std(accuracy) = ROCKET original accuracy
"""


