# Ejemplos de Markdown Avanzado

Este capítulo muestra diferentes características avanzadas de Markdown utilizadas en el proyecto.

---

## 1. Fórmula matemática con **MathJax**

Ejemplo de regresión lineal:

\[
y = \beta_0 + \beta_1 x
\]

---

## 2. Diagrama Mermaid (Pipeline del proyecto)

```mermaid
flowchart TD
    A[Dataset Original] --> B[training.py<br>Entrenamiento]
    B --> C[model.pkl<br>Modelo entrenado]
    C --> D[prediction.py<br>Predicciones]
    D --> E[Evaluación y Resultados]


## Tabla descriptiva del dataset

| Variable     | Descripción                       |
|--------------|-----------------------------------|
| TV           | Inversión en anuncios de TV       |
| Radio        | Inversión en anuncios de radio    |
| Newspaper    | Inversión en prensa escrita       |
| Sales        | Ventas (variable objetivo)        |

---

## Ejemplo de bloque de codigo en python

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)


---

