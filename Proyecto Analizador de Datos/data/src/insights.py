from datetime import datetime


def _fmt_money(x: float) -> str:
    return f"${x:,.0f}"


def build_report(total, por_categoria, por_mes, top1, dia_caro, top10_df):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # categoría dominante
    cat_dom = por_categoria.idxmax()
    monto_dom = float(por_categoria.max())
    pct_dom = (monto_dom / total) * 100 if total else 0

    # meses (si hay)
    multi_mes = len(por_mes) > 1
    if multi_mes:
        mes_caro, monto_caro = por_mes.idxmax(), float(por_mes.max())
        mes_barato, monto_barato = por_mes.idxmin(), float(por_mes.min())

    # top gasto individual
    fecha_top, categoria_top, desc_top, monto_top = top1

    # día más caro
    dia, monto_dia = dia_caro

    lines = []
    lines.append("REPORTE DE GASTOS")
    lines.append(f"Generado: {now}")
    lines.append("-" * 50)
    lines.append("Resumen ejecutivo")
    lines.append(f"• Gasto total del período: {_fmt_money(total)}")
    lines.append(f"• Categoría dominante: {cat_dom} ({_fmt_money(monto_dom)} | {pct_dom:.1f}% del total)")
    lines.append(f"• Gasto individual más alto: {desc_top} ({categoria_top}) el {fecha_top} por {_fmt_money(monto_top)}")
    lines.append(f"• Día más caro: {dia} ({_fmt_money(monto_dia)})")

    if multi_mes:
        lines.append(f"• Mes más caro: {mes_caro} ({_fmt_money(monto_caro)})")
        lines.append(f"• Mes más barato: {mes_barato} ({_fmt_money(monto_barato)})")
    else:
        lines.append(f"• Evolución mensual: solo hay un mes en los datos ({por_mes.index[0]})")

    lines.append("")
    lines.append("Ranking por categoría")
    for categoria, monto in por_categoria.items():
        monto = float(monto)
        pct = (monto / total) * 100 if total else 0
        lines.append(f"- {categoria}: {_fmt_money(monto)} ({pct:.1f}%)")

    lines.append("")
    lines.append("Gasto por mes")
    for mes, monto in por_mes.items():
        lines.append(f"- {mes}: {_fmt_money(float(monto))}")

    lines.append("")
    lines.append("Top 5 gastos individuales")
    top5 = top10_df.head(5)[["fecha", "categoria", "descripcion", "monto"]]
    for _, r in top5.iterrows():
        fecha = r["fecha"].date()
        lines.append(f"- {fecha} | {r['categoria']} | {r['descripcion']} | {_fmt_money(float(r['monto']))}")

    lines.append("-" * 50)
    return "\n".join(lines)

def build_report_md(total, por_categoria, por_mes, top1, dia_caro, top10_df):
    def fmt_money(x):
        return f"${x:,.0f}"

    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    cat_dom = por_categoria.idxmax()
    monto_dom = float(por_categoria.max())
    pct_dom = (monto_dom / total) * 100 if total else 0

    fecha_top, categoria_top, desc_top, monto_top = top1
    dia, monto_dia = dia_caro

    md = []
    md.append("# 📊 Reporte de gastos\n")
    md.append(f"**Generado:** {now}\n")
    md.append("---\n")

    md.append("## Resumen ejecutivo\n")
    md.append(f"- **Gasto total:** {fmt_money(total)}")
    md.append(f"- **Categoría dominante:** {cat_dom} ({fmt_money(monto_dom)} · {pct_dom:.1f}%)")
    md.append(f"- **Gasto individual más alto:** {desc_top} ({categoria_top}) el {fecha_top} por {fmt_money(monto_top)}")
    md.append(f"- **Día más caro:** {dia} ({fmt_money(monto_dia)})\n")

    if len(por_mes) > 1:
        mes_caro, monto_caro = por_mes.idxmax(), float(por_mes.max())
        mes_barato, monto_barato = por_mes.idxmin(), float(por_mes.min())
        md.append(f"- **Mes más caro:** {mes_caro} ({fmt_money(monto_caro)})")
        md.append(f"- **Mes más barato:** {mes_barato} ({fmt_money(monto_barato)})\n")
    else:
        md.append(f"- Evolución mensual: solo hay un mes ({por_mes.index[0]})\n")

    md.append("## Ranking por categoría\n")
    for categoria, monto in por_categoria.items():
        monto = float(monto)
        pct = (monto / total) * 100 if total else 0
        md.append(f"- **{categoria}**: {fmt_money(monto)} ({pct:.1f}%)")

    md.append("\n## Gasto por mes\n")
    for mes, monto in por_mes.items():
        md.append(f"- **{mes}**: {fmt_money(float(monto))}")

    md.append("\n## Top 5 gastos individuales\n")
    top5 = top10_df.head(5)[["fecha", "categoria", "descripcion", "monto"]]
    for _, r in top5.iterrows():
        md.append(
            f"- {r['fecha'].date()} · **{r['categoria']}** · {r['descripcion']} · {fmt_money(float(r['monto']))}"
        )

    return "\n".join(md)
