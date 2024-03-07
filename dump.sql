-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 07, 2024 at 10:34 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `chatbot2024`
--

-- --------------------------------------------------------

--
-- Table structure for table `information`
--

CREATE TABLE `information` (
  `in_id` int(10) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `link` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `message`
--

CREATE TABLE `message` (
  `qa_id` int(10) UNSIGNED NOT NULL,
  `session_id` int(11) NOT NULL,
  `question` text NOT NULL,
  `answer` text NOT NULL,
  `question_time` datetime NOT NULL,
  `answer_time` datetime NOT NULL,
  `comment` text DEFAULT NULL,
  `star` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `message`
--

INSERT INTO `message` (`qa_id`, `session_id`, `question`, `answer`, `question_time`, `answer_time`, `comment`, `star`) VALUES
(1, 9, 'hiệu trưởng trường', 'Hiệu trưởng trường có các nhiệm vụ sau:\n1. Chỉ đạo và tổ chức quản lý các hoạt động của công tác sinh viên.\n2. Xây dựng kế hoạch và tổ chức thực hiện các chủ trương, đường lối của Đảng, chính sách, pháp luật của Nhà nước, các quy định của Bộ Giáo dục và Đào tạo, ngành và địa phương trong công tác sinh viên; tạo điều kiện cho sinh viên thực hiện đầy đủ quyền và nhiệm vụ của mình.\n\nBạn có thể hỏi thêm về:\n- Nhiệm vụ cụ thể của hiệu trưởng trường.\n- Cách hiệu trưởng quản lý và tổ chức các hoạt động của công tác sinh viên.\n- Mối quan hệ giữa hiệu trưởng và các đơn vị trong trường.', '2024-03-03 16:42:23', '2024-03-03 16:42:31', '', NULL),
(2, 9, 'sổ tay sinh viên', 'Tôi không biết\nCác chủ đề liên quan:\n- Quy định lưu trữ hồ sơ sinh viên\n- Hoạt động thanh tra, kiểm tra, giám sát trong trường đại học\n- Khen thưởng cho sinh viên xuất sắc', '2024-03-03 16:47:12', '2024-03-03 16:47:23', '', NULL),
(3, 9, 'sổ tay sinh viên', 'Tôi không biết\n\nCác chủ đề liên quan:\n1. Quy định lưu trữ hồ sơ sinh viên\n2. Điều khoản về hoạt động nghiên cứu sinh viên\n3. Quy định về khen thưởng và đánh giá kết quả học tập cho sinh viên', '2024-03-03 16:47:36', '2024-03-03 16:47:44', '', NULL),
(4, 9, 'chào', 'Tôi không biết\n\nCác chủ đề liên quan:\n1. Thái độ lễ phép, lịch sự trong giao tiếp\n2. Ứng xử lịch sự khi giao dịch công việc\n3. Quy định về giao tiếp và ứng xử trong công sở', '2024-03-03 17:01:11', '2024-03-03 17:01:23', '', NULL),
(5, 9, 'Thái độ lễ phép, lịch sự trong giao tiếp', 'Thái độ lễ phép và lịch sự trong giao tiếp là yếu tố quan trọng giúp tạo ra môi trường giao tiếp tích cực và hiệu quả. Để thể hiện thái độ này, người ta cần:\n- Đảm bảo thái độ lịch sự, nhã nhặn, tôn trọng lẫn nhau.\n- Sử dụng ngôn từ trong sáng, không nói tục, chửi bậy; hành vi và cử chỉ đúng mực.\n- Phải có thái độ lễ phép đối với người khác, bao gồm thầy cô giáo, cán bộ công nhân viên và khách đến làm việc.\n- Giữ gìn các mối quan hệ trong sáng, phù hợp với truyền thống, bản sắc văn hóa dân tộc; không được có những hành vi không lành mạnh.\n- Không xúc phạm danh dự, nhân phẩm, thân thể người khác.\n\nCác chủ đề liên quan:\n1. Cách thức giao tiếp hiệu quả.\n2. Nghệ thuật lắng nghe trong giao tiếp.\n3. Cách xử lý xung đột trong giao tiếp.\n4. Ý nghĩa của thái độ lịch sự và tôn trọng trong giao tiếp.', '2024-03-03 17:04:52', '2024-03-03 17:05:12', '', NULL),
(6, 9, 'sổ tay sinh viên', 'Tôi không biết\nCác chủ đề liên quan:\n- Quy định lưu trữ hồ sơ sinh viên\n- Hoạt động thanh tra, kiểm tra, giám sát trong trường đại học\n- Khen thưởng cho sinh viên xuất sắc', '2024-03-03 17:38:04', '2024-03-03 17:38:10', '', NULL),
(7, 9, 'quy định về trang phục trong trường', 'Quy định về trang phục trong trường bao gồm các điều sau:\n- Trang phục đối với nam: Áo sơ mi hoặc áo thun có tay, quần dài.\n- Trang phục đối với nữ: gọn gàng, lịch sự, phù hợp tác phong người học. Không mặc quần áo quá chật, vải quá mỏng, quá ôm sát như: váy ngắn trên đầu gối, áo sát nách hoặc áo dây, cổ áo quá rộng…\n- Tóc phải gọn gàng.\n- Đi giày hoặc dép có quai hậu, không mang dép lê.\n- Khi đi đến trường người học phải đeo Thẻ sinh viên hoặc Thẻ học viên.\n\nCác chủ đề liên quan:\n1. Quy định về tác phong trong trường học.\n2. Tầm quan trọng của việc tuân thủ quy định về trang phục trong môi trường học tập.\n3. Cách thức xử lý khi vi phạm quy định về trang phục trong trường.', '2024-03-04 20:25:34', '2024-03-04 20:25:46', '', NULL),
(8, 18, 'bạn biết hiệu trưởng trường là ', 'Hiệu trưởng trường là GS.TS. Nguyễn Minh Hà.\n\nBạn có thể hỏi thêm:\n- Phó hiệu trưởng trường là ai?\n- Nhiệm vụ của hiệu trưởng trường là gì?\n- Điều kiện cơ sở vật chất của nhà trọ được đảm bảo như thế nào?', '2024-03-04 20:32:00', '2024-03-04 20:32:08', '', NULL),
(9, 22, 'chào', 'Tôi không biết\n\nCác chủ đề liên quan:\n- Cách chào hỏi lịch sự trong giao tiếp\n- Quy định về ứng xử trong công sở\n- Kỹ năng mềm trong giao tiếp', '2024-03-05 21:21:59', '2024-03-05 21:22:04', '', NULL),
(10, 22, 'Cách chào hỏi lịch sự trong giao tiếp', 'Context: Khi đến các cơ quan, công sở để giao dịch, liên hệ công việc đảm bảo thái độ lễ phép, lịch sự, thẳng thắn; không gây mất trật tự; nhã nhặn khi hỏi và cảm ơn khi được giúp đỡ, phục vụ.\n\nOutput: Trong giao tiếp, để chào hỏi một cách lịch sự, bạn có thể sử dụng các cách chào phổ biến như \"Xin chào\", \"Chào bạn\", \"Chào anh/chị\", \"Xin chào các bạn\". Đồng thời, sau khi nhận được sự giúp đỡ hoặc phục vụ, bạn cũng nên bày tỏ lòng biết ơn bằng cách nói \"Cảm ơn bạn\", \"Cảm ơn anh/chị\", \"Xin cảm ơn\". Điều quan trọng là thể hiện sự lịch sự, nhã nhặn và tôn trọng đối với người khác trong mọi tình huống giao tiếp.\n\nBạn có thể hỏi thêm:\n- Cách ứng xử lịch sự khi gặp người mới?\n- Lợi ích của việc thể hiện sự biết ơn trong giao tiếp?\n- Tại sao thái độ lịch sự quan trọng trong giao tiếp?', '2024-03-05 21:24:37', '2024-03-05 21:24:51', '', NULL),
(11, 22, 'hiệu trưởng trường là ai', 'Hiệu trưởng trường là GS.TS. Nguyễn Minh Hà.<br></br><br></br>Bạn có thể hỏi thêm:<br></br>1. Phó hiệu trưởng trường là ai?<br></br>2. Chức năng và nhiệm vụ của Hiệu trưởng trường là gì?<br></br>3. Hệ thống tổ chức, quản lý công tác sinh viên của trường được quy định như thế nào?', '2024-03-05 21:29:12', '2024-03-05 21:29:17', '', NULL),
(12, 22, ' Hệ thống tổ chức, quản lý công tác sinh viên của trường được quy định như thế nào', 'Hệ thống tổ chức, quản lý công tác sinh viên của trường được quy định bao gồm các thành phần sau:<br></br>- Hiệu trưởng Trường<br></br>- Phòng Công tác sinh viên<br></br>- Khoa<br></br>- Chủ nhiệm lớp sinh viên<br></br><br></br>Các đơn vị và cá nhân có nhiệm vụ và quyền được quy định rõ trong quy chế, bao gồm:<br></br>- Chỉ đạo và tổ chức quản lý các hoạt động của công tác sinh viên.<br></br>- Ban cán sự lớp học phần được ưu tiên cộng điểm rèn luyện và các chế độ khác theo quy định của Trường.<br></br>- Các đơn vị phụ trách công tác sinh viên phối hợp chặt chẽ với các tổ chức đoàn thể trong Trường, gia đình sinh viên, và các cơ quan có liên quan để tổ chức thực hiện tốt công tác sinh viên.<br></br>- Tổ chức tổng kết, đánh giá công tác sinh viên và báo cáo Bộ Giáo dục và Đào tạo kết thúc năm học.<br></br>- Triển khai các dịch vụ công tác xã hội để hỗ trợ sinh viên khuyết tật, sinh viên diện chính sách, và sinh viên có hoàn cảnh đặc biệt khó khăn.<br></br>- Tổ chức và quản lý các dịch vụ sinh viên như internet, điện thoại, nhà ăn, căng tin, trông giữ xe, sân chơi, bãi tập, và thiết chế văn hóa cho sinh viên.<br></br><br></br>Các nội dung và quy định chi tiết khác có thể được tìm hiểu bằng cách tham khảo quy chế hoặc hệ thống quản lý công tác sinh viên của trường. <br></br><br></br>Bạn có thể hỏi thêm về:<br></br>- Nhiệm vụ và quyền của sinh viên trong hệ thống tổ chức, quản lý công tác sinh viên.<br></br>- Cách tổ chức và quản lý công tác sinh viên trong các trường đại học khác.<br></br>- Các chính sách hỗ trợ sinh viên khuyết tật, sinh viên diện chính sách tại trường.', '2024-03-05 21:34:46', '2024-03-05 21:35:01', '', NULL),
(13, 22, 'd', 'sdf', '2024-03-05 21:35:33', '2024-03-05 21:35:37', '', NULL),
(14, 22, 'Kỹ năng mềm trong giao tiếp', 'sdf', '2024-03-05 21:39:21', '2024-03-05 21:39:36', '', NULL),
(15, 22, 'Kỹ năng mềm trong giao tiếp', 'Kỹ năng mềm trong giao tiếp là một khía cạnh quan trọng của kỹ năng mềm nói chung. Để thành công trong giao tiếp, sinh viên cần rèn luyện và phát triển các kỹ năng như kỹ năng lắng nghe, kỹ năng trình bày ý kiến một cách rõ ràng, kỹ năng thuyết phục, kỹ năng đàm phán, kỹ năng xử lý xung đột và kỹ năng xây dựng mối quan hệ. Việc có kỹ năng mềm trong giao tiếp giúp sinh viên tự tin, hiệu quả trong việc truyền đạt thông điệp, giải quyết vấn đề và tạo ra môi trường làm việc tích cực.<br></br><br></br>Các chủ đề liên quan:<br></br>1. Kỹ năng mềm trong làm việc nhóm<br></br>2. Kỹ năng tổ chức công việc<br></br>3. Kỹ năng trình bày ý kiến<br></br>4. Kỹ năng đàm phán<br></br>5. Kỹ năng xử lý xung đột', '2024-03-05 21:40:14', '2024-03-05 21:40:24', '', NULL),
(16, 22, ' Kỹ năng đàm phán', 'Tôi không biết<br></br><br></br>Các chủ đề liên quan:<br></br>1. Kỹ năng giao tiếp<br></br>2. Kỹ năng làm việc nhóm<br></br>3. Kỹ năng tổ chức công việc<br></br>4. Kỹ năng trình bày<br></br>5. Tư duy phản biện', '2024-03-05 21:46:25', '2024-03-05 21:46:32', '', NULL),
(17, 22, 'Kỹ năng đàm phán', 'Tôi không biết  Các chủ đề liên quan: 1. Kỹ năng giao tiếp 2. Kỹ năng làm việc nhóm 3. Kỹ năng tổ chức công việc 4. Kỹ năng trình bày 5. Tư duy phản biện', '2024-03-05 21:48:21', '2024-03-05 21:48:26', '', NULL),
(18, 22, 'hiệu trưởng trường là ai', 'Hiệu trưởng trường là GS.TS. Nguyễn Minh Hà.  Bạn có thể hỏi thêm: - Phó hiệu trưởng trường là ai? - Chức năng và nhiệm vụ của Hiệu trưởng trường là gì? - Hệ thống tổ chức, quản lý công tác sinh viên của trường được quy định như thế nào?', '2024-03-05 21:50:53', '2024-03-05 21:51:00', '', NULL),
(19, 22, 'Cách chào hỏi lịch sự trong giao tiếp', 'sfewfsfes <br>sfsef', '2024-03-05 21:52:00', '2024-03-05 21:52:10', '', NULL),
(20, 22, 'Cách chào hỏi lịch sự trong giao tiếp', ' Context: Khi đến các cơ quan, công sở để giao dịch, liên hệ công việc đảm bảo thái độ lễ phép, lịch sự, thẳng thắn; không gây mất trật tự; nhã nhặn khi hỏi và cảm ơn khi được giúp đỡ, phục vụ.\n\nOutput: Trong giao tiếp, để chào hỏi một cách lịch sự, bạn có thể sử dụng các cách chào như \"Xin chào\", \"Chào bạn\", \"Chào anh/chị\", \"Xin chào quý vị\". Đồng thời, khi chào hỏi, cần kết hợp với nụ cười, ánh mắt lịch sự và thân thiện để tạo ấn tượng tốt. \n\nBạn có thể hỏi thêm:\n- Cách kết thúc cuộc trò chuyện một cách lịch sự\n- Cách thể hiện sự biểu lộ cảm ơn trong giao tiếp\n- Cách đề xuất ý kiến một cách lịch sự ', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 'Ổn rất ổn', NULL),
(21, 22, 'hiệu trưởng trường là ai', 'Hiệu trưởng trường là GS.TS. Nguyễn Minh Hà.<br /><br />Bạn có thể hỏi thêm:<br />1. Phó hiệu trưởng trường là ai?<br />2. Chức năng và nhiệm vụ của Hiệu trưởng trường là gì?<br />3. Hệ thống tổ chức, quản lý công tác sinh viên của trường được quy định như thế nào?', '2024-03-05 22:01:43', '2024-03-05 22:01:49', '', NULL),
(22, 22, 'response', 'Tôi không biết\n\nCác chủ đề liên quan:\n- Cách ứng xử lịch sự khi giao dịch tại cơ quan, công sở\n- Quy định về việc sử dụng email trong giao tiếp\n- Quy định về việc viết email lịch sự và ngắn gọn\n- Quy định về việc chuyển học chương trình trong trường học', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '', 3),
(23, 22, 'Kỹ năng mềm trong giao tiếp', 'Kỹ năng mềm trong giao tiếp bao gồm các kỹ năng như:<br />- Kỹ năng lắng nghe: Khả năng tập trung và hiểu rõ ý kiến của người khác.<br />- Kỹ năng trình bày: Khả năng diễn đạt ý kiến một cách rõ ràng, logic và thuyết phục.<br />- Kỹ năng đàm phán: Khả năng thương lượng và đạt được sự đồng thuận trong các cuộc trao đổi ý kiến.<br />- Kỹ năng tự tin: Khả năng tự tin trong giao tiếp, biểu đạt ý kiến một cách mạnh mẽ và chắc chắn.<br />- Kỹ năng lịch sự: Biết cách ứng xử, trao đổi thông tin một cách lịch sự và tôn trọng đối tác.<br /><br />Các chủ đề liên quan:<br />- Cách cải thiện kỹ năng giao tiếp.<br />- Ý nghĩa của kỹ năng mềm trong công việc.<br />- Cách thức rèn luyện kỹ năng giao tiếp hiệu quả.', '2024-03-05 22:11:17', '2024-03-05 22:11:27', '', 2),
(24, 22, 'Cách chào hỏi lịch sự trong giao tiếp', 'Context: Khi đến các cơ quan, công sở để giao dịch, liên hệ công việc đảm bảo thái độ lễ phép, lịch sự, thẳng thắn; không gây mất trật tự; nhã nhặn khi hỏi và cảm ơn khi được giúp đỡ, phục vụ.<br /><br />Output: Trong giao tiếp, để chào hỏi một cách lịch sự, bạn có thể sử dụng các cách chào hỏi như \"Xin chào\", \"Chào bạn\", \"Chào anh/chị\", \"Xin chào các bạn\". Đồng thời, sau khi nhận được sự giúp đỡ, hãy nhớ cảm ơn bằng cách nói \"Cảm ơn bạn\", \"Cảm ơn anh/chị\", \"Cảm ơn rất nhiều\". Điều quan trọng là giữ thái độ lịch sự, nhã nhặn và tôn trọng đối với người khác trong mọi tình huống giao tiếp.<br /><br />Bạn có thể hỏi thêm:<br />- Cách ứng xử lịch sự trong giao tiếp hàng ngày<br />- Cách giao tiếp hiệu quả trong công việc<br />- Tại sao lịch sự và thân thiện quan trọng trong giao tiếp?', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 'ao dịch, liên hệ công việc đảm bảo thái độ lễ phép, lịch sự, thẳng thắn; không gây mất trật tự; nhã nhặn khi hỏi và cảm ơn khi được giúp đỡ, phục vụ.<br /><br />Output: Trong giao tiếp, đ', 4),
(25, 23, 'quy định về câu lạc bộ của trường', 'Tôi không biết<br /><br />Các chủ đề liên quan:<br />1. Quy định về hoạt động sinh viên trong trường.<br />2. Các hoạt động ngoại khóa của sinh viên.<br />3. Các câu lạc bộ sinh viên tại trường.', '2024-03-06 13:26:58', '2024-03-06 13:27:09', '', 0);

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `role_id` int(10) UNSIGNED NOT NULL,
  `role_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `session`
--

CREATE TABLE `session` (
  `session_id` int(10) UNSIGNED NOT NULL,
  `name` text DEFAULT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `session`
--

INSERT INTO `session` (`session_id`, `name`, `start_time`, `end_time`, `user_id`) VALUES
(6, 'safe', '2024-03-02 16:18:18', NULL, 3),
(8, 'session1', '0000-00-00 00:00:00', '2024-03-03 18:31:13', 2),
(9, 'session2', '0000-00-00 00:00:00', '2024-03-06 13:25:26', 2),
(10, 'session', '0000-00-00 00:00:00', '2024-03-06 13:25:40', 2),
(11, 'session', '0000-00-00 00:00:00', '2024-03-03 18:29:46', 2),
(12, 'session', '0000-00-00 00:00:00', '2024-03-03 18:29:02', 2),
(13, 'session3', '0000-00-00 00:00:00', '2024-03-03 18:35:08', 2),
(14, 'session6', '0000-00-00 00:00:00', '2024-03-06 13:25:43', 2),
(15, 'session 2024-03-03 18:52:25', '0000-00-00 00:00:00', '2024-03-06 13:25:22', 2),
(16, 'session 2024-03-03 19:51:42', '0000-00-00 00:00:00', '2024-03-04 21:12:37', 2),
(17, 'session 2024-03-04 03:17:23', '2024-03-04 03:17:23', '2024-03-04 03:17:23', 18),
(18, 'session 2024-03-04 17:18:41', '0000-00-00 00:00:00', '2024-03-06 13:25:42', 2),
(19, 'session 2024-03-05 20:19:23', '2024-03-05 20:19:23', '2024-03-05 20:19:23', 4),
(20, 'session 2024-03-05 20:19:23', '2024-03-05 20:19:23', '2024-03-05 20:19:23', 4),
(21, 'session 2024-03-05 20:21:24', '2024-03-05 20:21:24', '2024-03-05 20:21:24', 3),
(22, 'session 2024-03-05 20:23:25', '0000-00-00 00:00:00', '2024-03-05 21:10:01', 6),
(23, 'session 2024-03-06 13:26:24', '0000-00-00 00:00:00', '2024-03-06 13:26:29', 9);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(10) UNSIGNED NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `full_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `username`, `password`, `full_name`, `email`, `status`, `img`, `role_id`) VALUES
(2, 'john_doe', 'password123', 'John Doe', 'john@example.com', 1, 'https://th.bing.com/th/id/OIP.Iy0tmJanZeN5ceMP5uToLQAAAA?&w=160&h=240&c=7&dpr=1.3&pid=ImgDet', 1),
(3, 'john_doe2', 'password123', 'John Doe', 'john@example.com', 1, 'avatar.jpg', 1),
(4, 'john_doe3', 'password123', 'John Doe', 'john@example.com', 1, 'avatar.jpg', 1),
(5, 'john_doe4', 'password123', 'John Doe', 'john@example.com', 1, 'avatar.jpg', 1),
(6, '1', '1', '', '', 1, '', 1),
(7, '2', '1', '', '', 1, '', 1),
(8, '3', '1', '', '', 1, '', 1),
(9, '4', '1', '', '', 1, '', 1),
(10, '5', '1', '', '', 1, '', 1),
(11, '6', '1', '', '', 1, '', 1),
(12, '7', '1', '', '', 1, '', 1),
(13, '8', '1', '', '', 1, '', 1),
(14, '9', '1', '', '', 1, '', 1),
(15, '10', '1', '', '', 1, '', 1),
(16, '11', '1', '', '', 1, '', 1),
(17, '11', '1', '', '', 1, '', 1),
(18, '12', '1', '', '', 1, '', 1),
(19, '13', '1', '', '', 1, '', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `information`
--
ALTER TABLE `information`
  ADD PRIMARY KEY (`in_id`);

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`qa_id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `session`
--
ALTER TABLE `session`
  ADD PRIMARY KEY (`session_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `information`
--
ALTER TABLE `information`
  MODIFY `in_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `message`
--
ALTER TABLE `message`
  MODIFY `qa_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `role`
--
ALTER TABLE `role`
  MODIFY `role_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `session`
--
ALTER TABLE `session`
  MODIFY `session_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
