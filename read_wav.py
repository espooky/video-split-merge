import numpy as np #载入numpy库
import matplotlib.pyplot as plt  #载入matplotlib库的pyplot模块
import wave #载入wave模块

f=wave.open(r'E:\abearing\rotor.wav','rb') #打开wav文件
nchannels,sampwidth,framerate,nframes=f.getparams()[:4] #获取wav文件的声道数，量化位数，采样率，总采样点

f.setpos(10*framerate) #定位采样点的开始位置，第10秒
s_data=f.readframes(20*framerate) #读取开始位置以后的采样点，后20秒
f.close()
w_data=np.fromstring(s_data,dtype=np.short) #将字符串转化为数值
w_data.shape=(-1,nchannels) #将一维数组转化为两列数组
time=np.arange(10*framerate,30*framerate)/framerate #定义时间点
plt.subplot(211) #子图1
plt.plot(time,w_data[:,0],c='blue')
plt.subplot(212) #子图2
plt.plot(time,w_data[:,1],c='green')
plt.xlabel('time(second)') #X轴的标签
