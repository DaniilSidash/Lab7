#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая считывает текст из файла и выводит на
# экран только предложения, не содержащие запятых.

if __name__ == '__main__':
    with open('sidash_1.txt', 'r') as f:
        text = f.read()

    offers = text.split('.')
    del offers[offers.index('')]

    print([offer for offer in offers if not "," in offer])
