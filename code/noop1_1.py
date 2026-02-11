#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Pair:
    def __init__(self, first=0.0, second=0.0):
        if first > second:
            print("Ошибка: левая граница должна быть <= правой")
            exit()
        self.first = float(first)
        self.second = float(second)

    def read(self):
        self.first = float(input("Левая граница: "))
        self.second = float(input("Правая граница: "))
        if self.first > self.second:
            print("Ошибка: левая граница должна быть <= правой")
            exit()

    def display(self):
        print(f"[{self.first}, {self.second}]")

    def rangecheck(self, number):
        return self.first <= number <= self.second


def make_tim(first, second):
    if first > second:
        print("Ошибка: левая граница должна быть <= правой")
        exit()
    return Pair(first, second)


if __name__ == "__main__":
    print("\nСоздадим диапазон:")
    p2 = Pair()
    p2.read()
    print("Ваш диапазон: ", end="")
    p2.display()

    num = float(input("Проверить число: "))
    print(f"Число {num} в диапазоне? {p2.rangecheck(num)}")
