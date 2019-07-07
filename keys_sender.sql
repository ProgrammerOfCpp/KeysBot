-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Июл 07 2019 г., 13:10
-- Версия сервера: 5.7.21
-- Версия PHP: 7.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `keys_sender`
--

-- --------------------------------------------------------

--
-- Структура таблицы `favourite`
--

DROP TABLE IF EXISTS `favourite`;
CREATE TABLE IF NOT EXISTS `favourite` (
  `user_id` int(11) NOT NULL,
  `lot_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `lots`
--

DROP TABLE IF EXISTS `lots`;
CREATE TABLE IF NOT EXISTS `lots` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` text CHARACTER SET utf8mb4 NOT NULL,
  `description` text CHARACTER SET utf8mb4 NOT NULL,
  `bunch` text CHARACTER SET utf8mb4 NOT NULL,
  `basic_keys_count` int(11) NOT NULL,
  `price` double NOT NULL,
  `likes` int(11) NOT NULL DEFAULT '0',
  `dislikes` int(11) NOT NULL DEFAULT '0',
  `active` tinyint(1) NOT NULL DEFAULT '1',
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Структура таблицы `transactions`
--

DROP TABLE IF EXISTS `transactions`;
CREATE TABLE IF NOT EXISTS `transactions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(256) CHARACTER SET utf8mb4 NOT NULL,
  `sum` double NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `payment_type` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

--
-- Дамп данных таблицы `transactions`
--

INSERT INTO `transactions` (`id`, `address`, `sum`, `time`, `payment_type`) VALUES
(9, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 0.0001, '2019-06-29 08:42:40', 'buy'),
(10, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 1, '2019-06-29 12:14:25', 'buy'),
(11, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 1, '2019-06-29 12:15:01', 'buy'),
(12, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 0.0001, '2019-06-29 12:19:49', 'buy'),
(13, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 0.3, '2019-06-29 12:20:29', 'out'),
(14, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 0.0001, '2019-06-29 13:11:09', 'buy'),
(15, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 0.0001, '2019-06-29 13:12:34', 'buy'),
(16, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 0.0001, '2019-06-29 13:13:38', 'buy'),
(17, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 0.0001, '2019-06-29 13:14:25', 'buy'),
(18, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 0.0001, '2019-06-29 13:21:19', 'buy'),
(19, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 0.0001, '2019-06-29 13:22:45', 'buy'),
(20, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 0.0001, '2019-06-29 13:23:06', 'buy'),
(21, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 0.1, '2019-06-29 13:25:17', 'out'),
(22, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 0.00001910205079617348, '2019-06-29 19:22:59', 'buy'),
(23, '1ByNvH5vEwPvq3sSTGm9gb2QimDtHK5yaj', 0.000019076560915751233, '2019-06-29 19:24:28', 'buy'),
(24, '1KwQNsiASBF8SRiJ6Z3uXi5ZpFv9vRJyri ', 0.00000010128115842495259, '2019-06-30 09:55:58', 'buy'),
(25, '1KwQNsiASBF8SRiJ6Z3uXi5ZpFv9vRJyri ', 0.00000010128115842495259, '2019-06-30 09:56:25', 'buy'),
(26, '1KwQNsiASBF8SRiJ6Z3uXi5ZpFv9vRJyri ', 0.00000010129327393367123, '2019-06-30 09:58:16', 'buy'),
(27, '1KwQNsiASBF8SRiJ6Z3uXi5ZpFv9vRJyri ', 0.0000001015556389493924, '2019-06-30 10:01:45', 'buy'),
(28, '1KwQNsiASBF8SRiJ6Z3uXi5ZpFv9vRJyri', 0.00009973025951034677, '2019-06-30 17:28:10', 'buy');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL,
  `menu_id` varchar(256) CHARACTER SET utf8mb4 NOT NULL DEFAULT 'StartMenu',
  `prev_menu` varchar(256) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `lang` varchar(256) CHARACTER SET utf8mb4 NOT NULL DEFAULT 'en',
  `lot_title` varchar(256) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `lot_description` varchar(1024) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `lot_price` double NOT NULL DEFAULT '0',
  `lot_keys` varchar(1024) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `lot_id` int(11) NOT NULL DEFAULT '0',
  `priv_key` varchar(256) CHARACTER SET utf8mb4 NOT NULL,
  `address` varchar(256) CHARACTER SET utf8mb4 NOT NULL,
  `transaction_address` varchar(256) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `transaction_sum` double NOT NULL DEFAULT '0',
  `balance` double NOT NULL DEFAULT '0',
  `loaded` double NOT NULL DEFAULT '0',
  `spent` double NOT NULL DEFAULT '0',
  `withdraw_address` varchar(256) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `payment_type` varchar(256) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `show_all` int(11) NOT NULL DEFAULT '1',
  `notify` int(11) NOT NULL DEFAULT '1',
  `is_admin` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `menu_id`, `prev_menu`, `lang`, `lot_title`, `lot_description`, `lot_price`, `lot_keys`, `lot_id`, `priv_key`, `address`, `transaction_address`, `transaction_sum`, `balance`, `loaded`, `spent`, `withdraw_address`, `payment_type`, `show_all`, `notify`, `is_admin`) VALUES
(171467289, 'SettingsMenu', 'WalletMenu', 'rus', 'FISTING', 'ЕСТЬ ПРОБИТИЕ', 300, '👊👊👊👊', 17, '5Ki5TUYQcKnnpyeXtWbuWy7NX6QkmhiQTkYKACiVyaHd9EcC7Xy', '15wEo5ERndR9LGM4GFQfHRSuGWVb7CYTve', '', 0, 0, 0, 0, '', '', 1, 1, 1),
(446188415, 'SettingsMenu', 'InputKeysMenu', 'rus', 'а', 'а', 0.98754, 'ф', 0, 'KzGbd9V19qPw9SJmp6caVmVo29n6qaTTbRnzZ5sgfdXB8F4XfF27', '1HhaxxsTL2vdBRQiqVzx8RPKTfn5ZTbuHR', '', 0, 0.000612, 0, 0, '', '', 1, 1, 0),
(632009318, 'SupportMenu', 'SupportMenu', 'en', '', '', 0, '', 16, 'KyiXBWTahd5y8kUzG9FH4gTz1MHeeLPKu5PctcKzxHEsdnLShzhU', '1KwQNsiASBF8SRiJ6Z3uXi5ZpFv9vRJyri', '1HhaxxsTL2vdBRQiqVzx8RPKTfn5ZTbuHR', 0.00009973025951034677, 0.00001505, 0.00003505, 0.00009973, '', 'buy', 1, 1, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
