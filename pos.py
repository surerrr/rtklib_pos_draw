# -*- coding: utf-8 -*-
"""
Created  2019 9 20

@author  zhaoshuo

"""

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1

import numpy as np
import os


def plot_2D(path, i, name):

    a = np.loadtxt(path,str,skiprows=24)  # 获取txt str可以读字符串 跳过前24行

    e=a[:,2]
    n=a[:,3]
    u=a[:,4]

    epoch = e.size

    e = np.array(e, dtype='float_')
    n = np.array(n, dtype='float_')
    u = np.array(u, dtype='float_')

    av_e = np.mean(e)
    av_n = np.mean(n)
    av_u = np.mean(u)

    baseline = (av_n**2+av_e**2+av_u**2)**0.5

 #   print("平均值为=",av_e)

    e1 = e-av_e
    n1 = n-av_n
    u1 = u-av_u

    std_e = np.std(e1)
    std_n = np.std(n1)
    std_u = np.std(u1)

    var_e = np.var(e1) ** 0.5  # 标准差
    var_n = np.var(n1) ** 0.5  # 标准差

    scale_y = 400*max(var_e,var_n) # 刻度 四倍中误差

    if scale_y > 200:  # 最大不超过2m
        scale_y = 200

    epoch = e1.size
 #   print("历元数为=", epoch)

    lim1 = [10] * epoch
    lim2 = [-10] * epoch

    x = np.linspace(0, epoch, epoch)  # 0到24 分240份

    fig = plt.figure(i)

    fig.set_size_inches(8, 4)
    fig.subplots_adjust(left=0.1, bottom=0.2)  # 一些设置

    plt.plot(x, e1 * 100, "r.", label="dN"+" std="+str(round(std_e,3)))
    plt.plot(x, n1 * 100, "b.", label="dE"+" std="+str(round(std_n,3)))

    plt.plot(lim1, "m--")
    plt.plot(lim2, "m--")


    font2 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 15,
             }

    plt.ylabel("error of 2D/cm", font2)
    plt.xlabel("epoch", font2)
    plt.title(format("error of 2D"), font2)
    plt.ylim(-scale_y, scale_y)
    plt.legend()
    plt.grid("on")
    plt.savefig("error of 2D" +"("+str(round(baseline,1))+")"+ "{0}{1}.png".format(" ", name), dpi=300)


def plot_H(path, i, name):
    a = np.loadtxt(path, str, skiprows=24)  # 获取txt str可以读字符串 跳过前24行

    e = a[:, 2]
    n = a[:, 3]
    u = a[:, 4]

    epoch = e.size

    e = np.array(e, dtype='float_')
    n = np.array(n, dtype='float_')
    u = np.array(u, dtype='float_')

    av_e = np.mean(e)
    av_n = np.mean(n)
    av_u = np.mean(u)

    baseline = (av_n ** 2 + av_e ** 2 + av_u ** 2) ** 0.5

    u1 = u - av_u
    std_u = np.std(u1)

    var_u = np.var(u1)**0.5 # 标准差

    scale_y = 400 * var_u

    if scale_y > 200:
        scale_y = 200


    epoch = u1.size
    print("历元数为=", epoch)

    lim1 = [10] * epoch
    lim2 = [-10] * epoch

    x = np.linspace(0, epoch, epoch)  # 0到24 分240份

    fig1 = plt1.figure(i+1)

    fig1.set_size_inches(8, 4)
    fig1.subplots_adjust(left=0.1, bottom=0.2)  # 一些设置

    plt1.plot(x, u1 * 100, "g.", label="dU"+" std="+str(round(std_u,3)))  # alpha=0.2 透明度

    plt1.plot(lim1, "m--")
    plt1.plot(lim2, "m--")

    font2 = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 15,
             }

    plt1.ylabel("error of Elevation /cm", font2)
    plt1.xlabel("epoch", font2)
    plt1.title(format("error of Elevation"), font2)
    plt1.ylim(-scale_y, scale_y)
    plt1.legend()
    plt1.grid("on")
    plt1.savefig("error of Elevation" +"("+str(round(baseline,1))+")"+ "{0}{1}.png".format(" ", name), dpi=300)


if __name__ == '__main__':
    i = 0
    pathlist = os.listdir()
    for file in pathlist:
        if file.endswith(".pos"):
            print("开始绘制",file)
            name = file[0:9]  # 传进去文件名字
            plot_2D(file, i, name)  # 主函数调用
            plot_H(file, i, name)  # 主函数调用
            i = i + 2
