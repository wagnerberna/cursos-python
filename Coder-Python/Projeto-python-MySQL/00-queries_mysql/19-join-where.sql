-- All
-- SELECT * FROM estados e, cidades c 
-- WHERE e.id = c.estado_id;

-- região não precisa identificar tabela origem pois é única
SELECT 
  c.nome AS Cidade, 
  e.nome AS Estado, 
  regiao 
FROM estados e, cidades c 
WHERE e.id = c.estado_id;
