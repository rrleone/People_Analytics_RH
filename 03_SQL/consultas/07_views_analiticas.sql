-- Views reutilizáveis. Executar após validar os tipos e os resultados.
CREATE OR REPLACE VIEW public.vw_funcionarios_por_area AS
SELECT area, COUNT(*) AS total_funcionarios,
 COUNT(*) FILTER (WHERE data_demissao IS NULL) AS sem_data_demissao,
 COUNT(*) FILTER (WHERE data_demissao IS NOT NULL) AS com_data_demissao
FROM public.funcionarios GROUP BY area;

CREATE OR REPLACE VIEW public.vw_custo_mensal_rh AS
SELECT data_referencia,
 SUM(salario_base_mensal + encargos_mensais + beneficios_mensais
   + vale_transporte_mensal + vale_refeicao_mensal + provisao_ferias_mensal
   + horas_extras_mensais + adicionais_mensais) AS custo_total_pessoal
FROM public.historico_remuneracao GROUP BY data_referencia;
