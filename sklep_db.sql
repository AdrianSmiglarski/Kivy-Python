-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 05 Sty 2020, 17:47
-- Wersja serwera: 10.4.8-MariaDB
-- Wersja PHP: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `sklep_db`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `adresy`
--

CREATE TABLE `adresy` (
  `id_adresu` int(11) NOT NULL,
  `ulica` varchar(32) NOT NULL,
  `nr_domu` varchar(10) NOT NULL,
  `nr_lokalu` varchar(10) DEFAULT NULL,
  `kod_pocztowy` varchar(6) NOT NULL,
  `miejscowosc` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `adresy`
--

INSERT INTO `adresy` (`id_adresu`, `ulica`, `nr_domu`, `nr_lokalu`, `kod_pocztowy`, `miejscowosc`) VALUES
(1, 'Krakowska', '101A', '', '11-111', 'Warszawa'),
(2, 'Warszawska', '52B', '', '11-111', 'Warszawa'),
(3, 'Sienkiewicza', '1B', '', '22-222', 'Kielce'),
(4, 'Mała', '123', '22', '34-567', 'Gdańsk'),
(5, 'Duża', '101A', '', '65-234', 'Białystok'),
(6, 'Prosta', '32', '11', '21-123', 'Radom');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `oddzialy`
--

CREATE TABLE `oddzialy` (
  `id_oddzialu` int(11) NOT NULL,
  `nazwa` varchar(64) NOT NULL,
  `id_adresu` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `oddzialy`
--

INSERT INTO `oddzialy` (`id_oddzialu`, `nazwa`, `id_adresu`) VALUES
(1, 'MARKET NR.1', 1),
(2, 'MARKET CENTRUM', 3),
(3, 'MARKET NR.2', 2),
(4, 'MARKET - Białystok', 5),
(5, 'MARKET', 4);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `stany`
--

CREATE TABLE `stany` (
  `id_stanu` int(11) NOT NULL,
  `ilosc` int(11) NOT NULL,
  `id_oddzialu` int(11) DEFAULT NULL,
  `id_towaru` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `stany`
--

INSERT INTO `stany` (`id_stanu`, `ilosc`, `id_oddzialu`, `id_towaru`) VALUES
(1, 125, 1, 1),
(2, 25, 1, 4),
(3, 200, 1, 3),
(4, 50, 1, 2),
(5, 16, 2, 5),
(6, 75, 2, 4),
(7, 100, 2, 1),
(8, 67, 2, 2),
(9, 75, 3, 3),
(10, 24, 3, 2),
(11, 80, 3, 4),
(12, 15, 3, 5),
(13, 1, 4, 1),
(14, 2, 4, 1),
(15, 3, 4, 1),
(16, 4, 4, 1),
(17, 10, 5, 1),
(18, 20, 5, 2),
(19, 30, 5, 3),
(20, 40, 5, 4);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `towary`
--

CREATE TABLE `towary` (
  `id_towaru` int(11) NOT NULL,
  `nazwa` varchar(32) NOT NULL,
  `cena` decimal(38,2) NOT NULL,
  `opis` varchar(128) NOT NULL,
  `zdjecie` varchar(360) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `towary`
--

INSERT INTO `towary` (`id_towaru`, `nazwa`, `cena`, `opis`, `zdjecie`) VALUES
(1, 'Książka - A', '39.99', 'Bardzo fajna ksiazka', 'http://images.unsplash.com/photo-1549122728-f519709caa9c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2125&q=80'),
(2, 'Książka - B', '89.99', 'Bestseller', 'http://images.unsplash.com/photo-1521123845560-14093637aa7d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80'),
(3, 'Młotek', '9.99', 'Praktyczne narzedzie', 'https://scontent.fwaw3-2.fna.fbcdn.net/v/t1.0-9/12439034_1685673878343033_2805246231197812162_n.jpg?_nc_cat=104&_nc_oc=AQn-22B8C71C3x153OBN0muyItzRNxDqvbxgUbdbBtiq2oDRT8819KY0OXRhp3ouXeA&_nc_ht=scontent.fwaw3-2.fna&oh=634579520def416e9aeb2928c8294f3b&oe=5EA33C5B'),
(4, 'Rower', '599.99', 'Ma dwa koła', 'http://images.unsplash.com/photo-1532298229144-0ec0c57515c7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1308&q=80'),
(5, 'Hulajnoga', '149.99', 'Hulaj dusza piekła nie ma', 'http://images.unsplash.com/photo-1541903565640-451825e5aaf8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=647&q=80');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `adresy`
--
ALTER TABLE `adresy`
  ADD PRIMARY KEY (`id_adresu`);

--
-- Indeksy dla tabeli `oddzialy`
--
ALTER TABLE `oddzialy`
  ADD PRIMARY KEY (`id_oddzialu`),
  ADD KEY `oddzialy` (`id_adresu`);

--
-- Indeksy dla tabeli `stany`
--
ALTER TABLE `stany`
  ADD PRIMARY KEY (`id_stanu`),
  ADD KEY `stany` (`id_oddzialu`),
  ADD KEY `id_towaru` (`id_towaru`);

--
-- Indeksy dla tabeli `towary`
--
ALTER TABLE `towary`
  ADD PRIMARY KEY (`id_towaru`);

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `oddzialy`
--
ALTER TABLE `oddzialy`
  ADD CONSTRAINT `oddzialy` FOREIGN KEY (`id_adresu`) REFERENCES `adresy` (`id_adresu`);

--
-- Ograniczenia dla tabeli `stany`
--
ALTER TABLE `stany`
  ADD CONSTRAINT `stany` FOREIGN KEY (`id_oddzialu`) REFERENCES `oddzialy` (`id_oddzialu`),
  ADD CONSTRAINT `stany_ibfk_1` FOREIGN KEY (`id_towaru`) REFERENCES `towary` (`id_towaru`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
