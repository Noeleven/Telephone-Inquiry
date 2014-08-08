#创建数据库
drop database tps;
create database tps;
#创建登录用户表
use tps
create table tps_userlist(
ID int(11) not null primary key auto_increment,
username char(20) not null,
password char(30) not null,
name char(20) not null);
#创建成员信息表
create table tps_customerinfo(
ID int(11) not null primary key auto_increment,
name char(20),
mailaddr char(30),
Inum char(15),
Lnum char(64));
