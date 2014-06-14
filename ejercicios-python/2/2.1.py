# -*- encoding:utf-8 -*-

c = input("cantidad ")
x = input("tasa de interes ")
n = input("numero de años ")

cn = c * (1 + float(x)/100)**n

print cn
