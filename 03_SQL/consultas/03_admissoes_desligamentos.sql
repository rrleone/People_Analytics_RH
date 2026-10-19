-- Movimentação mensal e saldo
SELECT DATE_TRUNC('month', data_evento)::date AS mes,
 COUNT(*) FILTER (WHERE BTRIM(tipo_evento)='Admissão') AS admissoes,
 COUNT(*) FILTER (WHERE BTRIM(tipo_evento)='Desligamento') AS desligamentos,
 COUNT(*) FILTER (WHERE BTRIM(tipo_evento)='Admissão')
 - COUNT(*) FILTER (WHERE BTRIM(tipo_evento)='Desligamento') AS saldo
FROM public.eventos_rh
GROUP BY DATE_TRUNC('month', data_evento)
ORDER BY mes;
