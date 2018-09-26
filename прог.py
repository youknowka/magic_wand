#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# импортируем модуль с математикой 
import math
# импортируем библиотеку NumPy для работы с матрицами
import numpy
# импорт библиотеки для визуализации полученных данных
import matplotlib.pyplot as mpp


if __name__=='__main__':
# задание значений аргумента от 0 до 200 с шагом 0.1
    arguments = numpy.r_[0:200:0.1]
# "рисование" графика заданной функции
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
    )
# показ полученного графика
    mpp.show()
# эта программа никак не называется