SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
(1, 'loyal_loki0510', 'maddulokesh2001@gmail.com', 'pbkdf2:sha256:150000$TfhDWqOr$d4cf40cc6cbfccbdcd1410f9e155ef2aa660620b0439a60c4d74085dbf007a4a');

ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `user`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
COMMIT;

CREATE TABLE `buy` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `productname` varchar(50),
  `productquantity` varchar(50)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `buy` (`id`, `username`, `email`, `productname`, `productquantity`) VALUES
(1, 'loyal_loki0510', 'maddulokesh2001@gmail.com', 'mango', '50');

ALTER TABLE `buy`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `buy`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
COMMIT;

CREATE TABLE `sell` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `productname` varchar(50),
  `productquantity` varchar(50)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `sell` (`id`, `username`, `email`, `productname`, `productquantity`) VALUES
(1, 'loyal_loki0510', 'maddulokesh2001@gmail.com', 'mango', '50');

ALTER TABLE `sell`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `sell`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
COMMIT;
