# Лабораторная работа 1 по дисциплине "Технологии программирования"

## Знакомство с системой контроля версий Git и инструментом CI/CD GitHub Actions

### Цель работы:
1. Познакомиться c распределенной системой контроля версий кода Git и ее функциями;
2. Познакомиться с понятиями «непрерывная интеграция» (CI) и «непрерывное развертывание»
(CD), определить их место в современной разработке программного обеспечения;
3. Получить навыки разработки ООП-программ и написания модульных тестов к ним на
современных языках программирования;
4. Получить навыки работы с системой Git для хранения и управления версиями ПО;
5. Получить навыки управления автоматизированным тестированием программного обеспечения,
расположенного в системе Git, с помощью инструмента GitHub Actions.

## Вариант 12
#### 1. Формат входного файла - Json
#### 2. Расчетная функция - Определить и вывести на экран студента, имеющего 90 баллов минимум по двум дисциплинам. Если таких студентов несколько, нужно вывести любого из них. Если таких студентов нет, необходимо вывести сообщение об их отсутствии.

## Краткое описание проекта

ериктория **data** хранит текстовые файлы в двух форматах .txt и .yaml, включающих список студентов и полученных ими оценок.

Дериктория **src** хранит файлы раасчетных функций, датаридеров и главной функции **main**.

Дериктория **test** хранит файлы для модульного тестирования функций из дериктории **src**.

Суть работы программы заключается в следующем: в зависимости от того какой текстовый файл 
считывает будет решаться разные задачи. При чтении .txt происходит расчет среднего балла студента, а при чтении .Json -
индивидуальное задание варианта 12.

Проект написан на языке программирования Python 3, модульное тестирование в нем
осуществляется с помощью библиотеки pytest. 

## UML-диаграмма классов
![image](https://github.com/vov459/PTLab1_/blob/main/UML.jpg?raw=true) 