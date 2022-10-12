/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80029
 Source Host           : localhost:3306
 Source Schema         : ctf

 Target Server Type    : MySQL
 Target Server Version : 80029
 File Encoding         : 65001

 Date: 12/10/2022 11:14:35
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for buylog
-- ----------------------------
DROP TABLE IF EXISTS `buylog`;
CREATE TABLE `buylog`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `hint_id` int NOT NULL,
  `time` datetime NOT NULL,
  `rank` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `buylogmodel_user_id`(`user_id` ASC) USING BTREE,
  INDEX `buylogmodel_hint_id`(`hint_id` ASC) USING BTREE,
  CONSTRAINT `buylog_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `buylog_ibfk_2` FOREIGN KEY (`hint_id`) REFERENCES `hint` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of buylog
-- ----------------------------
INSERT INTO `buylog` VALUES (1, 1, 1, '2020-05-07 18:08:07', 20);
INSERT INTO `buylog` VALUES (2, 1, 2, '2020-05-07 18:08:07', 20);

-- ----------------------------
-- Table structure for chanllage
-- ----------------------------
DROP TABLE IF EXISTS `chanllage`;
CREATE TABLE `chanllage`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `type_name_id` int NOT NULL,
  `describe` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `rank` int NOT NULL,
  `low` int NOT NULL,
  `people` int NOT NULL,
  `answer` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `file` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `link` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `chanllagemodel_type_name_id`(`type_name_id` ASC) USING BTREE,
  CONSTRAINT `chanllage_ibfk_1` FOREIGN KEY (`type_name_id`) REFERENCES `type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of chanllage
-- ----------------------------
INSERT INTO `chanllage` VALUES (1, '赛题1', 1, '描述', 400, 300, 1, '12312412', '/home/develop/PycharmProjects/tctf/static/uploads/7NjM5kHenpf2z6D4Ia3r', '');
INSERT INTO `chanllage` VALUES (2, '赛题2', 1, '描述', 12312, 150, 2, '12312412', '', 'http://www.baidu.com');
INSERT INTO `chanllage` VALUES (3, '赛题3', 2, '描述', 500, 300, 2, '12312412', '', 'http://www.baidu.com');

-- ----------------------------
-- Table structure for hint
-- ----------------------------
DROP TABLE IF EXISTS `hint`;
CREATE TABLE `hint`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `chanllage_id` int NOT NULL,
  `message` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `sub_rank` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `hintmodel_chanllage_id`(`chanllage_id` ASC) USING BTREE,
  CONSTRAINT `hint_ibfk_1` FOREIGN KEY (`chanllage_id`) REFERENCES `chanllage` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of hint
-- ----------------------------
INSERT INTO `hint` VALUES (1, 2, '阿斯顿福建爱神的箭', 20);
INSERT INTO `hint` VALUES (2, 3, '阿斯顿发送到a', 20);

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `message` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `add_time` date NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of message
-- ----------------------------
INSERT INTO `message` VALUES (1, '阿斯顿福建爱神的箭', '2020-05-07');

-- ----------------------------
-- Table structure for ranklog
-- ----------------------------
DROP TABLE IF EXISTS `ranklog`;
CREATE TABLE `ranklog`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `chanllage_id` int NOT NULL,
  `event` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `answer` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `uptime` datetime NOT NULL,
  `rank` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `ranklogmodel_user_id`(`user_id` ASC) USING BTREE,
  INDEX `ranklogmodel_chanllage_id`(`chanllage_id` ASC) USING BTREE,
  CONSTRAINT `ranklog_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `ranklog_ibfk_2` FOREIGN KEY (`chanllage_id`) REFERENCES `chanllage` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of ranklog
-- ----------------------------
INSERT INTO `ranklog` VALUES (1, 1, 1, 'Corrent', '12312412', '2020-05-07 18:08:07', 500);

-- ----------------------------
-- Table structure for system
-- ----------------------------
DROP TABLE IF EXISTS `system`;
CREATE TABLE `system`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `game_mode` tinyint(1) NOT NULL,
  `start` datetime NOT NULL,
  `end` datetime NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of system
-- ----------------------------
INSERT INTO `system` VALUES (1, 'MyCTF', 0, '2020-05-07 12:12:12', '2020-06-12 12:12:12');

-- ----------------------------
-- Table structure for type
-- ----------------------------
DROP TABLE IF EXISTS `type`;
CREATE TABLE `type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of type
-- ----------------------------
INSERT INTO `type` VALUES (1, 'PWN');
INSERT INTO `type` VALUES (2, 'WEB');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` blob NOT NULL,
  `email` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `admin` tinyint(1) NOT NULL,
  `rank` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'admin', 0x2432622431322443707157396E6C6E37673174496359414A4B2E32772E4B32634C7139756266517767306F30587544364F6B30304D5A69574A55426D, 'admin@admin.com', 1, 970);
INSERT INTO `users` VALUES (2, 'test', 0x24326224313224486862394F55362E4A625A334F41376564414A72706565555947675A487636642E4D4C39736F58723441736B48626133357957544F, 'test@test.com', 0, 0);

SET FOREIGN_KEY_CHECKS = 1;
