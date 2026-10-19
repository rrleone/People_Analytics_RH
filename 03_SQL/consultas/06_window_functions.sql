-- Ranking de áreas pelo quadro sem data de desligamento
WITH quadro AS (
 SELECT area, COUNT(*) AS quantidade
 FROM public.funcionarios
 WHERE data_demissao IS NULL
 GROUP BY area
)
SELECT area, quantidade,
 DENSE_RANK() OVER (ORDER BY quantidade DESC) AS ranking_area,
 ROUND(100.0*quantidade/NULLIF(SUM(quantidade) OVER (),0),2) AS percentual_quadro
FROM quadro ORDER BY ranking_area, area;
