-- alteração de int para varchar com número max. de cacacteres
ALTER TABLE empresas MODIFY cnpj VARCHAR(14);

-- inserir empresas
INSERT INTO empresas
    (nome, cnpj)
VALUES
    ('Bradesco', 95694186000132),
    ('Vale', 27887148000146),
    ('Cielo', 01598317000134);


-- desc empresas;
-- desc prefeitos;
-- select * from empresas;
-- select * from cidades;

-- inserir tab cidades_empresas relacionamentos
INSERT INTO empresa_cidade
    (empresa_id, cidade_id, sede)
VALUES
    (1, 1, 1),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1);