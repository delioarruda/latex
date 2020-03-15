# -*- coding: utf-8 -*-
#import csv
import os
import sys
import pandas as pd
import locale
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

def draw_plots(arq):
    locale.setlocale(locale.LC_NUMERIC, "pt_BR.UTF-8")

    df = pd.read_csv(arq, sep=';', index_col=0)
    df = df.applymap(lambda x: '0' if x in ['-'] else x)
    df = df.applymap(locale.atof)

    medias = df.mean(axis=0)

    plt.figure(1)
    plt.hist(df.values[:,0])
    plt.axhline(medias[0], linewidth=4, color='r')
    plt.savefig('prova1.png')
    #plt.show()

    plt.figure(2)
    plt.hist(df.values[:,1])
    plt.axhline(medias[1], linewidth=4, color='r')
    plt.savefig('prova2.png')
    #plt.show()

    plt.figure(3)
    plt.hist(df.values[:,2])
    plt.axhline(medias[2], linewidth=4, color='r')
    plt.savefig('prova3.png')
    #plt.show()

    #return df.

def write_texfile():
    
    # Escrever o resultado em um arquivo .tex
    results = open('relatorio.tex','w')
    print >>results, '\\documentclass{article}'
    print >>results, '\\usepackage{calc}'
    print >>results, '\\usepackage{ifthen}'
    print >>results, '\\usepackage{tikz}'
    print >>results, '\\usepackage[utf8]{inputenc}'
    print >>results, '\\usepackage[T1]{fontenc}'
    print >>results, '\\usepackage{txfonts}'
    print >>results, '\\title{Relatório de Notas de Cálculo A\\\\Semestre 2016.1}'
    print >>results, '\\author{Melissa Weber Mendonça}'
    print >>results, '\\date{Sábado, 16 de maio de 2016}'
    print >>results, '\\begin{document}'
    print >>results, '\\maketitle'
    print >>results, '\\section*{Distribuição de Notas}'
    #print >>results, '\\
    print >>results, '\\begin{figure}[ht]'
    print >>results, '\\begin{center}'
    print >>results, '\\includegraphics[width=5cm]{prova1.png}'
    print >>results, '\\end{center}'
    print >>results, '\\caption{Notas da Prova 1.}'
    print >>results, '\\end{figure}'
    print >>results, '\\begin{figure}[ht]'
    print >>results, '\\begin{center}'
    print >>results, '\\includegraphics[width=5cm]{prova2.png}'
    print >>results, '\\end{center}'
    print >>results, '\\caption{Notas da Prova 2.}'
    print >>results, '\\end{figure}'
    print >>results, '\\begin{figure}[ht]'
    print >>results, '\\begin{center}'
    print >>results, '\\includegraphics[width=5cm]{prova3.png}'
    print >>results, '\\end{center}'
    print >>results, '\\caption{Notas da Prova 3.}'
    print >>results, '\\end{figure}'
    print >>results, '\\end{document}'
    results.close()
    # Compilar e mostrar o pdf resultante.
    try:
        os.system('pdflatex relatorio.tex')
    except OSError:
        print('LaTeX not installed.')
    os.system('xdg-open relatorio.pdf &')

if __name__ == '__main__':
    draw_plots('notas.csv')
    write_texfile()
