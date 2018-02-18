CREATE DATABASE  IF NOT EXISTS `lab5_7` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `lab5_7`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: lab5_7
-- ------------------------------------------------------
-- Server version	5.7.18-log

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
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (433443,'dfdfddfdfd'),(2322,'233333'),(1,'Alex'),(3,'Alex'),(4,'Alex'),(6,'Alexandru'),(7,'Babybuff'),(8,'Babybuff'),(9,'Babybuff'),(10,'Babybuff'),(11,'Bir'),(12,'Bir'),(15,'Bir'),(16,'Bir'),(17,'Bir'),(18,'Bir'),(19,'Bir'),(20,'Bir'),(21,'Bir'),(22,'Bir'),(24,'Bir'),(25,'Bir'),(26,'Bir'),(27,'Bir'),(28,'Bir'),(29,'Bir'),(30,'Bir'),(31,'Bir'),(32,'Bir'),(33,'Bir'),(34,'Bir'),(35,'Bir'),(36,'Bir'),(37,'Bir'),(38,'Bir'),(39,'Bir'),(40,'Bir'),(42,'Bir'),(43,'Bir'),(44,'Bir'),(45,'Bir'),(46,'Bir'),(47,'Bir'),(48,'Bir'),(49,'Bir'),(50,'Bir'),(23,'Bogdan'),(13,'BirJHJH'),(5,'Alexandru'),(14,'Bir');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movie` (
  `id` int(11) NOT NULL,
  `title` varchar(45) NOT NULL,
  `description` varchar(45) NOT NULL,
  `genre` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES (2,'Film','un nooou film','action'),(3,'Film','un nooou film','action'),(4,'Film','un nooou film','action'),(5,'Film','un nooou film','action'),(6,'Film','un nooou film','action'),(7,'Film','un nooou film','action'),(8,'Film','BestMovieEvah','action'),(9,'Film','un nooou film','action'),(10,'Film','un nooou film','action'),(11,'Film','un nooou film','action'),(12,'Film','un nooou film','action'),(13,'Film','un nooou film','action'),(14,'Film','un nooou film','action'),(15,'Film','un nooou film','action'),(16,'Film','un nooou film','action'),(17,'Film','un nooou film','action'),(18,'Film','un nooou film','action'),(19,'Film','un nooou film','action'),(20,'Film','un nooou film','action'),(21,'Film','un nooou film','action'),(22,'Film','un nooou film','action'),(23,'Film','un nooou film','action'),(24,'Film','un nooou film','action'),(25,'Film','un nooou film','action'),(26,'Film','un nooou film','action'),(27,'Film','un nooou film','action'),(28,'Film','un nooou film','action'),(29,'Film','un nooou film','action'),(30,'Film','un nooou film','action'),(31,'Film','un nooou film','action'),(32,'Film','un nooou film','action'),(33,'Film','un nooou film','action'),(34,'Film','un nooou film','action'),(35,'Film','un nooou film','action'),(2222,'2dfdfdfd343434343434','3dfdfddf','action'),(2323,'act','sd','action'),(9888,'2322423','lapte1234','action'),(9999,'sdfs','sd','action'),(101010,'BestMovieEvah','bestMovieEvaaaah','action'),(232323,'sdfds','sdfsf','action');
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rental`
--

DROP TABLE IF EXISTS `rental`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rental` (
  `id` int(11) NOT NULL,
  `movieId` int(11) NOT NULL,
  `clientId` int(11) NOT NULL,
  `rentedDate` varchar(45) NOT NULL,
  `dueDate` varchar(45) NOT NULL,
  `returnedDate` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rental`
--

LOCK TABLES `rental` WRITE;
/*!40000 ALTER TABLE `rental` DISABLE KEYS */;
INSERT INTO `rental` VALUES (4,4,4,'2017-12-05','2017-12-20','-1'),(5,5,5,'2017-12-05','2017-12-20','-1'),(6,6,6,'2017-12-05','2017-12-20','2017-12-12'),(7,7,7,'2017-12-05','2017-12-20','2017-12-12'),(8,8,8,'2017-12-05','2017-12-20','-1'),(9,9,9,'2017-12-05','2017-12-20','2017-12-12'),(10,10,10,'2017-12-05','2017-12-20','-1'),(12,12,12,'2017-12-05','2017-12-20','-1'),(13,13,13,'2017-12-05','2017-12-20','-1');
/*!40000 ALTER TABLE `rental` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-18 20:06:58
