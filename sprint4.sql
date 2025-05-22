/*
Integrantes do Grupo:

Daniel Santana Corrêa Batista – 559622
Jonas de Jesus Campos de Oliveira – 561144
Wendell Nascimento Dourado - 559336
*/

-- Inserções para tabelas principais (DML)
INSERT INTO linha (nome, sigla, numero) VALUES ('Linha Diamante', 'LD', 101);
INSERT INTO linha (nome, sigla, numero) VALUES ('Linha Esmeralda', 'LE', 102);
INSERT INTO linha (nome, sigla, numero) VALUES ('Linha Rubi', 'LR', 103);
INSERT INTO linha (nome, sigla, numero) VALUES ('Linha Turquesa', 'LT', 104);
INSERT INTO linha (nome, sigla, numero) VALUES ('Linha Safira', 'LS', 105);

INSERT INTO estacao (nome, sigla, endereco) VALUES ('Osasco', 'OS', 'Rua A, 100');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Presidente Altino', 'PA', 'Rua B, 200');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Ceasa', 'CE', 'Rua C, 300');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Vila Lobos-Jaguaré', 'VLJ', 'Rua D, 400');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Cidade Universitária', 'CU', 'Rua E, 500');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Pinheiros', 'PI', 'Rua F, 600');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Hebraica-Rebouças', 'HR', 'Rua G, 700');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Cidade Jardim', 'CJ', 'Rua H, 800');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Vila Olímpia', 'VO', 'Rua I, 900');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Berrini', 'BE', 'Rua J, 1000');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Morumbi-Claro', 'MC', 'Rua K, 1100');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Granja Julieta', 'GJ', 'Rua L, 1200');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('João Dias', 'JD', 'Rua M, 1300');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Santo Amaro', 'SA', 'Rua N, 1400');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Socorro', 'SO', 'Rua O, 1500');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Jurubatuba-Senac', 'JS', 'Rua P, 1600');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Autódromo', 'AU', 'Rua Q, 1700');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Primavera-Interlagos', 'PII', 'Rua R, 1800');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Grajaú', 'GR', 'Rua S, 1900');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Bruno Covas-Mendes-Vila Natal', 'BCM', 'Rua T, 2000');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Júlio Prestes', 'JP', 'Rua U, 2100');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Palmeiras-Barra Funda', 'PBF', 'Rua V, 2200');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Lapa', 'LA', 'Rua W, 2300');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Domingos de Moraes', 'DM', 'Rua X, 2400');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Imperatriz Leopoldina', 'IL', 'Rua Y, 2500');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Comandante Sampaio', 'CS', 'Rua Z, 2600');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('Quitaúna', 'QU', 'Rua AA, 2700');
INSERT INTO estacao (nome, sigla, endereco) VALUES ('General Miguel Costa', 'GMC', 'Rua AB, 2800');

INSERT INTO funcionario (nome, cpf, cargo, email, senha, acesso, id_funcionario_admin) 
VALUES ('Carlos Silva', '12345678901', 'Maquinista', 'carlos@email.com', 'senha123', 1, NULL);
INSERT INTO funcionario (nome, cpf, cargo, email, senha, acesso, id_funcionario_admin) 
VALUES ('Ana Souza', '23456789012', 'Fiscal', 'ana@email.com', 'senha456', 2, 1);
INSERT INTO funcionario (nome, cpf, cargo, email, senha, acesso, id_funcionario_admin) 
VALUES ('Bruno Lima', '34567890123', 'Atendente', 'bruno@email.com', 'senha789', 2, 2);
INSERT INTO funcionario (nome, cpf, cargo, email, senha, acesso, id_funcionario_admin) 
VALUES ('Mariana Costa', '45678901234', 'Supervisor', 'mariana@email.com', 'senha321', 3, 3);
INSERT INTO funcionario (nome, cpf, cargo, email, senha, acesso, id_funcionario_admin) 
VALUES ('Fernando Alves', '56789012345', 'Gerente', 'fernando@email.com', 'senha654', 3, 4);

