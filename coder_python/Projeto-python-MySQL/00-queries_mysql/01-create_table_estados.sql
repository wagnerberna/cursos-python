USE coder;
CREATE TABLE IF NOT EXISTS estados (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nome VARCHAR(45) NOT NULL,
  sigla VARCHAR(2) NOT NULL,
  regiao ENUM(
    'Norte',
    'Nordeste',
    'Centro-Oeste',
    'Sudeste',
    'Sul'
  ) NOT NULL,
  -- ENUM torna obrigatório uso de um desses valores
  populacao DECIMAL (5, 2) NOT NULL,
  -- 5 Digitos 2 flutuantes
  PRIMARY KEY (id),
  UNIQUE KEY (nome),
  UNIQUE KEY (sigla)
  -- Não aceitar duplicidade
);