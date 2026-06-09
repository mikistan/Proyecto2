import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def cargar_archivo_drive(ruta_archivo,separador=","):
    """Cargar archivo csv
        Párametros:
        ruta_archivo: str con la ruta del archivo
        separador: str, la forma en que está separados los datos en el archivo
    """
    return pd.read_csv(ruta_archivo,sep=separador)

def contar_nulos(df):
    """Cuenta la cantidad de nulos y su porcentaje en un DataFrame
    Párametros:
    df: DataFrame con la información
    """
    # Se calcula el total de nulos y el porcentaje
    null_count = df.isnull().sum()
    null_percentage = (df.isnull().sum() / len(df)) * 100

    # Lo metemos en un DataFrame
    null_analysis = pd.DataFrame({'Total Nulos': null_count,'Porcentaje (%)': null_percentage})

    # Se ordena de mayor a menor
    print(null_analysis.sort_values(by='Total Nulos', ascending=False))

def analisis_inicial(df):
    """Analiza con varios métodos el dataframe ingresado
    Párametros:
    df: DataFrame con la información
    """
    print(f"Tamaño: {df.shape}")
    print("\nPrimeras 5 filas del DataFrame:")
    print(df.head())
    print("Información general del DataFrame:")
    print(df.info())
    print("Descripción estadística del DataFrame:")
    print(df.describe())
    # Comprobar datos nan por columna
    contar_nulos(df)
    # Comprobar duplicados
    print(f"Cantidad de duplicados: {df.duplicated().sum()}")

def matriz_corr(df, columnas_numericas):
    """Crea una matriz de correlación para las variables ingresadas
    Parámetros:
    df; DataFrame con la información
    columnas_numericas: lista con las columnas a analizar
    """
    # Calcular matriz de correlación
    correlation_matrix = df[columnas_numericas].corr()
    # Crear figura
    plt.figure(figsize=(15, 12))

    # Crear mapa de calor
    ax = sns.heatmap(correlation_matrix,annot=True,fmt='.2f',cmap='coolwarm',center=0,vmin=-1,vmax=1,linewidths=0.5,linecolor='white',
    annot_kws={'size': 10,'weight': 'bold'},cbar_kws={'label': 'Coeficiente de Correlación'})

    # Título
    plt.title('Matriz de correlación de variables numéricas',fontsize=20,fontweight='bold',pad=20)
    # Rotación de etiquetas
    plt.xticks(rotation=45,ha='right',fontsize=10)
    plt.yticks(rotation=0,fontsize=10)

    # Explicación inferior
    plt.figtext(0.5,0.01,'La matriz de correlación permite identificar la intensidad y dirección de la relación lineal entre variables numéricas. Valores cercanos a 1\n'
    'indican correlación positiva fuerte, valores cercanos a -1 indican correlación negativa fuerte y valores cercanos a 0 sugieren poca relación.',
    ha='center',fontsize=11,bbox=dict(facecolor='lightgray',alpha=0.4,edgecolor='gray',boxstyle='round'))

    # Ajustar diseño
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.show()

def detecta_atipicos_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lim_inf = Q1 - 1.5 * IQR # Cálculo de límite inferior
    lim_sup = Q3 + 1.5 * IQR # Cálculo de límite superior
    atipicos = df[(df[column] < lim_inf) | (df[column] > lim_sup)]
    return atipicos

def boxplots(df, num_columnas):
    if len(num_columnas) % 3 == 0:  num_filas = len(num_columnas) // 3
    else:                           num_filas = len(num_columnas) // 3 + 1

    fig, axes = plt.subplots(num_filas, 3, figsize=(16, 10))
    colors = sns.color_palette("husl", n_colors=len(num_columnas))

    # Se utiliza flatten() para recorrer fácilmente todos los subplots.
    for ax, col, color in zip(axes.flatten(), num_columnas, colors):
        # Boxplot
        sns.boxplot(y=df[col],ax=ax,color=color,width=0.4,linewidth=1.5,flierprops=dict(marker='o',markerfacecolor='red',markersize=6,alpha=0.6))

        ax.set_title(f'Box Plot de {col}',fontsize=13,fontweight='bold')
        ax.set_ylabel('')
        ax.grid(axis='y',alpha=0.3,linestyle='--')

        # Detectar outliers usando IQR
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lim_inf = Q1 - 1.5 * IQR
        lim_sup = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lim_inf) | (df[col] > lim_sup)][col]

        # Marcar el outlier mínimo y máximo
        if len(outliers) > 0:
            outlier_min = outliers.min()
            outlier_max = outliers.max()

            # Outlier mínimo
            ax.annotate(f'Min: {outlier_min:.2f}',xy=(0, outlier_min),xytext=(0.15, outlier_min),textcoords='data',fontsize=8,color='darkred',
            bbox=dict(facecolor='white',alpha=0.8,edgecolor='gray',boxstyle='round'),
            arrowprops=dict(arrowstyle='->',color='red',lw=1))

            # Evitar duplicar si sólo existe un outlier
            if outlier_min != outlier_max:
                ax.annotate(f'Max: {outlier_max:.2f}',xy=(0, outlier_max),xytext=(0.15, outlier_max),textcoords='data',fontsize=8,color='darkred',
                bbox=dict(facecolor='white',alpha=0.8,edgecolor='gray',boxstyle='round'),
                arrowprops=dict(arrowstyle='->',color='red',lw=1))

        # Texto dentro del gráfico
        ax.text(0.03,0.95,'Visualiza mediana,\n''dispersión y posibles\n''valores atípicos.',transform=ax.transAxes,fontsize=9,va='top',
        bbox=dict(facecolor='white',alpha=0.8,edgecolor='gray',boxstyle='round'))

    # Eliminar los subplot vacíos (aplanando)
    axes_flat = axes.flatten()
    for i in range(len(num_columnas), len(axes_flat)):  fig.delaxes(axes_flat[i])

    fig.suptitle('Análisis de Outliers en Variables Numéricas',fontsize=18,fontweight='bold')
    fig.text(0.5,0.02,'Los boxplots permiten identificar la mediana, la dispersión '
    'de los datos y posibles valores atípicos en cada variable numérica.', ha='center',fontsize=11,
    bbox=dict(facecolor='lightgray',alpha=0.4,edgecolor='gray',boxstyle='round'))

    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.show()