-- Inserções para viagens
INSERT INTO viagem (id_estacao_partida, id_estacao_destino, data_partida, data_chegada) 
VALUES (1, 20, TIMESTAMP '2025-05-01 08:00:00', TIMESTAMP '2025-05-01 10:30:00');
INSERT INTO viagem (id_estacao_partida, id_estacao_destino, data_partida, data_chegada) 
VALUES (21, 28, TIMESTAMP '2025-05-01 09:15:00', TIMESTAMP '2025-05-01 11:45:00');
INSERT INTO viagem (id_estacao_partida, id_estacao_destino, data_partida, data_chegada) 
VALUES (6, 14, TIMESTAMP '2025-05-01 10:30:00', TIMESTAMP '2025-05-01 12:00:00');
INSERT INTO viagem (id_estacao_partida, id_estacao_destino, data_partida, data_chegada) 
VALUES (2, 10, TIMESTAMP '2025-05-01 14:00:00', TIMESTAMP '2025-05-01 15:30:00');
INSERT INTO viagem (id_estacao_partida, id_estacao_destino, data_partida, data_chegada) 
VALUES (23, 1, TIMESTAMP '2025-05-01 16:45:00', TIMESTAMP '2025-05-01 18:15:00');

-- Inserções para trens
INSERT INTO trem (id_viagem, status, numeracao) VALUES (1, 'ativo', 'T10501');
INSERT INTO trem (id_viagem, status, numeracao) VALUES (2, 'ativo', 'T10502');
INSERT INTO trem (id_viagem, status, numeracao) VALUES (3, 'ativo', 'T10503');
INSERT INTO trem (id_viagem, status, numeracao) VALUES (4, 'inativo', 'T10504');
INSERT INTO trem (id_viagem, status, numeracao) VALUES (5, 'ativo', 'T10505');

-- Inserções para itens
INSERT INTO item (nome, abreviacao, url, favorito, id_funcionario) 
VALUES ('Teclado', 'TCL', 'https://equipamentos.ccr.com.br/teclado', 1, 1);
INSERT INTO item (nome, abreviacao, url, favorito, id_funcionario) 
VALUES ('Monitor', 'MON', 'https://equipamentos.ccr.com.br/monitor', 0, 2);
INSERT INTO item (nome, abreviacao, url, favorito, id_funcionario) 
VALUES ('Radio', 'RAD', 'https://equipamentos.ccr.com.br/radio', 0, 3);
INSERT INTO item (nome, abreviacao, url, favorito, id_funcionario) 
VALUES ('Tablet', 'TAB', 'https://equipamentos.ccr.com.br/tablet', 1, 4);
INSERT INTO item (nome, abreviacao, url, favorito, id_funcionario) 
VALUES ('Smartphone', 'SMP', 'https://equipamentos.ccr.com.br/smartphone', 0, 5);

-- Inserções para tabelas associativas (DML)
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 1);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 2);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 3);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 4);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 5);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 6);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 7);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 8);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 9);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 10);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 11);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 12);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 13);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 14);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 15);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 16);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 17);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 18);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 19);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (2, 20);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (1, 21);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (1, 22);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (1, 23);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (1, 24);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (1, 25);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (1, 2);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (1, 1);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (1, 26);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (1, 27);
INSERT INTO linha_estacao (id_linha, id_estacao) VALUES (1, 28);

-- Consultas DQL
-- Consulta simples em todas as tabelas
SELECT * FROM linha;
SELECT * FROM estacao;
SELECT * FROM funcionario;
SELECT * FROM linha_estacao;
SELECT * FROM viagem;
SELECT * FROM trem;
SELECT * FROM item;

-- Consulta com ORDER BY
SELECT * FROM funcionario ORDER BY nome ASC;

-- Consulta com função numérica de grupo
SELECT COUNT(*) AS total_funcionarios FROM funcionario;
SELECT MAX(data_chegada - data_partida) AS viagem_mais_longa FROM viagem;

-- Consulta com GROUP BY
SELECT cargo, COUNT(*) AS quantidade FROM funcionario GROUP BY cargo;

-- Consulta com subquery
SELECT nome, email FROM funcionario WHERE id_funcionario = (SELECT MIN(id_funcionario) FROM funcionario);

-- Consulta com JOIN
SELECT l.nome AS linha, e.nome AS estacao 
FROM linha l
JOIN linha_estacao le ON l.id_linha = le.id_linha
JOIN estacao e ON le.id_estacao = e.id_estacao;

-- Consulta com WHERE
SELECT * FROM funcionario WHERE cargo = 'Maquinista';
SELECT t.id_trem, t.numeracao, v.data_partida, v.data_chegada
FROM trem t
JOIN viagem v ON t.id_viagem = v.id_viagem
WHERE t.status = 'ativo';
