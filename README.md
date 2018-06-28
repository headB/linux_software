# linux_software
创建初始化的ubuntu使用！
1. VLC（播放器）
2. Typora（markdown）
3. shutter截图软件！附件形式
先装xxxcommonxx.deb,然后是libxxx.amd64...deb,然后是libxxxx-perl*.deb
4. 顶栏流量
indicator-sysmonitor
sudo add-apt-repository ppa:fossfreedom/indicator-sysmonitor  
sudo apt-get update  
sudo apt-get install indicator-sysmonitor  
5. 谷歌浏览器
##this is a setup to install chrome for ubuntu.!
sudo wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -
sudo apt-get update
sudo apt-get install google-chrome-stable
/usr/bin/google-chrome-stable
6. 搜狗输入法。
参照官方网站
7. ubuntu的阿里云加速
##this is for the lazy guy,why me write by english?because I have not a Chinese Input resoure!
sudo sed -i "s/http:\/\/archive.ubuntu.com\/ubuntu/http:\/\/mirrors.aliyun.com\/ubuntu/g" /etc/apt/sources.list
sudo sed -i "s/http:\/\/security.ubuntu.com\/ubuntu/http:\/\/mirrors.aliyun.com\/ubuntu/g" /etc/apt/sources.list
sudo sed -i "s/http:\/\/cn.archive.ubuntu.com\/ubuntu/http:\/\/mirrors.aliyun.com\/ubuntu/g" /etc/apt/sources.list
8. wps
