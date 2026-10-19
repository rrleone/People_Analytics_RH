-- IDs duplicados
SELECT id_funcionario, COUNT(*) AS ocorrencias
FROM public.funcionarios GROUP BY id_funcionario HAVING COUNT(*)>1;

-- Datas de admissão ausentes
SELECT COUNT(*) AS admissoes_ausentes
FROM public.funcionarios WHERE data_admissao IS NULL;

-- Valores negativos em componentes de remuneração
SELECT * FROM public.historico_remuneracao
WHERE salario_base_mensal < 0 OR encargos_mensais < 0
 OR beneficios_mensais < 0 OR vale_transporte_mensal < 0
 OR vale_refeicao_mensal < 0 OR provisao_ferias_mensais < 0
 OR horas_extras_mensais < 0 OR adicionais_mensais < 0;

-- Eventos sem funcionário correspondente
SELECT e.* FROM public.eventos_rh e
LEFT JOIN public.funcionarios f ON f.id_funcionario=e.id_funcionario
WHERE f.id_funcionario IS NULL;
