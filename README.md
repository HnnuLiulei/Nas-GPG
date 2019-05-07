# Nas-GPG
基于GPG的简单数据备份方案

本文原创：淮南师范学院 刘磊
修改时间：2019.5.7

一、背景简介
作为一名负责单位信息化管理的运维管理人员，深知数据备份的重要，虽然一些核心系统上了本地备份+异地灾备，无论在安全还是稳定性都很成熟。但我还是一直在寻找一些较为“草根”的数据备份方案来满足一些特殊备份的需求，这种方案主要的特点：廉价、易部署、易管理、有一定的数据安全防护措施，对备份速率要求不是太高。得益于读了中国科学技术大学 张焕杰老师“从一个简单的备份需求演示GPG的使用”一文 链接地址：https://github.com/bg6cq/ITTS/blob/master/security/gpg/README.md?from=timeline，使得具备一定python和linux基础的我，可以利用GPG尝试去实现这样一种简单的数据发备份方案。 

二、技术需求
初级linux操作基础；
初级python基础；
了解非对称加密算法原理；
了解ftp服务器相关内容。

三、方案整体介绍
![image](https://github.com/HnnuLiulei/Nas-GPG/tree/master/img/frame.png)
