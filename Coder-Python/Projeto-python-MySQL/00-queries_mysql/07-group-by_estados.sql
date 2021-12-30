-- Agrupa por região com a soma da população ou média ordena total decrescente
SELECT regiao AS 'Região',
sum(populacao) AS 'Total'
-- avg(populacao) AS 'Media'
FROM estados
GROUP BY regiao
ORDER BY Total DESC
-- ORDER BY Media DESC

-- Média do total da população
-- SELECT avg(populacao) AS Total
-- FROM estados