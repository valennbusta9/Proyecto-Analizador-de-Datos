from src.cargaLimpia import cargaData
from src.analisis import (
    gasto_total,
    gasto_por_categoria,
    top_gastos,
    gasto_por_mes,
    gasto_mas_alto,
    dia_mas_caro
)
from src.plots import (
    plot_gasto_por_categoria,
    plot_evolucion_mensual,
    plot_top_gastos
)
from src.insights import build_report, build_report_md

# cargar datos
df = cargaData("Proyecto Analizador de Datos/data/gastos.csv")

# análisis
total = float(gasto_total(df))
por_categoria = gasto_por_categoria(df)
top10 = top_gastos(df, n=10)
por_mes = gasto_por_mes(df)

# outputs numéricos
por_categoria.to_csv("outputs/resumen_gastos.csv")

# gráficos
plot_gasto_por_categoria(por_categoria, "outputs/figures/gasto_por_categoria.png")

if len(por_mes) > 1:
    plot_evolucion_mensual(por_mes, "outputs/figures/evolucion_mensual.png")

plot_top_gastos(top10, "outputs/figures/top_10_gastos.png")

# insights
top1 = gasto_mas_alto(df)
dia_caro = dia_mas_caro(df)

texto = build_report(total, por_categoria, por_mes, top1, dia_caro, top10)

print("\n=== Conclusiones automáticas ===")
print(texto)

# guardar conclusiones en un txt (portfolio pro)
with open("outputs/conclusiones.txt", "w", encoding="utf-8") as f:
    f.write("Conclusiones automáticas\n")
    f.write(texto + "\n")

top1 = gasto_mas_alto(df)
dia_caro = dia_mas_caro(df)

from src.insights import build_report, build_report_md

# ...

reporte_txt = build_report(total, por_categoria, por_mes, top1, dia_caro, top10)
reporte_md = build_report_md(total, por_categoria, por_mes, top1, dia_caro, top10)

print("\n" + reporte_txt)

with open("outputs/conclusiones.txt", "w", encoding="utf-8") as f:
    f.write(reporte_txt + "\n")

with open("outputs/reporte.md", "w", encoding="utf-8") as f:
    f.write(reporte_md + "\n")

