
-- Perfil de funcionários em 30/09/2026
-- As datas da tabela funcionarios estão armazenadas como texto.

WITH p AS (
    SELECT DATE '2026-09-30' AS data_referencia
)
SELECT
    COUNT(*) AS total_cadastrado,

    COUNT(*) FILTER (
        WHERE NULLIF(TRIM(f.data_admissao), '')::date
              <= p.data_referencia
    ) AS admitidos_ate_referencia,

    COUNT(*) FILTER (
        WHERE NULLIF(TRIM(f.data_admissao), '')::date
                  <= p.data_referencia
          AND (
              NULLIF(TRIM(f.data_demissao), '') IS NULL
              OR NULLIF(TRIM(f.data_demissao), '')::date
                     > p.data_referencia
          )
    ) AS ativos_na_referencia,

    COUNT(*) FILTER (
        WHERE NULLIF(TRIM(f.data_demissao), '') IS NOT NULL
          AND NULLIF(TRIM(f.data_demissao), '')::date
                  <= p.data_referencia
    ) AS desligados_ate_referencia

FROM public.funcionarios f
CROSS JOIN p;
