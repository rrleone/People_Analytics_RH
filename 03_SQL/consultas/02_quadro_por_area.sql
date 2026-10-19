-- Distribuição de funcionários por área, cargo e nível
SELECT area, cargo, nivel,
 COUNT(*) FILTER (WHERE data_demissao IS NULL) AS sem_data_demissao,
 COUNT(*) AS total_registros
FROM public.funcionarios
GROUP BY area, cargo, nivel
ORDER BY area, sem_data_demissao DESC, cargo, nivel;
