import os
import pandas as pd
import openai

# Configura tu API Key desde una variable de entorno llamada OPENAI_API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")


def cargar_archivo_excel(ruta_archivo):
    """Carga un archivo Excel y devuelve un DataFrame."""
    try:
        df = pd.read_excel(ruta_archivo)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        return df
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
    return None


def mostrar_resumen_datos(df):
    """Muestra un resumen claro de los datos."""
    print("\n📊 RESUMEN DE LOS DATOS 📊")
    print("\n🔹 Columnas:", df.columns.tolist())
    print("\n🔹 Tipos de datos:\n", df.dtypes)
    print("\n🔹 Valores nulos por columna:\n", df.isnull().sum())

    print("\n📈 ESTADÍSTICAS CLAVE 📈")
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            print(f"\n🔢 Columna numérica: {col}")
            print(f"   • Media: {df[col].mean():.2f}")
            print(f"   • Mediana: {df[col].median():.2f}")
            moda = df[col].mode()
            if not moda.empty:
                print(f"   • Moda: {moda[0]:.2f}")
            else:
                print("   • Moda: No disponible")
            print(f"   • Desviación estándar: {df[col].std():.2f}")
        else:
            print(f"\n🔤 Columna categórica: {col}")
            print(df[col].value_counts().head(10))


def construir_prompt(df):
    """Construye un prompt para OpenAI con contexto amplio."""
    prompt = (
        "Eres un analista experto en datos comerciales. "
        "A continuación tienes un resumen estadístico de un conjunto "
        "de datos de ventas:\n\n"
    )
    fecha_min = df["Fecha"].min().strftime("%d-%m-%Y")
    fecha_max = df["Fecha"].max().strftime("%d-%m-%Y")
    prompt += (
        "📅 Rango de fechas: desde " + fecha_min +
        " hasta " + fecha_max + "\n"
    )
    productos_top = df["Especie"].value_counts().head(5).to_dict()
    prompt += "🐟 Productos más vendidos: " + str(productos_top) + "\n"
    destinos_top = df["Destino"].value_counts().head(5).to_dict()
    prompt += "🌎 Destinos principales: " + str(destinos_top) + "\n"
    clientes_top = df["CLIENTE"].value_counts().head(5).to_dict()
    prompt += "👥 Clientes principales: " + str(clientes_top) + "\n"
    monedas = df["Moneda"].value_counts().to_dict()
    prompt += "💱 Monedas utilizadas: " + str(monedas) + "\n"
    total_ventas_usd = df["Tot. Fact. U$$"].sum()
    promedio_ventas_usd = df["Tot. Fact. U$$"].mean()
    prompt += (
        "💰 Ventas totales en USD: " +
        f"{total_ventas_usd:,.2f}\n"
        "📊 Promedio por factura en USD: " +
        f"{promedio_ventas_usd:,.2f}\n"
    )
    prompt += (
        "\nProporciona un análisis breve y claro sobre estos datos, "
        "destacando patrones, tendencias o insights relevantes desde 2010 "
        "hasta la actualidad."
    )
    return prompt


def obtener_analisis_openai(prompt):
    """Envía el prompt a la API de OpenAI y devuelve el análisis."""
    if not openai.api_key:
        print("Error: La API Key de OpenAI no está configurada correctamente.")
        return None
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": ("Eres un asistente experto en análisis "
                             "de datos comerciales.")},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error al obtener análisis de OpenAI: {e}")
    return None


def main():
    ruta_archivo = input("📂 Introduce la ruta del archivo Excel: ")
    df = cargar_archivo_excel(ruta_archivo)
    if df is not None:
        mostrar_resumen_datos(df)
        prompt = construir_prompt(df)
        analisis = obtener_analisis_openai(prompt)
        if analisis:
            print("\n🤖 ANÁLISIS DE OPENAI 🤖")
            print(analisis)
        else:
            print("⚠️ No se pudo obtener el análisis de OpenAI.")
    else:
        print("⚠️ No se pudo cargar el archivo Excel correctamente.")


if __name__ == "__main__":
    main()
