DROP TABLE IF EXISTS location;

CREATE TABLE IF NOT EXISTS `location` (
  `locId` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `country` varchar(2) DEFAULT NULL,
  `region` varchar(2) DEFAULT NULL,
  `city` varchar(1000) DEFAULT NULL,
  `postalCode` varchar(10) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `metroCode` int(11) DEFAULT NULL,
  `areaCode` int(11) DEFAULT NULL,
  PRIMARY KEY (`locId`),
  KEY `city` (`city`(767))
) ENGINE=InnoDB  DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS blocks;

CREATE TABLE `blocks` (
  `startIpNum` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `endIpNum` int(11) DEFAULT NULL,
  `locId` int(11) DEFAULT NULL,
  PRIMARY KEY (`startIpNum`)
) ENGINE=InnoDB AUTO_INCREMENT=3758096129 DEFAULT CHARSET=latin1;