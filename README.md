# Nas-GPG
基于GPG的简单数据备份方案
====
本文原创：淮南师范学院 刘磊<br>
修改时间：2019.5.7<br>

## 一、背景简介
作为一名负责单位信息化管理的运维管理人员，深知数据备份的重要，虽然一些核心系统上了本地备份+异地灾备，无论在安全还是稳定性都很成熟。但我还是一直在寻找一些较为“草根”的数据备份方案来满足一些特殊备份的需求，这种方案主要的特点：廉价、易部署、易管理、有一定的数据安全防护措施，对备份速率要求不是太高。得益于读了中国科学技术大学 张焕杰老师“从一个简单的备份需求演示GPG的使用”一文，使得具备一定python和linux基础的我，可以利用GPG尝试去实现这样一种简单的数据发备份方案。上文链接地址：https://github.com/bg6cq/ITTS/blob/master/security/gpg/README.md?from=timeline  

## 二、技术需求
* 初级linux操作基础
* 初级python基础（pyhton版本为3.5）
* 了解非对称加密算法原理
* 了解ftp服务器相关内容

## 三、方案整体设计
![image](https://github.com/HnnuLiulei/Nas-GPG/blob/master/img/frame.png) <br>
如图，整个方案主要分为客户机和备份服务器两部分，客户机负责配置加解密环境，加解密数据由python编写的GPG加解密模块处理，数据备份由python编写的ftp管理模块处理；备份服务器则负责存储管理已加密的数据。其中，客户机（Ubuntu）上需要安装好gpg软件，即配置好加解密所需要的环境，每一台客户机都需要配置这样的环境，具体步骤见上文链接内容。安装好后需要记录好密码仓库路径及保存好自己的私钥和私钥保护密码，这里的密码仓库路径和私钥保护密码将在GPG加加解密模块中使用到；备份服务器由树莓派（一种卡片式微型计算机）挂载多块存储盘构成，树莓派上搭载的是linux操作系统，在其上主要部署了ftp服务，用来满足远程数据备份需求。这种采用树莓派作为备份服务器的方案虽然在性能上无法与专业备份服务器相比，但作为“草根”方案的替代选择，其数据处理及传输效率还是能够满足一定需求的。（最主要是便宜，硬件投入：一个树莓派300元，10T的存储盘费用大约1500元，加上其余零碎总共不超过2000元）<br>

## 四、具体实现
### 4.1、客户机端
首先要在客户机上已经成功安装gpg软件，并且已经成功导入公钥pub和私钥sec。
#### 4.1.1 GPG加解密模块
需要安装python对应模块为python-gnupg，具体设置详细代码见加密模块文件gpg_encrypt.py和解密模块文件gpg_decrypt.py，请根据情况进行内容替换。 <br>
这部分内容参考了网上的一篇博文，里面介绍了gnupg可用于加解密、数字签名等方面，本文只用到了数据加解密内容。原文链接地址https://cloud.tencent.com/developer/article/1176041 <br>
#### 4.1.2 ftp数据备份
需要安装python对应模块为python-ftplib，具体设置详细代码见Ftp管理模块ftp.py，请根据情况进行内容替换。 <br>
未完待续。。。
