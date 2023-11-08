# Проект 4. Диплом. Прогнозирование курсов валют и акций

## Оглавление  
[1. Цель и задачи проекта](https://github.com/V3ence/DS_education/blob/main/project_4/README.md#Описание-проекта)  
[2. Краткая информация о данных](https://github.com/V3ence/DS_education/blob/main/project_4/README.md#%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[3. Этапы работы над проектом](https://github.com/V3ence/DS_education/blob/main/project_4/README.md#Этапы-работы-над-проектом)  
[4. Результат](https://github.com/V3ence/DS_education/blob/main/project_4/README.md#Результаты)    
[5. Выводы](https://github.com/V3ence/DS_education/blob/main/project_4/README.md#Выводы)   


### Цель и задачи проекта.    
Выявить возможность прогнозирования курсов валют и акций с помощью различных существующих методов построения моделей прогнозирования, от простых к более сложным.

:arrow_up:[к оглавлению](https://github.com/V3ence/DS_education/blob/main/project_4/README.md#Оглавление)


### Краткая информация о данных
Данные для прогнозирования представляют собой ежедневные курсы валют и акций с сайта finance.yahoo.com. Дополнительные экзогенные данные по важным экономическим событиям взяты с сайта tradingview.com

:arrow_up:[к оглавлению](https://github.com/V3ence/DS_education/blob/main/project_4/README.md#Оглавление)

### Этапы работы над проектом
1. Загрузка необходимых библиотек и наших эндогенных данных.
2. Изучение данных.
3. Обработка данных и дальнейшее их изучение.
4. Создание моделей прогнозирования
4.1. Экспоненциальное сглаживание.
4.2. Авторегрессия
4.3. Авторегрессия со скользящей средней
4.4. Авторегрессия со скользящей средней и сезонной составляющей
4.5. Авторегрессия со скользящей средней, сезонной составляющей и экзогенными данными
4.6 Нейронная сеть LSTM

:arrow_up:[к оглавлению](https://github.com/V3ence/DS_education/blob/main/project_4/README.md#Оглавление)

### Результаты:  
- [Ноутбук на GitHub](https://github.com/V3ence/DS_education/blob/main/project_4/diploma.ipynb)


:arrow_up:[к оглавлению](https://github.com/V3ence/DS_education/blob/main/project_4/README.md#Оглавление)

### Выводы: 
Лучший результат с минимальной среднеквадратичной ошибкой RMSE=0.004 продемонстрировала модель нейронных сетей LSTM

:arrow_up:[к оглавлению](https://github.com/V3ence/DS_education/blob/main/project_4/README.md#Оглавление)
