-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 13, 2024 at 07:33 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `membership_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendances`
--

CREATE TABLE `attendances` (
  `id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  `check_in_time` datetime DEFAULT current_timestamp(),
  `attendance_number` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendances`
--

INSERT INTO `attendances` (`id`, `member_id`, `check_in_time`, `attendance_number`) VALUES
(1, 1, '2024-10-10 21:13:02', 1),
(2, 1, '2024-10-10 21:20:44', 2),
(3, 1, '2024-10-10 21:20:58', 3),
(4, 1, '2024-10-10 21:21:00', 4),
(5, 1, '2024-10-10 21:21:03', 5),
(6, 1, '2024-10-12 14:37:59', 1),
(7, 1, '2024-10-12 14:38:20', 2),
(8, 1, '2024-10-12 14:38:23', 3),
(9, 1, '2024-10-12 14:41:51', 4),
(10, 1, '2024-10-12 17:10:23', 5),
(11, 1, '2024-10-12 18:02:57', 1),
(12, 1, '2024-10-12 18:03:37', 2),
(13, 1, '2024-10-12 18:03:42', 3),
(14, 1, '2024-10-12 18:03:50', 4),
(15, 1, '2024-10-12 18:03:55', 5),
(16, 1, '2024-10-16 14:29:18', 1),
(17, 2, '2024-10-17 14:57:09', 1),
(18, 2, '2024-10-17 14:57:13', 2),
(19, 2, '2024-10-17 14:57:19', 3),
(20, 2, '2024-10-17 14:57:23', 4),
(21, 2, '2024-10-17 14:57:27', 5),
(22, 2, '2024-10-17 15:17:03', 1),
(23, 2, '2024-10-17 15:17:06', 2),
(24, 2, '2024-10-17 15:17:09', 3),
(25, 2, '2024-10-17 15:17:11', 4),
(26, 2, '2024-10-17 15:17:14', 5),
(27, 2, '2024-10-17 15:17:17', 1),
(28, 2, '2024-10-17 15:17:23', 2),
(29, 2, '2024-10-17 15:17:25', 3),
(30, 2, '2024-10-17 15:17:28', 4),
(31, 2, '2024-10-17 15:17:30', 5),
(32, 2, '2024-10-17 15:17:32', 1),
(33, 2, '2024-10-17 15:17:35', 2);

-- --------------------------------------------------------

--
-- Table structure for table `members`
--

CREATE TABLE `members` (
  `id` int(11) NOT NULL,
  `code` varchar(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `transport_type` varchar(10) NOT NULL,
  `registration_date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `members`
--

INSERT INTO `members` (`id`, `code`, `name`, `transport_type`, `registration_date`) VALUES
(1, '123', 'Frederick', 'bus', '2024-10-10 21:11:43'),
(2, '321', 'Armando', 'travel', '2024-10-16 14:29:43');

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `id` int(11) NOT NULL,
  `member_id` int(11) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `payment_date` datetime DEFAULT current_timestamp(),
  `attendance_cycle` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`id`, `member_id`, `amount`, `payment_date`, `attendance_cycle`) VALUES
(1, 1, 500000.00, '2024-10-10 21:21:03', 1),
(2, 1, 500000.00, '2024-10-12 17:10:23', 2),
(3, 1, 500000.00, '2024-10-12 18:03:55', 3),
(4, 2, 250000.00, '2024-10-17 14:57:27', 1),
(5, 2, 250000.00, '2024-10-17 15:17:14', 2),
(6, 2, 250000.00, '2024-10-17 15:17:30', 3);

-- --------------------------------------------------------

--
-- Table structure for table `transport_types`
--

CREATE TABLE `transport_types` (
  `type` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transport_types`
--

INSERT INTO `transport_types` (`type`) VALUES
('bus'),
('travel');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendances`
--
ALTER TABLE `attendances`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_attendance_member` (`member_id`),
  ADD KEY `idx_attendance_check_in` (`check_in_time`);

--
-- Indexes for table `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`),
  ADD KEY `transport_type` (`transport_type`),
  ADD KEY `idx_member_code` (`code`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idx_payment_member` (`member_id`),
  ADD KEY `idx_payment_date` (`payment_date`);

--
-- Indexes for table `transport_types`
--
ALTER TABLE `transport_types`
  ADD PRIMARY KEY (`type`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendances`
--
ALTER TABLE `attendances`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `members`
--
ALTER TABLE `members`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendances`
--
ALTER TABLE `attendances`
  ADD CONSTRAINT `attendances_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`);

--
-- Constraints for table `members`
--
ALTER TABLE `members`
  ADD CONSTRAINT `members_ibfk_1` FOREIGN KEY (`transport_type`) REFERENCES `transport_types` (`type`);

--
-- Constraints for table `payments`
--
ALTER TABLE `payments`
  ADD CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
