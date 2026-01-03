# 📊 Análisis de gastos personales en Python

Proyecto de análisis de datos desarrollado en Python que permite analizar gastos personales a partir de un archivo CSV, generar métricas clave, gráficos y reportes automáticos listos para presentación.

El objetivo del proyecto es demostrar habilidades en:
- Manipulación y análisis de datos
- Organización de código en módulos
- Generación de reportes automáticos
- Buenas prácticas para proyectos de portfolio

---

## 🚀 Funcionalidades

- Cálculo de gasto total del período
- Análisis de gasto por categoría
- Evolución mensual del gasto
- Identificación de:
  - Mes más caro y más barato
  - Categoría dominante
  - Gasto individual más alto
  - Día con mayor gasto
- Generación automática de:
  - Gráficos (.png)
  - Resumen numérico (.csv)
  - Reporte en texto (.txt)
  - Reporte en Markdown (.md)

---

## 🗂️ Estructura del proyecto

```
portfolio-gastos/
├── data/
│   └── gastos.csv
├── src/
│   ├── load_clean.py
│   ├── analysis.py
│   ├── plots.py
│   └── insights.py
├── outputs/
│   ├── figures/
│   ├── conclusiones.txt
│   ├── reporte.md
│   └── resumen_gastos.csv
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Tecnologías utilizadas

- Python 3
- Pandas
- Matplotlib
- Virtual environments (`venv`)

---

## ▶️ Cómo ejecutar el proyecto

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/valennbusta9/Proyecto-Analizador-de-Datos.git
cd portfolio-gastos
```

### 2️⃣ Crear y activar entorno virtual (macOS)
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar el análisis
```bash
python3 main.py
```

---

## 📁 Outputs generados

Al ejecutar el proyecto se generan automáticamente:

- `outputs/figures/`
  - Gráfico de gasto por categoría
  - Gráfico de evolución mensual
  - Top gastos
- `outputs/resumen_gastos.csv`
- `outputs/conclusiones.txt`
- `outputs/reporte.md`

---

## 📌 Notas

- El archivo `gastos.csv` puede ser reemplazado por otro CSV con la misma estructura.
- El proyecto está pensado para ser simple, claro y extensible.

---

## 👤 Autor

Proyecto desarrollado por **Valen**  
Estudiante de Licenciatura en Sistemas
