#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Dados que o programa irá informar
nome = raw_input()
salario_fixo = raw_input()
total_vendas = raw_input()
#Se fizer o float aqui, o programa fica mais rápido
salario_fixo = float(salario_fixo)
total_vendas = float(total_vendas)

salario = salario_fixo + (total_vendas*0.15)
print "TOTAL = R$ %.2f" % (salario)
