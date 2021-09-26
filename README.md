# WebTrOCR-开源的离线OCR  

## 介绍
WebTrOCR，基于开源项目 [Tr](https://github.com/myhub/tr) 
和https://github.com/alisen39/TrWebOCR 构建，使用的是tr的1.5版本，
可以完全离线，tr目前已经升级到2.3版本，不能完全离线。  
并且提供了易于使用的web页面，便于调试或日常使用。  
仅展示部分代码，如需全部代码，请联系Q2246187674


## 特性
* 中文识别  
快速高识别率
 
* 文字检测  
支持一定角度的旋转  

* 并发请求  
由于模型本身不支持并发，但通过tornado多进程的方式，能支持一定数量的并发请求。具体并发数取决于机器的配置。


## 安装需求  
 
### 运行平台  
* ✔ Python 3.6+  
* ✔ Ubuntu 16.04
* ✔ ️Ubuntu 18.04
* ✔ CentOS 7   
* ✔ Docker   

Windows和MacOS系统下可通过构建Docker镜像来使用，暂不支持直接部署使用  
其他Linux平台暂未测试，可自行安装测试  

### 最低配置要求  
* CPU:    1核  
* 内存:    2G  
* SWAP:   2G  

## 安装说明  
### 服务器部署
1. 安装python3.7  
    推荐使用miniconda
    
2. 执行install.py  
```
python install.py
```  

3. 安装依赖包  
``` shell script
pip install -r requirements.txt
```  

4. 运行  
``` shell script
python backend/main.py
```  

项目默认运行在8090端口，看到以下输出则代表运行成功：  
```shell script
# tr 1.5.0 https://github.com/myhub/tr
server is running: 0.0.0.0:8090
```  




## 效果展示  参考https://github.com/alisen39/TrWebOCR