def graficar_histogramas(df,titulo='Distribución de Variables Numéricas',bins='auto',kde=True):
    """
    Genera histogramas para cualquier DataFrame.
    Parámetros:
    df : DataFrame, DataFrame a analizar.
    titulo : str, Título general del gráfico.
    bins : int, str Número de bins o método automático.
    kde : bool, Mostrar curva KDE.
    """
    # columnas numéricas
    columnas = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if len(columnas) == 0:
        print("No se encontraron columnas numéricas.")
        return

    sns.set_style("whitegrid")
    n = len(columnas)
    ncols = 2
    nrows = math.ceil(n / ncols)
    fig, axes = plt.subplots(nrows,ncols,figsize=(8 * ncols, 5 * nrows))
    axes = axes.flatten()

    palette = sns.color_palette("Set2",n_colors=n)
    # Histogramas
    for i, col in enumerate(columnas):
        sns.histplot(df[col].dropna(),bins=bins,color=palette[i],edgecolor='black',linewidth=1,
        alpha=0.8,kde=kde,kde_kws={'bw_adjust': 1},line_kws={'linewidth': 3},ax=axes[i])

        axes[i].set_title(f'Distribución de {col}',fontsize=14,fontweight='bold')
        axes[i].set_xlabel(col,fontsize=11)
        axes[i].set_ylabel('Frecuencia',fontsize=11)
        axes[i].grid(alpha=0.3,linestyle='--')

        media = df[col].mean()
        mediana = df[col].median()

        axes[i].text(0.02,0.95,f'Media: {media:.2f}\nMediana: {mediana:.2f}',transform=axes[i].transAxes,
        fontsize=9,va='top',bbox=dict(facecolor='white',alpha=0.8,edgecolor='gray',boxstyle='round'))

    # Eliminar subplots vacíos
    for j in range(n, len(axes)):   fig.delaxes(axes[j])

    fig.suptitle(titulo,fontsize=20,fontweight='bold')
    fig.text(0.5,0.01,'Los histogramas permiten observar la distribución de los datos, '
    'su dispersión \ny posibles concentraciones de frecuencia para cada variable numérica.',
    ha='center',fontsize=11,bbox=dict(facecolor='lightgray',alpha=0.4,edgecolor='gray',boxstyle='round'))

    plt.tight_layout(rect=[0, 0.05, 1, 0.96])
    plt.show()

def grafico_conteo(df,columna,titulo=None,ordenar=True,figsize=(12, 7),y_label='Frecuencia', x_label="None"):
    """
    Genera un gráfico de conteo para cualquier
    variable categórica de un DataFrame.
    Parámetros
    df : DataFrame, DataFrame a analizar.
    columna : str, Nombre de la columna categórica.
    titulo : str, Título personalizado (opcional).
    ordenar : bool, Ordenar categorías por frecuencia.
    figsize : tuple, Tamaño de la figura.
    y_label y x_label: str, Etiquetas de los ejes.
    """
    if x_label is None: x_label = columna
    if columna not in df.columns:
        print(f"La columna '{columna}' no existe.")
        return

    # Calcular frecuencias
    conteo = df[columna].value_counts()

    if ordenar: orden = conteo.index
    else:   orden = None

    # Crear figura
    plt.figure(figsize=figsize)
    colores = sns.color_palette("viridis",n_colors=len(conteo))

    # Crear gráfico
    ax = sns.countplot(data=df,x=columna,order=orden,hue=columna,palette=colores,legend=False,edgecolor='black',linewidth=1.2)

    if titulo is None:  titulo = f'Distribución de {columna}'

    plt.title(titulo,fontsize=18,fontweight='bold')
    plt.xlabel(columna,fontsize=12,fontweight='bold')
    plt.ylabel(y_label,fontsize=12,fontweight='bold')

    plt.grid(axis='y',linestyle='--',alpha=0.3)

    # Etiquetas de frecuencia y porcentaje
    total = len(df)
    for barra in ax.patches:
        altura = barra.get_height()
        porcentaje = (altura / total) * 100
        ax.annotate(f'{int(altura)}\n({porcentaje:.1f}%)',(barra.get_x() + barra.get_width()/2,altura),
        ha='center',va='bottom',fontsize=10,fontweight='bold',xytext=(0, 5),textcoords='offset points',
        bbox=dict(facecolor='white',alpha=0.8,edgecolor='gray',boxstyle='round'))

    # Rotación automática si hay muchas categorías
    if len(conteo) > 5: plt.xticks(rotation=30,ha='right')

    # Texto inferior
    plt.figtext(0.5,0.01,f'El gráfico muestra la distribución de frecuencias de la variable "{columna}".\n'
    'Las etiquetas indican la cantidad de registros y su porcentaje respecto del total.',
    ha='center',fontsize=11,bbox=dict(facecolor='lightgray',alpha=0.4,edgecolor='gray',boxstyle='round'))

    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.show()