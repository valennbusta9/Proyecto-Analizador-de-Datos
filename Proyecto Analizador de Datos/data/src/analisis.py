def gasto_total(df):
    return df["monto"].sum()


def gasto_por_categoria(df):
    return (
        df.groupby("categoria")["monto"]
        .sum()
        .sort_values(ascending=False)
    )


def top_gastos(df, n=10):
    return df.sort_values("monto", ascending=False).head(n)


def gasto_por_mes(df):
    df["mes"] = df["fecha"].dt.to_period("M").astype(str)
    return df.groupby("mes")["monto"].sum()

def mes_mas_caro(por_mes):
    # por_mes: Series index=mes, values=monto
    mes = por_mes.idxmax()
    monto = por_mes.max()
    return mes, float(monto)


def mes_mas_barato(por_mes):
    mes = por_mes.idxmin()
    monto = por_mes.min()
    return mes, float(monto)


def categoria_dominante(por_categoria, total):
    cat = por_categoria.idxmax()
    monto = por_categoria.max()
    pct = (monto / total) * 100 if total else 0
    return cat, float(monto), float(pct)


def gasto_mas_alto(df):
    fila = df.loc[df["monto"].idxmax()]
    return fila["fecha"].date(), fila["categoria"], fila["descripcion"], float(fila["monto"])


def dia_mas_caro(df):
    por_dia = df.groupby(df["fecha"].dt.date)["monto"].sum()
    dia = por_dia.idxmax()
    monto = por_dia.max()
    return dia, float(monto)

