-- MySQL dump

SET FOREIGN_KEY_CHECKS=0;

CREATE TABLE `allocation_allocate_mentor` (
  `id` int NOT NULL,
  `team_domain` varchar(50) NOT NULL,
  `mentor_domain` varchar(50) DEFAULT NULL,
  `mentor_alt_domains` longtext,
  `mentor_experience` varchar(50) DEFAULT NULL,
  `similarity_score` double NOT NULL,
  `reason` varchar(100) DEFAULT NULL,
  `allocated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `allocation_allocate_mentor`
--

LOCK TABLES `allocation_allocate_mentor` WRITE;
/*!40000 ALTER TABLE `allocation_allocate_mentor` DISABLE KEYS */;
INSERT INTO `allocation_allocate_mentor` VALUES (1,'AI','AI',NULL,'Expert',1,'Exact expert match','2025-10-06 14:16:57.000000'),(2,'AI','AIML',NULL,'Expert',0.9,'Strong related expert match','2025-10-06 14:16:57.000000'),(3,'AI','AIDS',NULL,'Expert',0.9,'Strong related expert match','2025-10-06 14:16:57.000000'),(4,'AI','FS',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(5,'AI','CD',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(6,'AI','BW',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(7,'AI','CYS',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(8,'AI','IOT',NULL,'Expert',0.2,'Weak expert match (IOT)','2025-10-06 14:16:57.000000'),(9,'AI','AI','AIML,AIDS,FS','Beginner',0.8,'Exact beginner match','2025-10-06 14:16:57.000000'),(10,'AI','AI','AIML,FS,AIDS','Beginner',0.8,'Exact beginner match','2025-10-06 14:16:57.000000'),(11,'AI','AI','AIDS,AIML,FS','Beginner',0.8,'Exact beginner match','2025-10-06 14:16:57.000000'),(12,'AI','AI','AIDS,FS,AIML','Beginner',0.8,'Exact beginner match','2025-10-06 14:16:57.000000'),(13,'AI','AI','FS,AIML,AIDS','Beginner',0.8,'Exact beginner match','2025-10-06 14:16:57.000000'),(14,'AI','AI','FS,AIDS,AIML','Beginner',0.8,'Exact beginner match','2025-10-06 14:16:57.000000'),(15,'AI','AIML','AI,AIDS,FS','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(16,'AI','AIML','AI,FS,AIDS','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(17,'AI','AIML','AIDS,AI,FS','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(18,'AI','AIML','AIDS,FS,AI','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(19,'AI','AIML','FS,AI,AIDS','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(20,'AI','AIML','FS,AIDS,AI','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(21,'AI','AIDS','AI,AIML,FS','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(22,'AI','AIDS','AI,FS,AIML','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(23,'AI','AIDS','AIML,AI,FS','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(24,'AI','AIDS','AIML,FS,AI','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(25,'AI','AIDS','FS,AI,AIML','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(26,'AI','AIDS','FS,AIML,AI','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(27,'AI','FS','AI,AIML,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(28,'AI','FS','AI,AIDS,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(29,'AI','FS','AIML,AI,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(30,'AI','FS','AIML,AIDS,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(31,'AI','FS','AIDS,AI,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(32,'AI','FS','AIDS,AIML,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(33,'AI','CD','AI,AIML,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(34,'AI','CD','AI,AIDS,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(35,'AI','CD','AIML,AI,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(36,'AI','CD','AIML,AIDS,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(37,'AI','CD','AIDS,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(38,'AI','CD','AIDS,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(39,'AI','BW','AI,AIML,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(40,'AI','BW','AI,AIDS,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(41,'AI','BW','AIML,AI,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(42,'AI','BW','AIML,AIDS,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(43,'AI','BW','AIDS,AI,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(44,'AI','BW','AIDS,AIML,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(45,'AI','CYS','AI,AIML,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(46,'AI','CYS','AI,AIDS,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(47,'AI','CYS','AIML,AI,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(48,'AI','CYS','AIML,AIDS,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(49,'AI','CYS','AIDS,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(50,'AI','CYS','AIDS,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(51,'AI','IOT','AI,AIML,AIDS','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(52,'AI','IOT','AI,AIDS,AIML','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(53,'AI','IOT','AIML,AI,AIDS','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(54,'AI','IOT','AIML,AIDS,AI','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(55,'AI','IOT','AIDS,AI,AIML','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(56,'AI','IOT','AIDS,AIML,AI','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(57,'AIML','AIML',NULL,'Expert',1,'Exact expert match','2025-10-06 14:16:57.000000'),(58,'AIML','AI',NULL,'Expert',0.9,'Strong related expert match','2025-10-06 14:16:57.000000'),(59,'AIML','AIDS',NULL,'Expert',0.8,'Related expert match','2025-10-06 14:16:57.000000'),(60,'AIML','FS',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(61,'AIML','CD',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(62,'AIML','BW',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(63,'AIML','CYS',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(64,'AIML','IOT',NULL,'Expert',0.2,'Weak expert match (IOT)','2025-10-06 14:16:57.000000'),(65,'AIML','AIML','AI,AIDS,FS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(66,'AIML','AIML','AI,FS,AIDS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(67,'AIML','AIML','AIDS,AI,FS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(68,'AIML','AIML','AIDS,FS,AI','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(69,'AIML','AIML','FS,AI,AIDS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(70,'AIML','AIML','FS,AIDS,AI','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(71,'AIML','AI','AIML,AIDS,FS','Beginner',0.6,'Related beginner match','2025-10-06 14:16:57.000000'),(72,'AIML','AI','AIML,FS,AIDS','Beginner',0.6,'Related beginner match','2025-10-06 14:16:57.000000'),(73,'AIML','AI','AIDS,AIML,FS','Beginner',0.6,'Related beginner match','2025-10-06 14:16:57.000000'),(74,'AIML','AI','AIDS,FS,AIML','Beginner',0.6,'Related beginner match','2025-10-06 14:16:57.000000'),(75,'AIML','AI','FS,AIML,AIDS','Beginner',0.6,'Related beginner match','2025-10-06 14:16:57.000000'),(76,'AIML','AI','FS,AIDS,AIML','Beginner',0.6,'Related beginner match','2025-10-06 14:16:57.000000'),(77,'AIML','AIDS','AIML,AI,FS','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(78,'AIML','AIDS','AIML,FS,AI','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(79,'AIML','AIDS','AI,AIML,FS','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(80,'AIML','AIDS','AI,FS,AIML','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(81,'AIML','AIDS','FS,AIML,AI','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(82,'AIML','AIDS','FS,AI,AIML','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(83,'AIML','FS','AIML,AI,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(84,'AIML','FS','AIML,AIDS,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(85,'AIML','FS','AI,AIML,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(86,'AIML','FS','AI,AIDS,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(87,'AIML','FS','AIDS,AIML,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(88,'AIML','FS','AIDS,AI,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(89,'AIML','CD','AIML,AI,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(90,'AIML','CD','AIML,AIDS,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(91,'AIML','CD','AI,AIML,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(92,'AIML','CD','AI,AIDS,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(93,'AIML','CD','AIDS,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(94,'AIML','CD','AIDS,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(95,'AIML','BW','AIML,AI,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(96,'AIML','BW','AIML,AIDS,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(97,'AIML','BW','AI,AIML,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(98,'AIML','BW','AI,AIDS,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(99,'AIML','BW','AIDS,AIML,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(100,'AIML','BW','AIDS,AI,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(101,'AIML','CYS','AIML,AI,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(102,'AIML','CYS','AIML,AIDS,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(103,'AIML','CYS','AI,AIML,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(104,'AIML','CYS','AI,AIDS,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(105,'AIML','CYS','AIDS,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(106,'AIML','CYS','AIDS,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(107,'AIML','IOT','AIML,AI,AIDS','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(108,'AIML','IOT','AIML,AIDS,AI','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(109,'AIML','IOT','AI,AIML,AIDS','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(110,'AIML','IOT','AI,AIDS,AIML','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(111,'AIML','IOT','AIDS,AIML,AI','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(112,'AIML','IOT','AIDS,AI,AIML','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(113,'AIDS','AIDS',NULL,'Expert',1,'Exact expert match','2025-10-06 14:16:57.000000'),(114,'AIDS','AI',NULL,'Expert',0.9,'Strong related expert match','2025-10-06 14:16:57.000000'),(115,'AIDS','AIML',NULL,'Expert',0.8,'Related expert match','2025-10-06 14:16:57.000000'),(116,'AIDS','FS',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(117,'AIDS','BW',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(118,'AIDS','CD',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(119,'AIDS','CYS',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(120,'AIDS','IOT',NULL,'Expert',0.2,'Weak expert match (IOT)','2025-10-06 14:16:57.000000'),(121,'AIDS','AIDS','AI,AIML,FS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(122,'AIDS','AIDS','AI,FS,AIML','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(123,'AIDS','AIDS','AIML,AI,FS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(124,'AIDS','AIDS','AIML,FS,AI','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(125,'AIDS','AIDS','FS,AI,AIML','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(126,'AIDS','AIDS','FS,AIML,AI','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(127,'AIDS','AI','AIDS,AIML,FS','Beginner',0.6,'Related beginner match','2025-10-06 14:16:57.000000'),(128,'AIDS','AI','AIDS,FS,AIML','Beginner',0.6,'Related beginner match','2025-10-06 14:16:57.000000'),(129,'AIDS','AI','AIML,AIDS,FS','Beginner',0.6,'Related beginner match','2025-10-06 14:16:57.000000'),(130,'AIDS','AI','AIML,FS,AIDS','Beginner',0.6,'Related beginner match','2025-10-06 14:16:57.000000'),(131,'AIDS','AI','FS,AIDS,AIML','Beginner',0.6,'Related beginner match','2025-10-06 14:16:57.000000'),(132,'AIDS','AI','FS,AIML,AIDS','Beginner',0.6,'Related beginner match','2025-10-06 14:16:57.000000'),(133,'AIDS','AIML','AIDS,AI,FS','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(134,'AIDS','AIML','AIDS,FS,AI','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(135,'AIDS','AIML','AI,AIDS,FS','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(136,'AIDS','AIML','AI,FS,AIDS','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(137,'AIDS','AIML','FS,AIDS,AI','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(138,'AIDS','AIML','FS,AI,AIDS','Beginner',0.5,'Related beginner match','2025-10-06 14:16:57.000000'),(139,'AIDS','FS','AIDS,AI,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(140,'AIDS','FS','AIDS,AIML,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(141,'AIDS','FS','AI,AIDS,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(142,'AIDS','FS','AI,AIML,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(143,'AIDS','FS','AIML,AIDS,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(144,'AIDS','FS','AIML,AI,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(145,'AIDS','BW','AIDS,AI,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(146,'AIDS','BW','AIDS,AIML,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(147,'AIDS','BW','AI,AIDS,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(148,'AIDS','BW','AI,AIML,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(149,'AIDS','BW','AIML,AIDS,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(150,'AIDS','BW','AIML,AI,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(151,'AIDS','CD','AIDS,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(152,'AIDS','CD','AIDS,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(153,'AIDS','CD','AI,AIDS,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(154,'AIDS','CD','AI,AIML,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(155,'AIDS','CD','AIML,AIDS,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(156,'AIDS','CD','AIML,AI,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(157,'AIDS','CYS','AIDS,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(158,'AIDS','CYS','AIDS,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(159,'AIDS','CYS','AI,AIDS,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(160,'AIDS','CYS','AI,AIML,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(161,'AIDS','CYS','AIML,AIDS,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(162,'AIDS','CYS','AIML,AI,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(163,'AIDS','IOT','AIDS,AI,AIML','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(164,'AIDS','IOT','AIDS,AIML,AI','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(165,'AIDS','IOT','AI,AIDS,AIML','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(166,'AIDS','IOT','AI,AIML,AIDS','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(167,'AIDS','IOT','AIML,AIDS,AI','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(168,'AIDS','IOT','AIML,AI,AIDS','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(169,'FS','FS',NULL,'Expert',1,'Exact expert match','2025-10-06 14:16:57.000000'),(170,'FS','AI',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(171,'FS','AIML',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(172,'FS','AIDS',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(173,'FS','BW',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(174,'FS','CD',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(175,'FS','CYS',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(176,'FS','IOT',NULL,'Expert',0.3,'Weak expert match (IOT)','2025-10-06 14:16:57.000000'),(177,'FS','FS','AI,AIML,AIDS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(178,'FS','FS','AI,AIDS,AIML','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(179,'FS','FS','AIML,AI,AIDS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(180,'FS','FS','AIML,AIDS,AI','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(181,'FS','FS','AIDS,AI,AIML','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(182,'FS','FS','AIDS,AIML,AI','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(183,'FS','AI','FS,AIML,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(184,'FS','AI','FS,AIDS,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(185,'FS','AI','AIML,FS,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(186,'FS','AI','AIML,AIDS,FS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(187,'FS','AI','AIDS,FS,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(188,'FS','AI','AIDS,AIML,FS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(189,'FS','AIML','FS,AI,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(190,'FS','AIML','FS,AIDS,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(191,'FS','AIML','AI,FS,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(192,'FS','AIML','AI,AIDS,FS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(193,'FS','AIML','AIDS,FS,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(194,'FS','AIML','AIDS,AI,FS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(195,'FS','AIDS','FS,AI,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(196,'FS','AIDS','FS,AIML,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(197,'FS','AIDS','AI,FS,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(198,'FS','AIDS','AI,AIML,FS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(199,'FS','AIDS','AIML,FS,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(200,'FS','AIDS','AIML,AI,FS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(201,'FS','BW','FS,AI,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(202,'FS','BW','FS,AIML,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(203,'FS','BW','AI,FS,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(204,'FS','BW','AI,AIML,FS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(205,'FS','BW','AIML,FS,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(206,'FS','BW','AIML,AI,FS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(207,'FS','CD','FS,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(208,'FS','CD','FS,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(209,'FS','CD','AI,FS,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(210,'FS','CD','AI,AIML,FS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(211,'FS','CD','AIML,FS,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(212,'FS','CD','AIML,AI,FS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(213,'FS','CYS','FS,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(214,'FS','CYS','FS,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(215,'FS','CYS','AI,FS,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(216,'FS','CYS','AI,AIML,FS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(217,'FS','CYS','AIML,FS,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(218,'FS','CYS','AIML,AI,FS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(219,'FS','IOT','FS,AI,AIML','Beginner',0.4,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(220,'FS','IOT','FS,AIML,AI','Beginner',0.4,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(221,'FS','IOT','AI,FS,AIML','Beginner',0.4,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(222,'FS','IOT','AI,AIML,FS','Beginner',0.4,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(223,'FS','IOT','AIML,FS,AI','Beginner',0.4,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(224,'FS','IOT','AIML,AI,FS','Beginner',0.4,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(225,'CD','CD',NULL,'Expert',1,'Exact expert match','2025-10-06 14:16:57.000000'),(226,'CD','AI',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(227,'CD','AIML',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(228,'CD','AIDS',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(229,'CD','BW',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(230,'CD','FS',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(231,'CD','CYS',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(232,'CD','IOT',NULL,'Expert',0.2,'Weak expert match (IOT)','2025-10-06 14:16:57.000000'),(233,'CD','CD','AI,AIML,AIDS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(234,'CD','CD','AI,AIDS,AIML','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(235,'CD','CD','AIML,AI,AIDS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(236,'CD','CD','AIML,AIDS,AI','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(237,'CD','CD','AIDS,AI,AIML','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(238,'CD','CD','AIDS,AIML,AI','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(239,'CD','AI','CD,AIML,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(240,'CD','AI','CD,AIDS,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(241,'CD','AI','AIML,CD,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(242,'CD','AI','AIML,AIDS,CD','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(243,'CD','AI','AIDS,CD,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(244,'CD','AI','AIDS,AIML,CD','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(245,'CD','AIML','CD,AI,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(246,'CD','AIML','CD,AIDS,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(247,'CD','AIML','AI,CD,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(248,'CD','AIML','AI,AIDS,CD','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(249,'CD','AIML','AIDS,CD,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(250,'CD','AIML','AIDS,AI,CD','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(251,'CD','AIDS','CD,AI,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(252,'CD','AIDS','CD,AIML,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(253,'CD','AIDS','AI,CD,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(254,'CD','AIDS','AI,AIML,CD','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(255,'CD','AIDS','AIML,CD,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(256,'CD','AIDS','AIML,AI,CD','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(257,'CD','BW','CD,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(258,'CD','BW','CD,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(259,'CD','BW','AI,CD,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(260,'CD','BW','AI,AIML,CD','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(261,'CD','BW','AIML,CD,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(262,'CD','BW','AIML,AI,CD','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(263,'CD','FS','CD,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(264,'CD','FS','CD,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(265,'CD','FS','AI,CD,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(266,'CD','FS','AI,AIML,CD','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(267,'CD','FS','AIML,CD,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(268,'CD','FS','AIML,AI,CD','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(269,'CD','CYS','CD,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(270,'CD','CYS','CD,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(271,'CD','CYS','AI,CD,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(272,'CD','CYS','AI,AIML,CD','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(273,'CD','CYS','AIML,CD,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(274,'CD','CYS','AIML,AI,CD','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(275,'CD','IOT','CD,AI,AIML','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(276,'CD','IOT','CD,AIML,AI','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(277,'CD','IOT','AI,CD,AIML','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(278,'CD','IOT','AI,AIML,CD','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(279,'CD','IOT','AIML,CD,AI','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(280,'CD','IOT','AIML,AI,CD','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(281,'BW','BW',NULL,'Expert',1,'Exact expert match','2025-10-06 14:16:57.000000'),(282,'BW','AI',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(283,'BW','AIML',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(284,'BW','AIDS',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(285,'BW','CD',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(286,'BW','FS',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(287,'BW','CYS',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(288,'BW','IOT',NULL,'Expert',0.3,'Weak expert match (IOT)','2025-10-06 14:16:57.000000'),(289,'BW','BW','AI,AIML,AIDS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(290,'BW','BW','AI,AIDS,AIML','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(291,'BW','BW','AIML,AI,AIDS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(292,'BW','BW','AIML,AIDS,AI','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(293,'BW','BW','AIDS,AI,AIML','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(294,'BW','BW','AIDS,AIML,AI','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(295,'BW','AI','BW,AIML,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(296,'BW','AI','BW,AIDS,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(297,'BW','AI','AIML,BW,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(298,'BW','AI','AIML,AIDS,BW','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(299,'BW','AI','AIDS,BW,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(300,'BW','AI','AIDS,AIML,BW','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(301,'BW','AIML','BW,AI,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(302,'BW','AIML','BW,AIDS,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(303,'BW','AIML','AI,BW,AIDS','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(304,'BW','AIML','AI,AIDS,BW','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(305,'BW','AIML','AIDS,BW,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(306,'BW','AIML','AIDS,AI,BW','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(307,'BW','AIDS','BW,AI,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(308,'BW','AIDS','BW,AIML,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(309,'BW','AIDS','AI,BW,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(310,'BW','AIDS','AI,AIML,BW','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(311,'BW','AIDS','AIML,BW,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(312,'BW','AIDS','AIML,AI,BW','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(313,'BW','CD','BW,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(314,'BW','CD','BW,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(315,'BW','CD','AI,BW,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(316,'BW','CD','AI,AIML,BW','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(317,'BW','CD','AIML,BW,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(318,'BW','CD','AIML,AI,BW','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(319,'BW','FS','BW,AI,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(320,'BW','FS','BW,AIML,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(321,'BW','FS','AI,BW,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(322,'BW','FS','AI,AIML,BW','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(323,'BW','FS','AIML,BW,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(324,'BW','FS','AIML,AI,BW','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(325,'BW','CYS','BW,AI,AIML','Beginner',0.5,'Related beginner match (CYS)','2025-10-06 14:16:57.000000'),(326,'BW','CYS','BW,AIML,AI','Beginner',0.5,'Related beginner match (CYS)','2025-10-06 14:16:57.000000'),(327,'BW','CYS','AI,BW,AIML','Beginner',0.5,'Related beginner match (CYS)','2025-10-06 14:16:57.000000'),(328,'BW','CYS','AI,AIML,BW','Beginner',0.5,'Related beginner match (CYS)','2025-10-06 14:16:57.000000'),(329,'BW','CYS','AIML,BW,AI','Beginner',0.5,'Related beginner match (CYS)','2025-10-06 14:16:57.000000'),(330,'BW','CYS','AIML,AI,BW','Beginner',0.5,'Related beginner match (CYS)','2025-10-06 14:16:57.000000'),(331,'BW','IOT','BW,AI,AIML','Beginner',0.4,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(332,'BW','IOT','BW,AIML,AI','Beginner',0.4,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(333,'BW','IOT','AI,BW,AIML','Beginner',0.4,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(334,'BW','IOT','AI,AIML,BW','Beginner',0.4,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(335,'BW','IOT','AIML,BW,AI','Beginner',0.4,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(336,'BW','IOT','AIML,AI,BW','Beginner',0.4,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(337,'CYS','CYS',NULL,'Expert',1,'Exact expert match','2025-10-06 14:16:57.000000'),(338,'CYS','AI',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(339,'CYS','AIML',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(340,'CYS','AIDS',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(341,'CYS','CD',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(342,'CYS','FS',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(343,'CYS','BW',NULL,'Expert',0.4,'Weak expert match','2025-10-06 14:16:57.000000'),(344,'CYS','IOT',NULL,'Expert',0.2,'Weak expert match (IOT)','2025-10-06 14:16:57.000000'),(345,'CYS','CYS','AI,AIML,AIDS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(346,'CYS','CYS','AI,AIDS,AIML','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(347,'CYS','CYS','AIML,AI,AIDS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(348,'CYS','CYS','AIML,AIDS,AI','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(349,'CYS','CYS','AIDS,AI,AIML','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(350,'CYS','CYS','AIDS,AIML,AI','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(351,'CYS','AI','CYS,AIML,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(352,'CYS','AI','CYS,AIDS,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(353,'CYS','AI','AIML,CYS,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(354,'CYS','AI','AIML,AIDS,CYS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(355,'CYS','AI','AIDS,CYS,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(356,'CYS','AI','AIDS,AIML,CYS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(357,'CYS','AIML','CYS,AI,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(358,'CYS','AIML','CYS,AIDS,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(359,'CYS','AIML','AI,CYS,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(360,'CYS','AIML','AI,AIDS,CYS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(361,'CYS','AIML','AIDS,CYS,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(362,'CYS','AIML','AIDS,AI,CYS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(363,'CYS','AIDS','CYS,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(364,'CYS','AIDS','CYS,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(365,'CYS','AIDS','AI,CYS,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(366,'CYS','AIDS','AI,AIML,CYS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(367,'CYS','AIDS','AIML,CYS,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(368,'CYS','AIDS','AIML,AI,CYS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(369,'CYS','CD','CYS,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(370,'CYS','CD','CYS,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(371,'CYS','CD','AI,CYS,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(372,'CYS','CD','AI,AIML,CYS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(373,'CYS','CD','AIML,CYS,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(374,'CYS','CD','AIML,AI,CYS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(375,'CYS','FS','CYS,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(376,'CYS','FS','CYS,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(377,'CYS','FS','AI,CYS,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(378,'CYS','FS','AI,AIML,CYS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(379,'CYS','FS','AIML,CYS,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(380,'CYS','FS','AIML,AI,CYS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(381,'CYS','BW','CYS,AI,AIML','Beginner',0.5,'Related beginner match (BW)','2025-10-06 14:16:57.000000'),(382,'CYS','BW','CYS,AIML,AI','Beginner',0.5,'Related beginner match (BW)','2025-10-06 14:16:57.000000'),(383,'CYS','BW','AI,CYS,AIML','Beginner',0.5,'Related beginner match (BW)','2025-10-06 14:16:57.000000'),(384,'CYS','BW','AI,AIML,CYS','Beginner',0.5,'Related beginner match (BW)','2025-10-06 14:16:57.000000'),(385,'CYS','BW','AIML,CYS,AI','Beginner',0.5,'Related beginner match (BW)','2025-10-06 14:16:57.000000'),(386,'CYS','BW','AIML,AI,CYS','Beginner',0.5,'Related beginner match (BW)','2025-10-06 14:16:57.000000'),(387,'CYS','IOT','CYS,AI,AIML','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(388,'CYS','IOT','CYS,AIML,AI','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(389,'CYS','IOT','AI,CYS,AIML','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(390,'CYS','IOT','AI,AIML,CYS','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(391,'CYS','IOT','AIML,CYS,AI','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(392,'CYS','IOT','AIML,AI,CYS','Beginner',0.3,'Weak beginner match (IOT)','2025-10-06 14:16:57.000000'),(393,'IOT','IOT',NULL,'Expert',1,'Exact expert match','2025-10-06 14:16:57.000000'),(394,'IOT','AI',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(395,'IOT','AIML',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(396,'IOT','AIDS',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(397,'IOT','CD',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(398,'IOT','FS',NULL,'Expert',0.3,'Weak expert match','2025-10-06 14:16:57.000000'),(399,'IOT','BW',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(400,'IOT','CYS',NULL,'Expert',0.2,'Weak expert match','2025-10-06 14:16:57.000000'),(401,'IOT','IOT','AI,AIML,AIDS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(402,'IOT','IOT','AI,AIDS,AIML','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(403,'IOT','IOT','AIML,AI,AIDS','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(404,'IOT','IOT','AIML,AIDS,AI','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(405,'IOT','IOT','AIDS,AI,AIML','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(406,'IOT','IOT','AIDS,AIML,AI','Beginner',0.7,'Exact beginner match','2025-10-06 14:16:57.000000'),(407,'IOT','AI','IOT,AIML,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(408,'IOT','AI','IOT,AIDS,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(409,'IOT','AI','AIML,IOT,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(410,'IOT','AI','AIML,AIDS,IOT','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(411,'IOT','AI','AIDS,IOT,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(412,'IOT','AI','AIDS,AIML,IOT','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(413,'IOT','AIML','IOT,AI,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(414,'IOT','AIML','IOT,AIDS,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(415,'IOT','AIML','AI,IOT,AIDS','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(416,'IOT','AIML','AI,AIDS,IOT','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(417,'IOT','AIML','AIDS,IOT,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(418,'IOT','AIML','AIDS,AI,IOT','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(419,'IOT','AIDS','IOT,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(420,'IOT','AIDS','IOT,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(421,'IOT','AIDS','AI,IOT,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(422,'IOT','AIDS','AI,AIML,IOT','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(423,'IOT','AIDS','AIML,IOT,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(424,'IOT','AIDS','AIML,AI,IOT','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(425,'IOT','CD','IOT,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(426,'IOT','CD','IOT,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(427,'IOT','CD','AI,IOT,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(428,'IOT','CD','AI,AIML,IOT','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(429,'IOT','CD','AIML,IOT,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(430,'IOT','CD','AIML,AI,IOT','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(431,'IOT','FS','IOT,AI,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(432,'IOT','FS','IOT,AIML,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(433,'IOT','FS','AI,IOT,AIML','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(434,'IOT','FS','AI,AIML,IOT','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(435,'IOT','FS','AIML,IOT,AI','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(436,'IOT','FS','AIML,AI,IOT','Beginner',0.4,'Weak beginner match','2025-10-06 14:16:57.000000'),(437,'IOT','BW','IOT,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(438,'IOT','BW','IOT,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(439,'IOT','BW','AI,IOT,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(440,'IOT','BW','AI,AIML,IOT','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(441,'IOT','BW','AIML,IOT,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(442,'IOT','BW','AIML,AI,IOT','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(443,'IOT','CYS','IOT,AI,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(444,'IOT','CYS','IOT,AIML,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(445,'IOT','CYS','AI,IOT,AIML','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(446,'IOT','CYS','AI,AIML,IOT','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(447,'IOT','CYS','AIML,IOT,AI','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000'),(448,'IOT','CYS','AIML,AI,IOT','Beginner',0.3,'Weak beginner match','2025-10-06 14:16:57.000000');
/*!40000 ALTER TABLE `allocation_allocate_mentor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allocation_allocationresult`
--

DROP TABLE IF EXISTS `allocation_allocationresult`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocation_allocationresult` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `team_name` varchar(100) NOT NULL,
  `team_domain` varchar(100) NOT NULL,
  `mentor_name` varchar(100) NOT NULL,
  `mentor_domain` varchar(100) NOT NULL,
  `alt_domains` longtext NOT NULL,
  `experience` varchar(50) NOT NULL,
  `similarity_score` double NOT NULL,
  `reason` longtext NOT NULL,
  `allocated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `allocation_allocationresult`
--

LOCK TABLES `allocation_allocationresult` WRITE;
/*!40000 ALTER TABLE `allocation_allocationresult` DISABLE KEYS */;
INSERT INTO `allocation_allocationresult` VALUES (4,'Ai Image Processing','AIDS','Suresh Kumar','AIML','','Expert',0.8,'Related expert match','2025-10-13 17:45:06.348793'),(5,'Security Management','CYS','Suriya','CYS','','Expert',1,'Exact expert match','2025-10-14 04:05:32.987289'),(6,'Cloud Management','CD','Gnanavel','BW','','Expert',0.2,'Weak expert match','2025-10-17 06:53:38.063129');
/*!40000 ALTER TABLE `allocation_allocationresult` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allocation_announcement`
--

DROP TABLE IF EXISTS `allocation_announcement`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocation_announcement` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `message` longtext NOT NULL,
  `ann_type` varchar(20) NOT NULL,
  `target_role` varchar(20) NOT NULL,
  `deadline_date` date DEFAULT NULL,
  `deadline_time` time(6) DEFAULT NULL,
  `schedule_date` date DEFAULT NULL,
  `schedule_time` time(6) DEFAULT NULL,
  `venue` varchar(200) DEFAULT NULL,
  `created_by_username` varchar(80) NOT NULL,
  `created_by_name` varchar(80) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `allocation_announcement`
--

LOCK TABLES `allocation_announcement` WRITE;
/*!40000 ALTER TABLE `allocation_announcement` DISABLE KEYS */;
INSERT INTO `allocation_announcement` VALUES (1,'Zeroth Review','','deadline','student','2025-12-28','12:37:00.000000',NULL,NULL,NULL,'20001','ZZZ','2025-12-26 07:07:31.474015'),(2,'First REeview PPt','','deadline','both','2026-01-31','11:51:00.000000',NULL,NULL,NULL,'20001','ZZZ','2026-01-28 05:21:48.368777');
/*!40000 ALTER TABLE `allocation_announcement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allocation_announcementstatus`
--

DROP TABLE IF EXISTS `allocation_announcementstatus`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocation_announcementstatus` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `receiver_role` varchar(20) NOT NULL,
  `receiver_id` varchar(80) NOT NULL,
  `receiver_name` varchar(80) NOT NULL,
  `seen_at` datetime(6) DEFAULT NULL,
  `acknowledged_at` datetime(6) DEFAULT NULL,
  `announcement_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `allocation_announcem_announcement_id_b4ef3f5a_fk_allocatio` (`announcement_id`),
  CONSTRAINT `allocation_announcem_announcement_id_b4ef3f5a_fk_allocatio` FOREIGN KEY (`announcement_id`) REFERENCES `allocation_announcement` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `allocation_announcementstatus`
--

LOCK TABLES `allocation_announcementstatus` WRITE;
/*!40000 ALTER TABLE `allocation_announcementstatus` DISABLE KEYS */;
INSERT INTO `allocation_announcementstatus` VALUES (1,'student','24UCS101','Mohammed Salis',NULL,NULL,1),(2,'student','24UCS102','Nandhana',NULL,NULL,1),(3,'student','24UCS103','Nathiya',NULL,NULL,1),(4,'student','24UCS104','Narmatha',NULL,NULL,1),(5,'student','24UCS105','Vinothaa',NULL,NULL,1),(6,'student','24UCS106','Raahul Kanna',NULL,NULL,1),(7,'student','24UCS107','Saravanamariappan',NULL,NULL,1),(8,'student','24UCS108','Sandhiya',NULL,NULL,1),(9,'student','24UCS109','Sahana',NULL,NULL,1),(10,'student','24UCS110','Vitharshana',NULL,NULL,1),(11,'student','24UCS111','Sackthika',NULL,NULL,1),(12,'student','24UCS112','Padmapriya',NULL,NULL,1),(13,'student','24UCS113','Bhavasri',NULL,NULL,1),(14,'student','24UCS114','Dharunika',NULL,NULL,1),(15,'student','24UCS115','Ragul',NULL,NULL,1),(16,'student','24UCS116','Pravinraja',NULL,NULL,1),(17,'student','24UCS117','Santhosh',NULL,NULL,1),(18,'student','24UCS118','Praveen',NULL,NULL,1),(19,'student','24UCS119','Pavish',NULL,NULL,1),(20,'student','24UCS120','Ragunath',NULL,NULL,1),(21,'student','24UCS201','Kavin',NULL,NULL,1),(22,'student','24UCS202','Srishanth',NULL,NULL,1),(23,'student','24UCS203','Omar',NULL,NULL,1),(24,'student','24UCS204','Pranav',NULL,NULL,1),(25,'student','24UCS205','Srinithi',NULL,NULL,1),(26,'student','24UCS206','Nithya',NULL,NULL,1),(27,'student','24UCS207','Sangeetha',NULL,NULL,1),(28,'student','24UCS208','Priya','2025-12-26 07:58:09.263694','2025-12-26 08:03:56.883086',1),(29,'student','24UCS209','Maheshwari',NULL,NULL,1),(30,'student','24UCS210','Vinoth',NULL,NULL,1),(31,'student','24UCS211','Kirubakaran',NULL,NULL,1),(32,'student','24UCS212','Aarthi',NULL,NULL,1),(33,'student','24UCS213','Bala',NULL,NULL,1),(34,'student','24UCS214','Elakkiya',NULL,NULL,1),(35,'student','24UCS215','Lakshmi','2025-12-26 08:15:36.377271','2025-12-26 08:50:31.172217',1),(36,'student','24UCS216','Raghavendra',NULL,NULL,1),(37,'student','24UCS217','Annapoorani',NULL,NULL,1),(38,'student','24UCS218','Fathima',NULL,NULL,1),(39,'student','24UCS219','Gobi',NULL,NULL,1),(40,'student','24UCS220','Meena',NULL,NULL,1),(41,'student','24UCS101','Mohammed Salis',NULL,NULL,2),(42,'student','24UCS102','Nandhana',NULL,NULL,2),(43,'student','24UCS103','Nathiya',NULL,NULL,2),(44,'student','24UCS104','Narmatha',NULL,NULL,2),(45,'student','24UCS105','Vinothaa',NULL,NULL,2),(46,'student','24UCS106','Raahul Kanna',NULL,NULL,2),(47,'student','24UCS107','Saravanamariappan',NULL,NULL,2),(48,'student','24UCS108','Sandhiya',NULL,NULL,2),(49,'student','24UCS109','Sahana',NULL,NULL,2),(50,'student','24UCS110','Vitharshana',NULL,NULL,2),(51,'student','24UCS111','Sackthika',NULL,NULL,2),(52,'student','24UCS112','Padmapriya',NULL,NULL,2),(53,'student','24UCS113','Bhavasri',NULL,NULL,2),(54,'student','24UCS114','Dharunika',NULL,NULL,2),(55,'student','24UCS115','Ragul',NULL,NULL,2),(56,'student','24UCS116','Pravinraja',NULL,NULL,2),(57,'student','24UCS117','Santhosh',NULL,NULL,2),(58,'student','24UCS118','Praveen',NULL,NULL,2),(59,'student','24UCS119','Pavish',NULL,NULL,2),(60,'student','24UCS120','Ragunath',NULL,NULL,2),(61,'student','24UCS201','Kavin',NULL,NULL,2),(62,'student','24UCS202','Srishanth',NULL,NULL,2),(63,'student','24UCS203','Omar',NULL,NULL,2),(64,'student','24UCS204','Pranav',NULL,NULL,2),(65,'student','24UCS205','Srinithi',NULL,NULL,2),(66,'student','24UCS206','Nithya',NULL,NULL,2),(67,'student','24UCS207','Sangeetha',NULL,NULL,2),(68,'student','24UCS208','Priya',NULL,NULL,2),(69,'student','24UCS209','Maheshwari',NULL,NULL,2),(70,'student','24UCS210','Vinoth',NULL,NULL,2),(71,'student','24UCS211','Kirubakaran',NULL,NULL,2),(72,'student','24UCS212','Aarthi',NULL,NULL,2),(73,'student','24UCS213','Bala',NULL,NULL,2),(74,'student','24UCS214','Elakkiya',NULL,NULL,2),(75,'student','24UCS215','Lakshmi','2026-01-28 05:28:42.246735','2026-01-28 05:29:14.235941',2),(76,'student','24UCS216','Raghavendra',NULL,NULL,2),(77,'student','24UCS217','Annapoorani',NULL,NULL,2),(78,'student','24UCS218','Fathima',NULL,NULL,2),(79,'student','24UCS219','Gobi',NULL,NULL,2),(80,'student','24UCS220','Meena',NULL,NULL,2),(81,'mentor','10001','Suresh Kumar',NULL,NULL,2),(82,'mentor','10002','Gnanavel',NULL,NULL,2),(83,'mentor','10003','Suriya',NULL,NULL,2),(84,'mentor','10004','Lathika',NULL,NULL,2),(85,'mentor','10005','Jayashree',NULL,NULL,2);
/*!40000 ALTER TABLE `allocation_announcementstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allocation_approvedteam`
--

DROP TABLE IF EXISTS `allocation_approvedteam`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocation_approvedteam` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `project_title` varchar(200) NOT NULL,
  `student_class` varchar(50) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `members` varchar(300) NOT NULL,
  `member_names` varchar(300) NOT NULL,
  `approved_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `allocation_approvedteam`
--

LOCK TABLES `allocation_approvedteam` WRITE;
/*!40000 ALTER TABLE `allocation_approvedteam` DISABLE KEYS */;
INSERT INTO `allocation_approvedteam` VALUES (41,'Security Management','CSE-B','CYS','24UCS212,24UCS205,24UCS203','Omar,Srinithi,Aarthi','2025-10-27 09:27:22.658322'),(42,'Cloud Management','CSE-B','CD','24UCS201,24UCS210,24UCS206,24UCS219','Kavin,Nithya,Vinoth,Gobi','2025-10-27 09:27:22.663647'),(43,'Ai Image Processing','CSE-B','AIDS','24UCS208,24UCS220,24UCS215','Priya,Lakshmi,Meena','2025-10-27 09:27:22.667148');
/*!40000 ALTER TABLE `allocation_approvedteam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allocation_coordinator_login`
--

DROP TABLE IF EXISTS `allocation_coordinator_login`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocation_coordinator_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `name` varchar(80) NOT NULL,
  `password` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `allocation_coordinator_login`
--

LOCK TABLES `allocation_coordinator_login` WRITE;
/*!40000 ALTER TABLE `allocation_coordinator_login` DISABLE KEYS */;
INSERT INTO `allocation_coordinator_login` VALUES (1,'20001','ZZZ','20001');
/*!40000 ALTER TABLE `allocation_coordinator_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allocation_mentor`
--

DROP TABLE IF EXISTS `allocation_mentor`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocation_mentor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `name` varchar(80) NOT NULL,
  `primary_domain` varchar(80) NOT NULL,
  `experience` int NOT NULL,
  `alternative_domains` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `allocation_mentor`
--

LOCK TABLES `allocation_mentor` WRITE;
/*!40000 ALTER TABLE `allocation_mentor` DISABLE KEYS */;
INSERT INTO `allocation_mentor` VALUES (4,'10001','Suresh Kumar','AIML',4,''),(7,'10003','Suriya','CYS',5,''),(13,'10002','Gnanavel','BW',6,'');
/*!40000 ALTER TABLE `allocation_mentor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allocation_mentor_login`
--

DROP TABLE IF EXISTS `allocation_mentor_login`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocation_mentor_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `name` varchar(80) NOT NULL,
  `password` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `allocation_mentor_login`
--

LOCK TABLES `allocation_mentor_login` WRITE;
/*!40000 ALTER TABLE `allocation_mentor_login` DISABLE KEYS */;
INSERT INTO `allocation_mentor_login` VALUES (1,'10001','Suresh Kumar','10001'),(2,'10002','Gnanavel','10002'),(3,'10003','Suriya','10003'),(4,'10004','Lathika','10004'),(5,'10005','Jayashree','10005');
/*!40000 ALTER TABLE `allocation_mentor_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allocation_modifyrequest`
--

DROP TABLE IF EXISTS `allocation_modifyrequest`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocation_modifyrequest` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `project_title` varchar(200) NOT NULL,
  `student_class` varchar(50) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `members` varchar(300) NOT NULL,
  `member_names` varchar(300) NOT NULL,
  `change_type` varchar(100) NOT NULL,
  `requested_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `allocation_modifyrequest`
--

LOCK TABLES `allocation_modifyrequest` WRITE;
/*!40000 ALTER TABLE `allocation_modifyrequest` DISABLE KEYS */;
INSERT INTO `allocation_modifyrequest` VALUES (25,'Cloud Management','CSE-B','CD','24UCS201,24UCS210,24UCS206,24UCS219','Kavin,Nithya,Vinoth,Gobi','Project Title, Domain','2025-11-07 08:16:15.458093');
/*!40000 ALTER TABLE `allocation_modifyrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allocation_projectdocument`
--

DROP TABLE IF EXISTS `allocation_projectdocument`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocation_projectdocument` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `team_name` varchar(200) NOT NULL,
  `review_stage` varchar(50) NOT NULL,
  `doc_type` varchar(20) NOT NULL,
  `file_url` varchar(500) NOT NULL,
  `uploaded_by` varchar(100) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `allocation_projectdocument`
--

LOCK TABLES `allocation_projectdocument` WRITE;
/*!40000 ALTER TABLE `allocation_projectdocument` DISABLE KEYS */;
INSERT INTO `allocation_projectdocument` VALUES (1,'Team Alpha','zeroth','abstract','https://res.cloudinary.com/demo/image/upload/sample.pdf','student1','2026-01-21 05:34:51.390135');
/*!40000 ALTER TABLE `allocation_projectdocument` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allocation_projectfile`
--

DROP TABLE IF EXISTS `allocation_projectfile`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocation_projectfile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `team_name` varchar(200) NOT NULL,
  `review_type` varchar(20) NOT NULL,
  `file_type` varchar(20) NOT NULL,
  `cloudinary_url` varchar(200) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `allocation_projectfile`
--

LOCK TABLES `allocation_projectfile` WRITE;
/*!40000 ALTER TABLE `allocation_projectfile` DISABLE KEYS */;
INSERT INTO `allocation_projectfile` VALUES (1,'Ai Image Processing','zero','ppt','https://res.cloudinary.com/dmwwhifs8/raw/upload/v1769408590/project_portal/Ai_Image_Processing/Ai_Image_Processing_PPT.pptx','2026-01-26 06:23:14.731433'),(2,'Ai Image Processing','zero','pdf','https://res.cloudinary.com/dmwwhifs8/image/upload/v1769408592/project_portal/Ai_Image_Processing/Ai_Image_Processing_Report.pdf','2026-01-26 06:23:14.749272'),(3,'Ai Image Processing','zero','abstract','https://res.cloudinary.com/dmwwhifs8/image/upload/v1769407893/project_portal/Ai_Image_Processing/Ai_Image_Processing_Abstract.pdf','2026-01-26 06:23:14.759516');
/*!40000 ALTER TABLE `allocation_projectfile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allocation_stu_login`
--

DROP TABLE IF EXISTS `allocation_stu_login`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocation_stu_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `password` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `allocation_stu_login`
--

LOCK TABLES `allocation_stu_login` WRITE;
/*!40000 ALTER TABLE `allocation_stu_login` DISABLE KEYS */;
INSERT INTO `allocation_stu_login` VALUES (1,'24UCS101','24UCS101'),(2,'24UCS102','24UCS102'),(3,'24UCS103','24UCS103'),(4,'24UCS104','24UCS104'),(5,'24UCS105','24UCS105'),(6,'24UCS106','24UCS106'),(7,'24UCS107','24UCS107'),(8,'24UCS108','24UCS108'),(9,'24UCS109','24UCS109'),(10,'24UCS110','24UCS110'),(11,'24UCS111','24UCS111'),(12,'24UCS112','24UCS112'),(13,'24UCS113','24UCS113'),(14,'24UCS114','24UCS114'),(15,'24UCS115','24UCS115'),(16,'24UCS116','24UCS116'),(17,'24UCS117','24UCS117'),(18,'24UCS118','24UCS118'),(19,'24UCS119','24UCS119'),(20,'24UCS120','24UCS120'),(21,'24UCS201','24UCS201'),(22,'24UCS202','24UCS202'),(23,'24UCS203','24UCS203'),(24,'24UCS204','24UCS204'),(25,'24UCS205','24UCS205'),(26,'24UCS206','24UCS206'),(27,'24UCS207','24UCS207'),(28,'24UCS208','24UCS208'),(29,'24UCS209','24UCS209'),(30,'24UCS210','24UCS210'),(31,'24UCS211','24UCS211'),(32,'24UCS212','24UCS212'),(33,'24UCS213','24UCS213'),(34,'24UCS214','24UCS214'),(35,'24UCS215','24UCS215'),(36,'24UCS216','24UCS216'),(37,'24UCS217','24UCS217'),(38,'24UCS218','24UCS218'),(39,'24UCS219','24UCS219'),(40,'24UCS220','24UCS220');
/*!40000 ALTER TABLE `allocation_stu_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allocation_student`
--

DROP TABLE IF EXISTS `allocation_student`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocation_student` (
  `student_id` varchar(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `cgpa` decimal(4,2) NOT NULL,
  `clas` varchar(50) NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `allocation_student`
--

LOCK TABLES `allocation_student` WRITE;
/*!40000 ALTER TABLE `allocation_student` DISABLE KEYS */;
INSERT INTO `allocation_student` VALUES ('24UCS101','Mohammed Salis',9.21,'CSE-A'),('24UCS102','Nandhana',8.23,'CSE-A'),('24UCS103','Nathiya',7.49,'CSE-A'),('24UCS104','Narmatha',8.63,'CSE-A'),('24UCS105','Vinothaa',9.63,'CSE-A'),('24UCS106','Raahul Kanna',9.35,'CSE-A'),('24UCS107','Saravanamariappan',8.96,'CSE-A'),('24UCS108','Sandhiya',8.32,'CSE-A'),('24UCS109','Sahana',7.45,'CSE-A'),('24UCS110','Vitharshana',8.63,'CSE-A'),('24UCS111','Sackthika',8.60,'CSE-A'),('24UCS112','Padmapriya',8.74,'CSE-A'),('24UCS113','Bhavasri',6.23,'CSE-A'),('24UCS114','Dharunika',6.52,'CSE-A'),('24UCS115','Ragul',7.21,'CSE-A'),('24UCS116','Pravinraja',8.23,'CSE-A'),('24UCS117','Santhosh',8.76,'CSE-A'),('24UCS118','Praveen',7.14,'CSE-A'),('24UCS119','Pavish',6.25,'CSE-A'),('24UCS120','Ragunath',5.23,'CSE-A'),('24UCS201','Kavin',8.36,'CSE-B'),('24UCS202','Srishanth',7.23,'CSE-B'),('24UCS203','Omar',8.71,'CSE-B'),('24UCS204','Pranav',6.32,'CSE-B'),('24UCS205','Srinithi',8.96,'CSE-B'),('24UCS206','Nithya',9.12,'CSE-B'),('24UCS207','Sangeetha',5.23,'CSE-B'),('24UCS208','Priya',7.45,'CSE-B'),('24UCS209','Maheshwari',8.24,'CSE-B'),('24UCS210','Vinoth',9.54,'CSE-B'),('24UCS211','Kirubakaran',7.85,'CSE-B'),('24UCS212','Aarthi',8.24,'CSE-B'),('24UCS213','Bala',7.02,'CSE-B'),('24UCS214','Elakkiya',8.52,'CSE-B'),('24UCS215','Lakshmi',9.36,'CSE-B'),('24UCS216','Raghavendra',8.04,'CSE-B'),('24UCS217','Annapoorani',8.52,'CSE-B'),('24UCS218','Fathima',7.23,'CSE-B'),('24UCS219','Gobi',6.33,'CSE-B'),('24UCS220','Meena',8.54,'CSE-B');
/*!40000 ALTER TABLE `allocation_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allocation_team`
--

DROP TABLE IF EXISTS `allocation_team`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocation_team` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `project_title` varchar(100) NOT NULL,
  `student_class` varchar(50) NOT NULL,
  `domain` varchar(100) NOT NULL,
  `members` longtext NOT NULL,
  `member_names` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `project_title` (`project_title`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `allocation_team`
--

LOCK TABLES `allocation_team` WRITE;
/*!40000 ALTER TABLE `allocation_team` DISABLE KEYS */;
INSERT INTO `allocation_team` VALUES (6,'Security Management','CSE-B','CYS','24UCS212,24UCS205,24UCS203','Omar,Srinithi,Aarthi','2025-10-14 03:48:33.388955'),(7,'Cloud Management','CSE-B','CD','24UCS201,24UCS210,24UCS206,24UCS219','Kavin,Nithya,Vinoth,Gobi','2025-10-17 06:52:51.056744'),(8,'Ai Image Processing','CSE-B','AIDS','24UCS208,24UCS220,24UCS215','Priya,Lakshmi,Meena','2025-10-17 08:44:18.934181');
/*!40000 ALTER TABLE `allocation_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `allocation_zerothreviewremark`
--

DROP TABLE IF EXISTS `allocation_zerothreviewremark`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocation_zerothreviewremark` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `team_name` varchar(255) NOT NULL,
  `mentor_name` varchar(255) NOT NULL,
  `heading` varchar(255) NOT NULL,
  `remark` longtext NOT NULL,
  `color` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_zeroth_review_remark` (`team_name`,`mentor_name`,`heading`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `allocation_zerothreviewremark`
--

LOCK TABLES `allocation_zerothreviewremark` WRITE;
/*!40000 ALTER TABLE `allocation_zerothreviewremark` DISABLE KEYS */;
INSERT INTO `allocation_zerothreviewremark` VALUES (6,'Ai Image Processing','Suresh Kumar','COMPUTER FUNDAMENTALS','bro','#ffe066','2025-12-24 13:54:56.389099'),(7,'Ai Image Processing','Suresh Kumar','Memory Unit','vv','#ffe066','2025-12-24 13:54:56.398153'),(8,'Ai Image Processing','Suresh Kumar','Register','dgtrjfth','#69db7c','2025-12-24 13:54:56.398153'),(9,'Ai Image Processing','Suresh Kumar','Index Register Addressing Mode','xdsfyretrg','#ff6b6b','2025-12-24 13:54:56.405417'),(10,'Ai Image Processing','Suresh Kumar','Buses','zcv','#ffe066','2025-12-24 13:55:11.311898'),(11,'Ai Image Processing','Suresh Kumar','y C','good','#ffe066','2026-01-28 08:09:30.719489');
/*!40000 ALTER TABLE `allocation_zerothreviewremark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add mentor',7,'add_mentor'),(26,'Can change mentor',7,'change_mentor'),(27,'Can delete mentor',7,'delete_mentor'),(28,'Can view mentor',7,'view_mentor'),(29,'Can add student',8,'add_student'),(30,'Can change student',8,'change_student'),(31,'Can delete student',8,'delete_student'),(32,'Can view student',8,'view_student'),(33,'Can add stud_ login',9,'add_stud_login'),(34,'Can change stud_ login',9,'change_stud_login'),(35,'Can delete stud_ login',9,'delete_stud_login'),(36,'Can view stud_ login',9,'view_stud_login'),(37,'Can add stu_ login',10,'add_stu_login'),(38,'Can change stu_ login',10,'change_stu_login'),(39,'Can delete stu_ login',10,'delete_stu_login'),(40,'Can view stu_ login',10,'view_stu_login'),(41,'Can add team',11,'add_team'),(42,'Can change team',11,'change_team'),(43,'Can delete team',11,'delete_team'),(44,'Can view team',11,'view_team'),(45,'Can add mentor_ login',12,'add_mentor_login'),(46,'Can change mentor_ login',12,'change_mentor_login'),(47,'Can delete mentor_ login',12,'delete_mentor_login'),(48,'Can view mentor_ login',12,'view_mentor_login'),(49,'Can add men_ login',12,'add_men_login'),(50,'Can change men_ login',12,'change_men_login'),(51,'Can delete men_ login',12,'delete_men_login'),(52,'Can view men_ login',12,'view_men_login'),(53,'Can add men_ login',13,'add_men_login'),(54,'Can change men_ login',13,'change_men_login'),(55,'Can delete men_ login',13,'delete_men_login'),(56,'Can view men_ login',13,'view_men_login'),(57,'Can add allocate_ mentor',14,'add_allocate_mentor'),(58,'Can change allocate_ mentor',14,'change_allocate_mentor'),(59,'Can delete allocate_ mentor',14,'delete_allocate_mentor'),(60,'Can view allocate_ mentor',14,'view_allocate_mentor'),(61,'Can add allocation result',15,'add_allocationresult'),(62,'Can change allocation result',15,'change_allocationresult'),(63,'Can delete allocation result',15,'delete_allocationresult'),(64,'Can view allocation result',15,'view_allocationresult'),(65,'Can add approved team',16,'add_approvedteam'),(66,'Can change approved team',16,'change_approvedteam'),(67,'Can delete approved team',16,'delete_approvedteam'),(68,'Can view approved team',16,'view_approvedteam'),(69,'Can add modify request',17,'add_modifyrequest'),(70,'Can change modify request',17,'change_modifyrequest'),(71,'Can delete modify request',17,'delete_modifyrequest'),(72,'Can view modify request',17,'view_modifyrequest'),(73,'Can add zeroth review remark',18,'add_zerothreviewremark'),(74,'Can change zeroth review remark',18,'change_zerothreviewremark'),(75,'Can delete zeroth review remark',18,'delete_zerothreviewremark'),(76,'Can view zeroth review remark',18,'view_zerothreviewremark'),(77,'Can add announcement status',19,'add_announcementstatus'),(78,'Can change announcement status',19,'change_announcementstatus'),(79,'Can delete announcement status',19,'delete_announcementstatus'),(80,'Can view announcement status',19,'view_announcementstatus'),(81,'Can add announcement',20,'add_announcement'),(82,'Can change announcement',20,'change_announcement'),(83,'Can delete announcement',20,'delete_announcement'),(84,'Can view announcement',20,'view_announcement'),(85,'Can add coordinator_ login',21,'add_coordinator_login'),(86,'Can change coordinator_ login',21,'change_coordinator_login'),(87,'Can delete coordinator_ login',21,'delete_coordinator_login'),(88,'Can view coordinator_ login',21,'view_coordinator_login'),(89,'Can add project document',22,'add_projectdocument'),(90,'Can change project document',22,'change_projectdocument'),(91,'Can delete project document',22,'delete_projectdocument'),(92,'Can view project document',22,'view_projectdocument'),(93,'Can add project file',23,'add_projectfile'),(94,'Can change project file',23,'change_projectfile'),(95,'Can delete project file',23,'delete_projectfile'),(96,'Can view project file',23,'view_projectfile');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(14,'allocation','allocate_mentor'),(15,'allocation','allocationresult'),(20,'allocation','announcement'),(19,'allocation','announcementstatus'),(16,'allocation','approvedteam'),(21,'allocation','coordinator_login'),(13,'allocation','men_login'),(7,'allocation','mentor'),(12,'allocation','mentor_login'),(17,'allocation','modifyrequest'),(22,'allocation','projectdocument'),(23,'allocation','projectfile'),(10,'allocation','stu_login'),(9,'allocation','stud_login'),(8,'allocation','student'),(11,'allocation','team'),(18,'allocation','zerothreviewremark'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2025-08-30 06:52:20.697294'),(2,'auth','0001_initial','2025-08-30 06:52:21.841727'),(3,'admin','0001_initial','2025-08-30 06:52:22.129557'),(4,'admin','0002_logentry_remove_auto_add','2025-08-30 06:52:22.146125'),(5,'admin','0003_logentry_add_action_flag_choices','2025-08-30 06:52:22.173461'),(6,'allocation','0001_initial','2025-08-30 06:52:22.299408'),(7,'contenttypes','0002_remove_content_type_name','2025-08-30 06:52:22.674879'),(8,'auth','0002_alter_permission_name_max_length','2025-08-30 06:52:22.829734'),(9,'auth','0003_alter_user_email_max_length','2025-08-30 06:52:22.884374'),(10,'auth','0004_alter_user_username_opts','2025-08-30 06:52:22.896774'),(11,'auth','0005_alter_user_last_login_null','2025-08-30 06:52:23.035398'),(12,'auth','0006_require_contenttypes_0002','2025-08-30 06:52:23.040172'),(13,'auth','0007_alter_validators_add_error_messages','2025-08-30 06:52:23.059076'),(14,'auth','0008_alter_user_username_max_length','2025-08-30 06:52:23.247059'),(15,'auth','0009_alter_user_last_name_max_length','2025-08-30 06:52:23.397482'),(16,'auth','0010_alter_group_name_max_length','2025-08-30 06:52:23.436829'),(17,'auth','0011_update_proxy_permissions','2025-08-30 06:52:23.462044'),(18,'auth','0012_alter_user_first_name_max_length','2025-08-30 06:52:23.610015'),(19,'sessions','0001_initial','2025-08-30 06:52:23.688171'),(20,'allocation','0002_remove_student_id_remove_student_password_and_more','2025-09-10 07:21:46.662029'),(21,'allocation','0003_stud_login_student_cls','2025-09-10 07:21:46.674104'),(22,'allocation','0004_rename_cls_student_clas','2025-09-10 07:21:46.678953'),(23,'allocation','0005_delete_student','2025-09-10 07:23:36.324065'),(25,'allocation','0006_student','2025-09-10 07:45:38.536178'),(26,'allocation','0007_stu_login_delete_stud_login','2025-09-10 07:46:54.225762'),(34,'allocation','0008_team','2025-09-12 09:08:40.208762'),(35,'allocation','0009_mentor_login','2025-09-12 09:08:49.882717'),(41,'allocation','0010_remove_mentor_login_department_and_more','2025-09-12 09:18:32.508602'),(42,'allocation','0011_mentor_login_name','2025-09-12 09:20:40.388338'),(52,'allocation','0012_rename_mentor_login_men_login','2025-09-12 09:22:09.234765'),(53,'allocation','0013_rename_men_login_mentor_login','2025-09-12 09:22:41.896419'),(54,'allocation','0014_add_name_to_mentor_login','2025-09-12 09:22:41.901877'),(55,'allocation','0015_remove_mentor_login_name','2025-09-12 09:22:41.904647'),(56,'allocation','0016_mentor_login_name','2025-09-12 09:22:41.906794'),(57,'allocation','0017_delete_mentor_login','2025-09-12 09:22:41.907703'),(58,'allocation','0018_mentor_login','2025-09-12 09:24:11.075166'),(59,'allocation','0019_delete_mentor','2025-09-12 12:15:20.156056'),(60,'allocation','0020_mentor','2025-09-12 12:16:09.017462'),(61,'allocation','0021_delete_mentor','2025-09-12 12:51:23.607502'),(62,'allocation','0022_mentor','2025-09-12 12:51:58.902687'),(63,'allocation','0023_allocate_mentor','2025-09-21 04:06:51.464813'),(64,'allocation','0024_delete_allocate_mentor','2025-09-21 04:26:01.506764'),(65,'allocation','0025_allocate_mentor','2025-09-21 04:26:21.382696'),(66,'allocation','0026_delete_allocate_mentor','2025-09-21 04:35:17.423247'),(67,'allocation','0027_allocate_mentor','2025-09-21 05:04:52.967187'),(68,'allocation','0028_delete_team','2025-10-07 04:25:58.335723'),(69,'allocation','0029_team','2025-10-07 04:34:44.171663'),(70,'allocation','0030_allocationresult','2025-10-07 05:10:23.488528'),(71,'allocation','0031_delete_team','2025-10-13 08:36:06.347976'),(72,'allocation','0032_team','2025-10-13 08:48:19.697931'),(73,'allocation','0033_approvedteam_modifyrequest','2025-10-22 07:08:13.896515'),(74,'allocation','0034_delete_modifyrequest','2025-10-22 07:13:41.465875'),(75,'allocation','0035_modifyrequest','2025-10-22 07:19:22.191035'),(76,'allocation','0036_zerothreviewremark','2025-12-23 04:56:25.496421'),(77,'allocation','0037_delete_zerothreviewremark','2025-12-23 07:49:56.797762'),(78,'allocation','0038_zerothreviewremark','2025-12-23 07:50:35.326352'),(79,'allocation','0039_delete_zerothreviewremark','2025-12-24 13:00:13.062453'),(80,'allocation','0040_zerothreviewremark','2025-12-24 13:14:59.872104'),(81,'allocation','0041_delete_zerothreviewremark','2025-12-24 13:18:22.197306'),(82,'allocation','0042_zerothreviewremark_and_more','2025-12-24 13:37:49.372679'),(83,'allocation','0043_delete_zerothreviewremark','2025-12-24 13:37:49.380947'),(84,'allocation','0044_zerothreviewremark_and_more','2025-12-24 13:40:56.367804'),(85,'allocation','0045_delete_zerothreviewremark','2025-12-24 13:40:56.388145'),(86,'allocation','0046_zerothreviewremark_and_more','2025-12-24 13:45:10.707571'),(87,'allocation','0047_announcement_announcementstatus','2025-12-25 09:11:45.694139'),(88,'allocation','0048_remove_announcementstatus_announcement_and_more','2025-12-25 14:44:17.623876'),(89,'allocation','0049_announcement_announcementstatus','2025-12-25 14:46:08.984783'),(90,'allocation','0050_delete_announcementstatus','2025-12-25 15:57:29.784052'),(91,'allocation','0051_announcementstatus','2025-12-25 15:59:19.498748'),(92,'allocation','0052_remove_announcementstatus_announcement_and_more','2025-12-25 16:02:02.416708'),(93,'allocation','0053_announcement_announcementstatus','2025-12-25 16:02:47.760774'),(94,'allocation','0054_coordinator_login','2025-12-26 03:58:33.289331'),(95,'allocation','0055_remove_announcementstatus_announcement_and_more','2025-12-26 06:04:37.916422'),(96,'allocation','0056_announcement_announcementstatus','2025-12-26 06:05:36.089197'),(97,'allocation','0057_projectdocument','2026-01-21 05:32:52.730845'),(98,'allocation','0058_projectfile','2026-01-21 07:39:16.776100'),(99,'allocation','0059_delete_projectfile','2026-01-26 06:10:10.753686'),(100,'allocation','0060_projectfile','2026-01-26 06:10:29.988523'),(101,'allocation','0061_delete_projectfile','2026-01-26 06:21:24.368883'),(102,'allocation','0062_projectfile','2026-01-26 06:22:39.066136');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;

/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1nj0urwpvd605c4zw917qwzj48bc4dyj','.eJyrViouKU1JzSuJz0xRslIyMgl1DjYyMFTSgYvnJeamAmW8E8sy85CEk9MLEoHCFnrGZsiiOYnFxUBh52BXXSelWgCvwR4y:1v7rdI:_KolVamDZanqOumszW0Vla0cK_VuGwD_mB4DcAVit_E','2025-10-26 08:40:48.916757'),('99ow4sylokbzny76k3mjy07mrnbt69db','eyJjb29yZGluYXRvcl9pZCI6MSwidXNlcm5hbWUiOiIyMDAwMSIsIm1lbnRvcl9uYW1lIjoiWlpaIn0:1vbYqN:UuAROFEHt9vlcRvMPutZqD6TTX_kKuPrzeIeL956Ea8','2026-01-16 06:41:03.339531'),('ci5ezqfyrq1ahq3avo06verb3v0ilqm0','.eJyrViouKU1JzSuJz0xRslIyMgl1DjYyNFfSgYvnJeamAmUc8_ISC_LzixLzMpEkk9MLEoGSFnqmRsiiOYnFxUBh52BXXSelWgCMhCC0:1v7rfQ:6aOn5Xbkcgls3xiq6x5wxoqxSUvxeE9Z9E2bh-1LE3Y','2025-10-26 08:43:00.074509'),('clmztk8yyv2g61j60tcazuuxdc8hrmjx','.eJyrVspNzSvJL4rPTFGyMtRRKi1OLcpLzE1VslIyNDAwMFTSgSmAigaXFqUWZyh4l-YmFgEli0tKU4DyYO1KRiahzsFGhhZI4lBdboklGZm5iUgSyekFiUAJcz0jY2TRnMTiYqCwc7CrrpNSLQDyZTLv:1vHHgN:Lw3B2Y264EMh5XRuAkMhjmbTsATcPgMTYEvRvqPdjNo','2025-11-21 08:18:55.605391'),('mqatxxcguj1psmn4k3i73bafrr8u9j16','.eJyrVspNzSvJL4rPTFGyMtRRKi1OLcpLzE1VslIyNDAwMFTSgSmAigaXFqUWZyh4l-YmFgEli0tKU4DyYO1KRiahzsFGhqZI4lBdPonZxRm5mUgSyekFiUAJSz1jM2TRnMTiYqCwc7CrrpNSLQD1LjMB:1vm1h5:-P0R0nJ4I1O0wVWsr6NEyjjj7E1i-MbpXjOmkS4T-kc','2026-02-14 03:30:43.168789');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;


/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;

-- Dump completed on 2026-01-31 11:22:31
SET FOREIGN_KEY_CHECKS=1;
