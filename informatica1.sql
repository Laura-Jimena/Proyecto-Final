-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-11-2023 a las 21:48:54
-- Versión del servidor: 8.2.0
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `informatica1`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `citas`
--

CREATE TABLE `citas` (
  `id` int NOT NULL,
  `id_paciente` int DEFAULT NULL,
  `id_medico` int DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `estado` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `citas`
--

INSERT INTO `citas` (`id`, `id_paciente`, `id_medico`, `fecha`, `hora`, `estado`) VALUES
(3, 1, 1, '2023-12-25', '19:30:00', NULL),
(4, 6, 1, '2023-12-25', '16:30:00', NULL),
(5, 9, 1, '2023-12-02', '12:00:00', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `disponibilidad_medicos`
--

CREATE TABLE `disponibilidad_medicos` (
  `id_disponibilidad` int NOT NULL,
  `id_medico` int DEFAULT NULL,
  `fecha_disponible` date DEFAULT NULL,
  `hora` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `disponibilidad_medicos`
--

INSERT INTO `disponibilidad_medicos` (`id_disponibilidad`, `id_medico`, `fecha_disponible`, `hora`) VALUES
(1, 2, '2023-12-15', '08:30:00'),
(7, 4, '2023-12-10', '08:30:00'),
(8, 3, '2023-12-15', '16:30:00'),
(9, 3, '2023-11-26', '16:30:00'),
(10, 1, '2023-11-30', '12:30:00'),
(11, 1, '2023-11-26', '15:30:00'),
(12, 1, '2023-11-25', '08:30:00'),
(13, 1, '2023-12-01', '16:30:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicos`
--

CREATE TABLE `medicos` (
  `id` int NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `cedula` varchar(100) DEFAULT NULL,
  `especialidad` varchar(255) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `medicos`
--

INSERT INTO `medicos` (`id`, `nombre`, `cedula`, `especialidad`, `telefono`, `email`) VALUES
(1, 'Juan Hernandez', '24134568', 'NEUROLOGIA', '3216549870', 'juan@u'),
(2, 'Maria Domiguez', '12312312', 'TRAUMATOLOGÍA', '3165698596', 'mariadom@udea'),
(3, 'Luis Cardona', '12345678', 'C. PLASTICA', '3254124587', 'luisc@plast.com'),
(4, 'Daniel Ramirez', '8745693', 'MEDICINA INTERNA', '3247894562', 'danielr@udea'),
(5, 'Juliana Garcia', '7125896', 'GINECO Y OBSTETRICIA', '3215265458', 'julig@udea');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pacientes`
--

CREATE TABLE `pacientes` (
  `id` int NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `cedula` varchar(255) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `genero` varchar(10) DEFAULT NULL,
  `tipo_sangre` varchar(10) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `pacientes`
--

INSERT INTO `pacientes` (`id`, `nombre`, `cedula`, `fecha_nacimiento`, `genero`, `tipo_sangre`, `telefono`, `direccion`, `email`) VALUES
(1, 'Laura Munevar', '1054090489', '2023-02-11', 'FEMENINO', 'O+', '3223502665', 'Calle 60', 'laura@udea'),
(5, 'Juanito Perez', '11111111', '2003-02-28', 'Femenino', 'A+', '3254569871', 'Calle 69', 'juanitop@udea'),
(6, 'Pepito Perez', '147258369', '2001-11-25', 'Masculino', 'A+', '3158569632', 'Calle 70', 'pepito@udea'),
(7, 'Maria Torres', '740147525', '2006-03-11', 'Masculino', 'AB-', '3216542121', 'Carrera 15', 'Torres1@udea'),
(8, 'Luisa Mora', '12396385', '1998-03-12', 'Femenino', 'B-', '3245689875', 'Avenida luis amigo', 'luisa@udea'),
(9, 'Pedro Martinez', '145145145', '1963-03-01', 'Masculino', 'A+', '3216218574', 'Calle60', 'p.mart@udea');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `citas`
--
ALTER TABLE `citas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_paciente` (`id_paciente`),
  ADD KEY `id_medico` (`id_medico`);

--
-- Indices de la tabla `disponibilidad_medicos`
--
ALTER TABLE `disponibilidad_medicos`
  ADD PRIMARY KEY (`id_disponibilidad`),
  ADD KEY `id_medico` (`id_medico`);

--
-- Indices de la tabla `medicos`
--
ALTER TABLE `medicos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `citas`
--
ALTER TABLE `citas`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `disponibilidad_medicos`
--
ALTER TABLE `disponibilidad_medicos`
  MODIFY `id_disponibilidad` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `medicos`
--
ALTER TABLE `medicos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `pacientes`
--
ALTER TABLE `pacientes`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `citas`
--
ALTER TABLE `citas`
  ADD CONSTRAINT `citas_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `pacientes` (`id`),
  ADD CONSTRAINT `citas_ibfk_2` FOREIGN KEY (`id_medico`) REFERENCES `medicos` (`id`);

--
-- Filtros para la tabla `disponibilidad_medicos`
--
ALTER TABLE `disponibilidad_medicos`
  ADD CONSTRAINT `disponibilidad_medicos_ibfk_1` FOREIGN KEY (`id_medico`) REFERENCES `medicos` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
