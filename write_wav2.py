import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig #载入scipy库的signal模块

framerate=44100 #采样率为44100
time=10 #wav声音时长为10秒
t=np.arange(0,time,1/framerate) #定义时间点
w_data=sig.chirp(t,100,time,1000,method='linear')*1000  #生成线性扫频信号，从100Hz到1000Hz
w_data=w_data.astype(np.short) #浮点型数组转换为整型数组

f=wave.open(r'E:\abearing\sweep.wav','wb') #打开wav声音文件
f.setnchannels(1) #定义声道数为1
f.setsampwidth(3) #定义量化位数 3*8=24
f.setframerate(framerate) #定义采样率
f.writeframes(w_data.tostring()) #写入wav声音文件
f.close()

