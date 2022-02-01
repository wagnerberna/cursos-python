-- inserir usando o ID do estado:
INSERT INTO cidades (nome, area, estado_id)
VALUES ('Porto Alegre', 795, 21);

INSERT INTO cidades (nome, area, estado_id)
VALUES ('Caxias do Sul', 133.9, 21);

-- inserir usando um select ao invés do ID para localizar a siga
INSERT INTO cidades 
    (nome, area, estado_id)
VALUES (
    'Farroupilha',
    96.6,
    (select id from estados where sigla = 'RS')
);

INSERT INTO cidades
    (nome, area, estado_id)
VALUES (
    'Bento Gonçalves',
    100.2,
    (select id from estados where sigla = 'RS')
);
