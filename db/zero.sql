-- MySQL dump 10.13  Distrib 5.5.34, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: tps
-- ------------------------------------------------------
-- Server version	5.5.34-0ubuntu0.12.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tps_customerinfo`
--

DROP TABLE IF EXISTS `tps_customerinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tps_customerinfo` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(20) DEFAULT NULL,
  `Inum` char(64) DEFAULT NULL,
  `Lnum` char(15) DEFAULT NULL,
  `mailaddr` char(30) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tps_customerinfo`
--

LOCK TABLES `tps_customerinfo` WRITE;
/*!40000 ALTER TABLE `tps_customerinfo` DISABLE KEYS */;
INSERT INTO `tps_customerinfo` VALUES (1,'马泽华','18721696742','842','mazh@iceflow.cn'),(2,'张强','13621998464,18918363268','843','zhangqiang@iceflow.cn'),(3,'葛艳萍','18918363261','861','geyp@iceflow.cn'),(4,'陆沙舟','18918363256','876','lusz@iceflow.cn'),(6,'陈先哲','13916541465','888','chenxz@iceflow.cn'),(7,'周永','13501820478\r\n13501820478\r\n13501820478\r\n13501820478\r\n13501820478\r','886','zhouyong@iceflow.cn'),(8,'邓莹',NULL,'800','dengy@iceflow.cn'),(9,'董树凯','18762320120',NULL,'dongsk@iceflow.cn'),(10,'谢海凤','18096645868',NULL,'xiehf@iceflow.cn'),(11,'杨海刚','18918363277','882','yanghg@iceflow.cn'),(12,'邱燕','18918363271','846','qiuyan@iceflow.cn'),(13,'蒋冬','18918363253,15821260367','881','jiangdong@iceflow.cn'),(14,'韦红兵','18918363272','139','weihb@iceflow.cn'),(15,'黄毓俊','15618677067','857','huangyj@iceflow.cn'),(16,'周文均','18918363259','870','zhouwj@iceflow.cn'),(17,'杜一夫','18918363265','869','duyf@iceflow.cn'),(18,'殷作亮','18918363252','872','yinzl@iceflow.cn'),(19,'刘爱奎','18918363267,15618646989','868','liuak@iceflow.cn'),(20,'胡建','18918363276','875','hujian@iceflow.cn'),(21,'韩天斌','13166360099','866','hantb@iceflow.cn'),(22,'龚霄云','13381928287','851','gongxy@iceflow.cn');
/*!40000 ALTER TABLE `tps_customerinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tps_userlist`
--

DROP TABLE IF EXISTS `tps_userlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tps_userlist` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `username` char(20) DEFAULT NULL,
  `name` char(20) DEFAULT NULL,
  `password` char(30) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tps_userlist`
--

LOCK TABLES `tps_userlist` WRITE;
/*!40000 ALTER TABLE `tps_userlist` DISABLE KEYS */;
INSERT INTO `tps_userlist` VALUES (1,'mazh','马泽华','iceflow'),(2,'dongsk','董树凯','iceflow'),(3,'zhangq','张强','iceflow'),(4,'duyf','杜一夫','iceflow'),(5,'yinzl','殷作亮','iceflow'),(6,'hujian','胡建','iceflow'),(7,'liuak','刘爱奎','iceflow'),(8,'lusz','陆沙舟','iceflow'),(9,'zhouwj','周文均','iceflow'),(10,'huangyj','黄毓俊','iceflow'),(11,'dengying','邓莹','iceflow'),(12,'weihb','韦红兵','iceflow'),(13,'jiangdong','蒋冬','iceflow'),(14,'qiuyan','邱燕','iceflow'),(15,'yanghg','杨海刚','iceflow'),(16,'xiehf','谢海凤','iceflow'),(17,'chenxz','陈先哲','iceflow'),(18,'geyp','葛艳萍','iceflow'),(19,'zhouyong','周永','iceflow'),(20,'gongxy','龚霄云','iceflow'),(21,'hantb','韩天斌','iceflow');
/*!40000 ALTER TABLE `tps_userlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-06-23 13:37:08
