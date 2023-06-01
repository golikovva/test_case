# Пошаговое описание запуска docker контейнера и скриптов в нём

1) Переходим в директорию с docker проектом

[comment]: <> (<tr>)

![plot](./readme_illustrations/1.jpg)

[comment]: <> (</tr>)

2) По инструкции из Dockerfile создаем образ. Назовем его test_image

[comment]: <> (<tr>)

![plot](./readme_illustrations/2.jpg)

[comment]: <> (</tr>)

Можно убедиться: образ создан

[comment]: <> (<tr>)

![plot](./readme_illustrations/3.jpg)

[comment]: <> (</tr>)

3) На основе созданного образа создаем и запускаем контейнер. Чтобы сразу в нем запустить скрипты, можно открыть контейнер в интерактивном режиме (-it). В созданном контейнере, командой ls убеждаемся, что скрипты и текстовый файл на месте 

[comment]: <> (<tr>)

![plot](./readme_illustrations/4.jpg)

[comment]: <> (</tr>)

4) Запускаем первый скрипт

[comment]: <> (<tr>)

![plot](./readme_illustrations/5.jpg)

[comment]: <> (</tr>)

5) Запускаем второй скрипт.

[comment]: <> (<tr>)

![plot](./readme_illustrations/6.jpg)

[comment]: <> (</tr>)

6) Убеждаемся что в той же директории появилось 10 файлов с названиями самых часто встречаемых слов в тексте

[comment]: <> (<tr>)

![plot](./readme_illustrations/6.jpg)

[comment]: <> (</tr>)



