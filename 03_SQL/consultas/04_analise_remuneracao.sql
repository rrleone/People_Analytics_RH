-- Composição do custo por mês de referência
SELECT data_referencia,
 SUM(salario_base_mensal) AS salario_base,
 SUM(encargos_mensais) AS encargos,
 SUM(beneficios_mensais) AS beneficios,
 SUM(vale_transporte_mensal) AS vale_transporte,
 SUM(vale_refeicao_mensal) AS vale_refeicao,
 SUM(provisao_ferias_mensal) AS provisao_ferias,
 SUM(horas_extras_mensais) AS horas_extras,
 SUM(adicionais_mensais) AS adicionais,
 SUM(salario_base_mensal + encargos_mensais + beneficios_mensais
   + vale_transporte_mensal + vale_refeicao_mensal + provisao_ferias_mensal
   + horas_extras_mensais + adicionais_mensais) AS custo_total
FROM public.historico_remuneracao
GROUP BY data_referencia
ORDER BY data_referencia;
