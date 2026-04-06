CREATE TABLE DOCENTE (
    cod_doc INT PRIMARY KEY,
    nombre VARCHAR(100),
    especialidad VARCHAR(100)
);

CREATE TABLE RAMO (
    id_ramo INT PRIMARY KEY,
    descripcion VARCHAR(100)
);

CREATE TABLE INFORME (
    folio INT PRIMARY KEY,
    cod_doc INT,
    cod_ramo INT,
    nom_alu VARCHAR(100),
    nota_final DECIMAL(4,1),
    estado VARCHAR(2),
    FOREIGN KEY (cod_doc) REFERENCES DOCENTE(cod_doc),
    FOREIGN KEY (cod_ramo) REFERENCES RAMO(id_ramo)
);

INSERT INTO DOCENTE VALUES
(1, 'Juan Pérez', 'Matemáticas'),
(2, 'María González', 'Lenguaje'),
(3, 'Carlos Soto', 'Historia'),
(4, 'Ana Rojas', 'Ciencias'),
(5, 'Pedro Díaz', 'Inglés');

INSERT INTO RAMO VALUES
(101, 'Álgebra'),
(102, 'Literatura'),
(103, 'Historia de Chile'),
(104, 'Biología'),
(105, 'Inglés Básico');

INSERT INTO INFORME VALUES
(1001, 1, 101, 'Luis Torres',    6.5, 'AP'),
(1002, 2, 102, 'Camila Vega',    5.8, 'AP'),
(1003, 3, 103, 'Diego Muñoz',    4.2, 'RP'),
(1004, 4, 104, 'Sofía Herrera',  6.9, 'AP'),
(1005, 5, 105, 'Martín López',   3.9, 'RP');