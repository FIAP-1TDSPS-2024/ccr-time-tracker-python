DROP TABLE item CASCADE CONSTRAINTS;
DROP TABLE funcionario CASCADE CONSTRAINTS;
DROP TABLE trem CASCADE CONSTRAINTS;
DROP TABLE viagem CASCADE CONSTRAINTS;
DROP TABLE linha_estacao CASCADE CONSTRAINTS;
DROP TABLE estacao CASCADE CONSTRAINTS;
DROP TABLE linha CASCADE CONSTRAINTS;

CREATE TABLE linha(
    id_linha number(10) GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_id_linha PRIMARY KEY,
    nome varchar(50) CONSTRAINT linha_nome_nn NOT NULL,
    sigla varchar(10) CONSTRAINT linha_sigla_nn NOT NULL CONSTRAINT linha_sigla_check_lgn CHECK (length(sigla) = 2),
    numero number(10) CONSTRAINT linha_numero_nn NOT NULL,
    UNIQUE(sigla)
);

CREATE TABLE estacao (
    id_estacao number(10) GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_id_estacao PRIMARY KEY,
    nome varchar(50) CONSTRAINT estacao_nome_nn NOT NULL,
    sigla varchar(10) CONSTRAINT estacao_sigla_nn NOT NULL,
    endereco varchar(100) CONSTRAINT estacao_endereco_nn NOT NULL
);


CREATE TABLE linha_estacao(
    id_linha number(10) CONSTRAINT fk_id_linha REFERENCES linha(id_linha),
    id_estacao number(10) CONSTRAINT fk_id_estacao REFERENCES estacao(id_estacao),
    CONSTRAINT pk_linha_estacao PRIMARY KEY (id_linha, id_estacao)
);

CREATE TABLE viagem(
    id_viagem number(10) GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_id_viagem PRIMARY KEY,
    id_estacao_partida number(10) CONSTRAINT fk_id_estacao_partida REFERENCES estacao(id_estacao),
    id_estacao_destino number(10) CONSTRAINT fk_id_estacao_destino REFERENCES estacao(id_estacao),
    data_partida timestamp CONSTRAINT viagem_data_partida_nn NOT NULL,
    data_chegada timestamp CONSTRAINT viagem_data_chegada_nn NOT NULL
);

CREATE TABLE trem(
    id_trem number(10) GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_id_trem PRIMARY KEY,
    id_viagem number(10) CONSTRAINT fk_id_viagem REFERENCES viagem(id_viagem),
    status varchar(10) CONSTRAINT trem_status_nn NOT NULL,
    CONSTRAINT trem_status_ck CHECK (status IN ('ativo', 'inativo')),
    numeracao varchar(10) CONSTRAINT trem_numeracao_nn NOT NULL
);
CREATE TABLE funcionario(
    id_funcionario number(10) GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_id_funcionario PRIMARY KEY,
    nome varchar(50) CONSTRAINT funcionario_nome_nn NOT NULL,
    cpf varchar(11) CONSTRAINT funcionario_cpf_nn NOT NULL,
    cargo varchar(50) CONSTRAINT funcionario_cargo_nn NOT NULL,
    email varchar(50) CONSTRAINT funcionario_email_nn NOT NULL,
    senha varchar(50) CONSTRAINT funcionario_senha_nn NOT NULL,
    acesso number(1) CONSTRAINT funcionario_acesso_nn NOT NULL,
    id_funcionario_admin number(10) CONSTRAINT fk_id_funcionario_admin REFERENCES funcionario(id_funcionario)
);

CREATE TABLE item(
    id_item number(10) GENERATED ALWAYS AS IDENTITY CONSTRAINT pk_id_item PRIMARY KEY,
    nome varchar(50) CONSTRAINT item_nome_nn NOT NULL,
    abreviacao varchar(10) CONSTRAINT item_abreviacao_nn NOT NULL,
    url varchar(100) CONSTRAINT item_url_nn NOT NULL,
    favorito number(1) CONSTRAINT item_favorito_nn NOT NULL,
    id_funcionario number(10) CONSTRAINT fk_id_funcionario REFERENCES funcionario(id_funcionario)
);