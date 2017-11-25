# _*_coding=utf-8_*_
"""
#产生数据
x = np.linspace(-np.pi,np.pi,256,endpoint=True)
y_sin,y_cos = np.sin(x),np.cos(x)

#画背景
plt.figure(figsize=(8,6),dpi=80)
plt.title("simple wave graph")
plt.grid(True)

#X轴
plt.xlabel("axis X")
plt.xlim(-4.0,4.0)
plt.xticks(np.linspace(-4,4,9,endpoint=True))

#Y轴
plt.ylabel("axis Y")
plt.ylim(-1.0, 1.0)
plt.yticks(np.linspace(-1.0,1.0,9,endpoint=True))

#画波形
plt.plot(x,y_sin,"r--",linewidth=2.0,label="sin example")
plt.plot(x,y_cos,"b-",linewidth=2.0,label="cos example")

plt.legend(loc="upper left", shadow=True)
plt.show()
"""

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
def simple_advanced_plot():
    """
    simple advanced plot
    """
    # 生成测试数据
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    y_cos, y_sin = np.cos(x), np.sin(x)
    # 生成画布，并设置标题
    plt.figure(figsize=(8,6),dpi=80)
    plt.title("fuza wave graph")
    plt.grid(True)
    #画图的另外一种方式
    ax_1 = plt.subplot(111)
    ax_1.plot(x,y_cos,color="blue",linewidth=2.0,linestyle="--",label="left cos")
    ax_1.legend(loc="upper left", shadow=True)
    #设置Y轴（左边)
    ax_1.set_ylabel("left cos axis y")
    ax_1.set_ylim(-1.0,1.0)
    ax_1.set_yticks(np.linspace(-1,1,9,endpoint=True))

    ax_2 = plt.twinx()
    ax_2.plot(x,y_sin,color="red",linewidth=2.0,linestyle="-",label="right sin")
    ax_2.legend(loc="upper right", shadow=True)
    ax_2.set_ylabel("right sin axis y")
    ax_2.set_ylim(-2.0, 2.0)
    ax_2.set_yticks(np.linspace(-2,2,9,endpoint=True))

    ax_1.set_xlabel("axis x")
    ax_1.set_xlim(-4.0, 4.0)
    ax_1.set_xticks(np.linspace(-4,4,9,endpoint=True))

    plt.show()
    return
# simple_advanced_plot()

def subplot_plot():
    """
    subplot plot
    """
    # 子图的style列表
    style_list = ["r+-", "g*-", "b.--", "yo-"]

    # 依次画图
    for num in range(4):
        # 生成测试数据
        x = np.linspace(0.0, 2+num, num = 200)
        y = np.sin((5-num)*np.pi*x)
        # 子图的生成方式
        plt.subplot(2, 2, num+1)
        plt.title("sin%d*pi*x" % (5-num))
        plt.plot(x, y, style_list[num])

    #图形显示
    plt.show()
    return

simple_advanced_plot()
#subplot_plot()