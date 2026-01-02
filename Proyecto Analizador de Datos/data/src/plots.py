import matplotlib.pyplot as plt


def plot_gasto_por_categoria(series, output_path):
    plt.figure(figsize=(8, 5))
    series.plot(kind="bar")
    plt.title("Gasto total por categoría")
    plt.ylabel("Monto")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_evolucion_mensual(series, output_path):
    plt.figure(figsize=(8, 5))
    series.plot(marker="o")
    plt.title("Evolución mensual del gasto")
    plt.ylabel("Monto")
    plt.xlabel("Mes")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_top_gastos(df, output_path):
    plt.figure(figsize=(8, 5))
    df.plot(kind="barh", x="descripcion", y="monto", legend=False)
    plt.title("Top 10 gastos más altos")
    plt.xlabel("Monto")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
