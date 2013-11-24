-- MySQL dump 10.13  Distrib 5.6.13, for osx10.8 (x86_64)
--
-- Host: grant.rutgers.edu    Database: beer
-- ------------------------------------------------------
-- Server version	5.5.20

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
-- Table structure for table `bars`
-- DROP TABLE IF EXISTS `bars`; /*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bars` (
  `name` varchar(50) NOT NULL DEFAULT '',
  `license` varchar(7) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `phone` varchar(12) DEFAULT NULL,
  `addr` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Table structure for table `beers`
--

DROP TABLE IF EXISTS `beers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `beers` (
  `name` varchar(50) NOT NULL DEFAULT '',
  `manf` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Table structure for table `drinkers`
--

DROP TABLE IF EXISTS `drinkers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `drinkers` (
  `name` varchar(50) NOT NULL DEFAULT '',
  `city` varchar(50) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `addr` varchar(200) DEFAULT NULL,
  `profession` varchar(50) DEFAULT NULL,
  `age` INTEGER DEFAULT NULL,
  `income` INTEGER DEFAULT NULL,
  `gender` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Table structure for table `frequents`
--

DROP TABLE IF EXISTS `frequents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `frequents` (
  `drinker` varchar(50) NOT NULL DEFAULT '',
  `bar` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`drinker`,`bar`),
  KEY `fk_frequents_bar` (`bar`),
  CONSTRAINT `fk_frequents_bar` FOREIGN KEY (`bar`) REFERENCES `bars` (`name`),
  CONSTRAINT `fk_frequents_drinker` FOREIGN KEY (`drinker`) REFERENCES `drinkers` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frequents`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `likes` (
  `drinker` varchar(50) NOT NULL DEFAULT '',
  `beer` varchar(50) NOT NULL DEFAULT '',
  `rating` INTEGER DEFAULT NULL,
  PRIMARY KEY (`drinker`,`beer`),
  KEY `fk_likes_beer` (`beer`),
  CONSTRAINT `fk_likes_beer` FOREIGN KEY (`beer`) REFERENCES `beers` (`name`),
  CONSTRAINT `fk_likes_drinker` FOREIGN KEY (`drinker`) REFERENCES `drinkers` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--


--
-- Table structure for table `sells`
--

DROP TABLE IF EXISTS `sells`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sells` (
  `bar` varchar(50) NOT NULL DEFAULT '',
  `beer` varchar(50) NOT NULL DEFAULT '',
  `price` decimal(9,2) DEFAULT NULL,
  PRIMARY KEY (`bar`,`beer`),
  KEY `fk_sells_beer` (`beer`),
  CONSTRAINT `fk_sells_bar` FOREIGN KEY (`bar`) REFERENCES `bars` (`name`),
  CONSTRAINT `fk_sells_beer` FOREIGN KEY (`beer`) REFERENCES `beers` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sells`
--


DROP TABLE IF EXISTS `checkin`;
CREATE TABLE `checkin` (
    `bar` varchar(50) NOT NULL DEFAULT '',
    `drinker` varchar(50) NOT NULL DEFAULT '',
    `date` datetime NOT NULL,
    `rating` INTEGER DEFAULT NULL,
    PRIMARY KEY (`bar`, `drinker`, `date`),
    CONSTRAINT `fk_checkin_bar` FOREIGN KEY (`bar`) REFERENCES `bars` (`name`),
    CONSTRAINT `fk_checkin_drinker` FOREIGN KEY (`drinker`) REFERENCES `drinkers` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-09-12 15:56:04
