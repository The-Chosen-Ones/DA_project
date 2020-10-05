-- MySQL dump 10.13  Distrib 8.0.21, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: DfOEP
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ACCOUNT`
--

DROP TABLE IF EXISTS `ACCOUNT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ACCOUNT` (
  `Email_id` varchar(255) NOT NULL,
  `First_name` varchar(255) NOT NULL,
  `Family_name` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Mobile` char(10) NOT NULL,
  `Sex` varchar(10) NOT NULL,
  PRIMARY KEY (`Email_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ACCOUNT`
--

LOCK TABLES `ACCOUNT` WRITE;
/*!40000 ALTER TABLE `ACCOUNT` DISABLE KEYS */;
INSERT INTO `ACCOUNT` VALUES ('ahmad@mail.com','Ahmad','Jabbar','passahma','9827781009','M'),('alecia@mail.com','Alecia','Zeleya','passalec','2123456789','F'),('fank@mail.com','Franklin','Wong','passfran','2023456789','M'),('james@mail.com','James','Borge','passjame','9827781000','M'),('jennifer@mail.com','Jennifer','Wallace','passjenn','2123456009','F'),('joe@mail.com','Joe','Cook','passjoec','9827701000','M'),('john@mail.com','John','Smith','passjohn','1023456789','M'),('joyce@mail.com','Joyce','English','passjoyc','9823334009','F'),('profDA101@mail.com','William','Shaw','passwill','9827701410','M'),('ramesh@mail.com','Ramesh','Narayan','passrame','2123334009','M'),('steve@mail.com','Steve','Gates','passstev','9827701010','M'),('ta_1DA101@mail.com','Sheldon','Cooper','passshel','9817701410','M'),('ta_2DA101@mail.com','Lilly','','passshel','9817703310','F');
/*!40000 ALTER TABLE `ACCOUNT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ADDRESS`
--

DROP TABLE IF EXISTS `ADDRESS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ADDRESS` (
  `Email_id` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  PRIMARY KEY (`Email_id`,`Address`),
  CONSTRAINT `ADDRESS_ibfk_1` FOREIGN KEY (`Email_id`) REFERENCES `ACCOUNT` (`Email_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ADDRESS`
--

LOCK TABLES `ADDRESS` WRITE;
/*!40000 ALTER TABLE `ADDRESS` DISABLE KEYS */;
INSERT INTO `ADDRESS` VALUES ('ahmad@mail.com','Dallas, Houston, TX'),('ahmad@mail.com','room 139'),('alecia@mail.com','pinto road, state abc'),('alecia@mail.com','room 919'),('fank@mail.com','city qwerty, state abc'),('fank@mail.com','room 119'),('james@mail.com','room 131'),('james@mail.com','Stone, Houston, TX'),('jennifer@mail.com','Berry, Bellaire, TX'),('jennifer@mail.com','room 919'),('joe@mail.com','room 131'),('joe@mail.com','Stair, Houston, TX'),('john@mail.com','city xyz, state abc'),('john@mail.com','room 109'),('joyce@mail.com','Rice, Houston, TX'),('joyce@mail.com','room 939'),('profDA101@mail.com','Flat 134, TX'),('ramesh@mail.com','FireOak, Humble, TX'),('ramesh@mail.com','room 129'),('steve@mail.com','room 134'),('steve@mail.com','Will road, CA'),('ta_1DA101@mail.com','Flat D4, CA'),('ta_2DA101@mail.com','Room 923, CA');
/*!40000 ALTER TABLE `ADDRESS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ATTENDS`
--

DROP TABLE IF EXISTS `ATTENDS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ATTENDS` (
  `Team_name` varchar(255) NOT NULL,
  `Channel_name` varchar(255) NOT NULL,
  `Org_id` varchar(255) NOT NULL,
  `SRoll_no` int NOT NULL,
  `Start_time` datetime NOT NULL,
  PRIMARY KEY (`Team_name`,`Channel_name`,`Org_id`,`SRoll_no`,`Start_time`),
  KEY `Team_name` (`Team_name`,`Channel_name`,`Org_id`,`Start_time`),
  KEY `SRoll_no` (`SRoll_no`),
  CONSTRAINT `ATTENDS_ibfk_2` FOREIGN KEY (`Team_name`, `Channel_name`, `Org_id`, `Start_time`) REFERENCES `MEETING` (`Team_name`, `Channel_name`, `Org_id`, `Start_time`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ATTENDS_ibfk_3` FOREIGN KEY (`SRoll_no`) REFERENCES `STUDENT` (`Roll_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ATTENDS`
--

LOCK TABLES `ATTENDS` WRITE;
/*!40000 ALTER TABLE `ATTENDS` DISABLE KEYS */;
INSERT INTO `ATTENDS` VALUES ('Data_Analysis','General','profDA101@mail.com',1010202030,'2020-10-05 11:00:00'),('Data_Analysis','Tutorials','ta_1DA101@mail.com',1010202030,'2020-10-09 13:00:00'),('Data_Analysis','Tutorials','ta_2DA101@mail.com',1010202030,'2020-10-02 13:00:00'),('Data_Analysis','General','profDA101@mail.com',1010202040,'2020-10-01 11:00:00'),('Data_Analysis','General','profDA101@mail.com',1010202040,'2020-10-03 11:00:00'),('Data_Analysis','General','profDA101@mail.com',1010202040,'2020-10-05 11:00:00'),('Data_Analysis','Tutorials','ta_1DA101@mail.com',1010202040,'2020-10-09 13:00:00'),('Data_Analysis','Tutorials','ta_2DA101@mail.com',1010202040,'2020-10-02 13:00:00'),('Data_Analysis','General','profDA101@mail.com',1010404040,'2020-10-03 11:00:00'),('Data_Analysis','Tutorials','ta_1DA101@mail.com',1010404040,'2020-10-09 13:00:00'),('Data_Analysis','General','profDA101@mail.com',1010604040,'2020-10-01 11:00:00'),('Data_Analysis','General','profDA101@mail.com',1010604940,'2020-10-01 11:00:00'),('Data_Analysis','General','profDA101@mail.com',1010604940,'2020-10-03 11:00:00'),('Data_Analysis','General','profDA101@mail.com',1010604940,'2020-10-05 11:00:00'),('Data_Analysis','Tutorials','ta_1DA101@mail.com',1010604940,'2020-10-09 13:00:00'),('Data_Analysis','Tutorials','ta_2DA101@mail.com',1010604940,'2020-10-02 13:00:00'),('Data_Analysis','General','profDA101@mail.com',1010604943,'2020-10-01 11:00:00'),('Data_Analysis','General','profDA101@mail.com',1010604943,'2020-10-03 11:00:00'),('Data_Analysis','General','profDA101@mail.com',1010604943,'2020-10-05 11:00:00'),('Data_Analysis','Tutorials','ta_2DA101@mail.com',1010604943,'2020-10-02 13:00:00'),('Data_Analysis','General','profDA101@mail.com',1010605043,'2020-10-03 11:00:00'),('Data_Analysis','General','profDA101@mail.com',1010605043,'2020-10-05 11:00:00'),('Data_Analysis','Tutorials','ta_1DA101@mail.com',1010605143,'2020-10-09 13:00:00'),('Data_Analysis','Tutorials','ta_2DA101@mail.com',1010605143,'2020-10-02 13:00:00'),('Data_Analysis','General','profDA101@mail.com',1020402040,'2020-10-01 11:00:00'),('Data_Analysis','General','profDA101@mail.com',1020402040,'2020-10-03 11:00:00'),('Data_Analysis','General','profDA101@mail.com',1020402040,'2020-10-05 11:00:00'),('Data_Analysis','Tutorials','ta_1DA101@mail.com',1020402040,'2020-10-09 13:00:00'),('Data_Analysis','Tutorials','ta_2DA101@mail.com',1020402040,'2020-10-02 13:00:00'),('Data_Analysis','General','profDA101@mail.com',1020404040,'2020-10-01 11:00:00'),('Data_Analysis','General','profDA101@mail.com',1020404040,'2020-10-05 11:00:00');
/*!40000 ALTER TABLE `ATTENDS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CHANNEL`
--

DROP TABLE IF EXISTS `CHANNEL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CHANNEL` (
  `Team_name` varchar(255) NOT NULL,
  `Channel_name` varchar(255) NOT NULL,
  PRIMARY KEY (`Team_name`,`Channel_name`),
  CONSTRAINT `CHANNEL_ibfk_1` FOREIGN KEY (`Team_name`) REFERENCES `TEAM` (`Team_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CHANNEL`
--

LOCK TABLES `CHANNEL` WRITE;
/*!40000 ALTER TABLE `CHANNEL` DISABLE KEYS */;
INSERT INTO `CHANNEL` VALUES ('Data_Analysis','General'),('Data_Analysis','Tutorials');
/*!40000 ALTER TABLE `CHANNEL` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DEGREE`
--

DROP TABLE IF EXISTS `DEGREE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DEGREE` (
  `Email_id` varchar(255) NOT NULL,
  `Degree` varchar(255) NOT NULL,
  PRIMARY KEY (`Email_id`,`Degree`),
  CONSTRAINT `DEGREE_ibfk_1` FOREIGN KEY (`Email_id`) REFERENCES `INSTRUCTOR` (`Email_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DEGREE`
--

LOCK TABLES `DEGREE` WRITE;
/*!40000 ALTER TABLE `DEGREE` DISABLE KEYS */;
INSERT INTO `DEGREE` VALUES ('profDA101@mail.com','Btech'),('profDA101@mail.com','Mtech'),('profDA101@mail.com','Phd'),('ta_1DA101@mail.com','Btech'),('ta_2DA101@mail.com','Btech');
/*!40000 ALTER TABLE `DEGREE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GIVES`
--

DROP TABLE IF EXISTS `GIVES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `GIVES` (
  `SRoll_no` int NOT NULL,
  `Quiz_no` int NOT NULL,
  `Course_name` varchar(255) NOT NULL,
  PRIMARY KEY (`SRoll_no`,`Quiz_no`,`Course_name`),
  KEY `Quiz_no` (`Quiz_no`,`Course_name`),
  CONSTRAINT `GIVES_ibfk_1` FOREIGN KEY (`Quiz_no`, `Course_name`) REFERENCES `QUIZ` (`Quiz_no`, `Course_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `GIVES_ibfk_2` FOREIGN KEY (`SRoll_no`) REFERENCES `STUDENT` (`Roll_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GIVES`
--

LOCK TABLES `GIVES` WRITE;
/*!40000 ALTER TABLE `GIVES` DISABLE KEYS */;
/*!40000 ALTER TABLE `GIVES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `INSTRUCTOR`
--

DROP TABLE IF EXISTS `INSTRUCTOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `INSTRUCTOR` (
  `Email_id` varchar(255) NOT NULL,
  `Sup_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Email_id`),
  CONSTRAINT `INSTRUCTOR_ibfk_1` FOREIGN KEY (`Email_id`) REFERENCES `ACCOUNT` (`Email_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `INSTRUCTOR`
--

LOCK TABLES `INSTRUCTOR` WRITE;
/*!40000 ALTER TABLE `INSTRUCTOR` DISABLE KEYS */;
INSERT INTO `INSTRUCTOR` VALUES ('profDA101@mail.com','profDA101@mail.com'),('ta_1DA101@mail.com','profDA101@mail.com'),('ta_2DA101@mail.com','profDA101@mail.com');
/*!40000 ALTER TABLE `INSTRUCTOR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MEETING`
--

DROP TABLE IF EXISTS `MEETING`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MEETING` (
  `Team_name` varchar(255) NOT NULL,
  `Channel_name` varchar(255) NOT NULL,
  `Org_id` varchar(255) NOT NULL,
  `Start_time` datetime NOT NULL,
  `End_time` datetime NOT NULL,
  PRIMARY KEY (`Team_name`,`Channel_name`,`Org_id`,`Start_time`),
  KEY `Org_id` (`Org_id`),
  CONSTRAINT `MEETING_ibfk_1` FOREIGN KEY (`Team_name`, `Channel_name`) REFERENCES `CHANNEL` (`Team_name`, `Channel_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `MEETING_ibfk_2` FOREIGN KEY (`Org_id`) REFERENCES `INSTRUCTOR` (`Email_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MEETING`
--

LOCK TABLES `MEETING` WRITE;
/*!40000 ALTER TABLE `MEETING` DISABLE KEYS */;
INSERT INTO `MEETING` VALUES ('Data_Analysis','General','profDA101@mail.com','2020-10-01 11:00:00','2020-10-01 12:00:00'),('Data_Analysis','General','profDA101@mail.com','2020-10-03 11:00:00','2020-10-03 12:00:00'),('Data_Analysis','General','profDA101@mail.com','2020-10-05 11:00:00','2020-10-05 12:00:00'),('Data_Analysis','Tutorials','ta_1DA101@mail.com','2020-10-09 13:00:00','2020-10-09 14:30:00'),('Data_Analysis','Tutorials','ta_2DA101@mail.com','2020-10-02 13:00:00','2020-10-02 14:30:00');
/*!40000 ALTER TABLE `MEETING` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MEMBERSHIP`
--

DROP TABLE IF EXISTS `MEMBERSHIP`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `MEMBERSHIP` (
  `Team_name` varchar(255) NOT NULL,
  `Member_id` varchar(255) NOT NULL,
  PRIMARY KEY (`Team_name`,`Member_id`),
  KEY `Member_id` (`Member_id`),
  CONSTRAINT `MEMBERSHIP_ibfk_1` FOREIGN KEY (`Member_id`) REFERENCES `ACCOUNT` (`Email_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `MEMBERSHIP_ibfk_2` FOREIGN KEY (`Team_name`) REFERENCES `TEAM` (`Team_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MEMBERSHIP`
--

LOCK TABLES `MEMBERSHIP` WRITE;
/*!40000 ALTER TABLE `MEMBERSHIP` DISABLE KEYS */;
INSERT INTO `MEMBERSHIP` VALUES ('Data_Analysis','ahmad@mail.com'),('Data_Analysis','alecia@mail.com'),('Data_Analysis','fank@mail.com'),('Data_Analysis','james@mail.com'),('Data_Analysis','jennifer@mail.com'),('Data_Analysis','joe@mail.com'),('Data_Analysis','john@mail.com'),('Data_Analysis','joyce@mail.com'),('Data_Analysis','ramesh@mail.com'),('Data_Analysis','steve@mail.com');
/*!40000 ALTER TABLE `MEMBERSHIP` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `QUESANS`
--

DROP TABLE IF EXISTS `QUESANS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `QUESANS` (
  `Q_id` int NOT NULL,
  `Answer` varchar(255) NOT NULL,
  `Marks` int NOT NULL,
  PRIMARY KEY (`Q_id`,`Answer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `QUESANS`
--

LOCK TABLES `QUESANS` WRITE;
/*!40000 ALTER TABLE `QUESANS` DISABLE KEYS */;
INSERT INTO `QUESANS` VALUES (1,'Structured Query Language',10),(2,'Data and analysis',10),(3,'Data and analysis',10),(4,'pymysql',10),(5,'4nf',0),(5,'bcnf',10),(6,'can be',10),(7,'no',0),(7,'yes',10),(8,'no',10),(8,'yes',0),(9,'tuples',0),(10,'no',10),(11,'no',10),(12,'yes',10),(13,'no',10);
/*!40000 ALTER TABLE `QUESANS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `QUESTION`
--

DROP TABLE IF EXISTS `QUESTION`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `QUESTION` (
  `Q_id` int NOT NULL,
  `Qn_text` mediumtext NOT NULL,
  `Course_name` varchar(255) NOT NULL,
  PRIMARY KEY (`Q_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `QUESTION`
--

LOCK TABLES `QUESTION` WRITE;
/*!40000 ALTER TABLE `QUESTION` DISABLE KEYS */;
INSERT INTO `QUESTION` VALUES (1,'SQL full form','CS.301.2020'),(2,'DA full form','CS.301.2020'),(3,'DnA full form','CS.301.2020'),(4,'library to use SQL in python','CS.301.2020'),(5,'Normaliation done after 3NF','CS.301.2020'),(6,'is super key a key','CS.301.2020'),(7,'is key a super key','CS.301.2020'),(8,'can null be a key','CS.301.2020'),(9,'rows are also called __?','CS.301.2020'),(10,'is order of rows fixed in relational model?','CS.301.2020'),(11,'is order of columns fixed in relational model?','CS.301.2020'),(12,'Cartesian product may not produce null set. is it right?','CS.301.2020'),(13,'Cartesian product can not produce null set. is it right?','CS.301.2020');
/*!40000 ALTER TABLE `QUESTION` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `QUIZ`
--

DROP TABLE IF EXISTS `QUIZ`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `QUIZ` (
  `Quiz_no` int NOT NULL,
  `Course_name` varchar(255) NOT NULL,
  `No_of_qn` int NOT NULL,
  PRIMARY KEY (`Quiz_no`,`Course_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `QUIZ`
--

LOCK TABLES `QUIZ` WRITE;
/*!40000 ALTER TABLE `QUIZ` DISABLE KEYS */;
INSERT INTO `QUIZ` VALUES (1,'CS.301.2020',5);
/*!40000 ALTER TABLE `QUIZ` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RESPONSE`
--

DROP TABLE IF EXISTS `RESPONSE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RESPONSE` (
  `Quiz_no` int NOT NULL,
  `Course_name` varchar(255) NOT NULL,
  `Q_id` int NOT NULL,
  `SRoll_no` int NOT NULL,
  `Inst_Email_id` varchar(255) NOT NULL,
  `Answer` varchar(255) NOT NULL,
  PRIMARY KEY (`Quiz_no`,`Course_name`,`Q_id`,`SRoll_no`,`Inst_Email_id`),
  KEY `SRoll_no` (`SRoll_no`),
  KEY `Inst_Email_id` (`Inst_Email_id`),
  KEY `Q_id` (`Q_id`,`Answer`),
  CONSTRAINT `RESPONSE_ibfk_1` FOREIGN KEY (`Q_id`) REFERENCES `QUESTION` (`Q_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `RESPONSE_ibfk_2` FOREIGN KEY (`SRoll_no`) REFERENCES `STUDENT` (`Roll_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `RESPONSE_ibfk_3` FOREIGN KEY (`Inst_Email_id`) REFERENCES `INSTRUCTOR` (`Email_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `RESPONSE_ibfk_5` FOREIGN KEY (`Quiz_no`, `Course_name`) REFERENCES `QUIZ` (`Quiz_no`, `Course_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `RESPONSE_ibfk_6` FOREIGN KEY (`Q_id`, `Answer`) REFERENCES `QUESANS` (`Q_id`, `Answer`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RESPONSE`
--

LOCK TABLES `RESPONSE` WRITE;
/*!40000 ALTER TABLE `RESPONSE` DISABLE KEYS */;
/*!40000 ALTER TABLE `RESPONSE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STUDENT`
--

DROP TABLE IF EXISTS `STUDENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `STUDENT` (
  `Email_id` varchar(255) NOT NULL,
  `Roll_no` int NOT NULL,
  `Batch` varchar(20) NOT NULL,
  PRIMARY KEY (`Email_id`),
  UNIQUE KEY `Roll_no` (`Roll_no`),
  CONSTRAINT `STUDENT_ibfk_1` FOREIGN KEY (`Email_id`) REFERENCES `ACCOUNT` (`Email_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STUDENT`
--

LOCK TABLES `STUDENT` WRITE;
/*!40000 ALTER TABLE `STUDENT` DISABLE KEYS */;
INSERT INTO `STUDENT` VALUES ('ahmad@mail.com',1010604940,'cse'),('alecia@mail.com',1020402040,'cse'),('fank@mail.com',1010202040,'cse'),('james@mail.com',1010604943,'ece'),('jennifer@mail.com',1020404040,'ece'),('joe@mail.com',1010605043,'cse'),('john@mail.com',1010202030,'cse'),('joyce@mail.com',1010604040,'cse'),('ramesh@mail.com',1010404040,'ece'),('steve@mail.com',1010605143,'ece');
/*!40000 ALTER TABLE `STUDENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TEAM`
--

DROP TABLE IF EXISTS `TEAM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TEAM` (
  `Team_name` varchar(255) NOT NULL,
  `Course_name` varchar(255) NOT NULL,
  `Details` mediumtext,
  `Admin_id` varchar(255) NOT NULL,
  PRIMARY KEY (`Team_name`),
  KEY `Admin_id` (`Admin_id`),
  CONSTRAINT `TEAM_ibfk_1` FOREIGN KEY (`Admin_id`) REFERENCES `INSTRUCTOR` (`Email_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TEAM`
--

LOCK TABLES `TEAM` WRITE;
/*!40000 ALTER TABLE `TEAM` DISABLE KEYS */;
INSERT INTO `TEAM` VALUES ('Data_Analysis','CS.301.2020','data and analysis and SQL','profDA101@mail.com');
/*!40000 ALTER TABLE `TEAM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TEXTBOOK`
--

DROP TABLE IF EXISTS `TEXTBOOK`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `TEXTBOOK` (
  `Team_name` varchar(255) NOT NULL,
  `Textbook` varchar(255) NOT NULL,
  PRIMARY KEY (`Team_name`,`Textbook`),
  CONSTRAINT `TEXTBOOK_ibfk_1` FOREIGN KEY (`Team_name`) REFERENCES `TEAM` (`Team_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TEXTBOOK`
--

LOCK TABLES `TEXTBOOK` WRITE;
/*!40000 ALTER TABLE `TEXTBOOK` DISABLE KEYS */;
INSERT INTO `TEXTBOOK` VALUES ('Data_Analysis','Fundamentals of DA'),('Data_Analysis','SQL Basics');
/*!40000 ALTER TABLE `TEXTBOOK` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-05 19:28:39
