# 📘 Práctica 2 — Documentación del Proyecto de Predicción

Bienvenidos al libro interactivo creado para la Práctica 2 del curso.  
En este proyecto hemos desarrollado un modelo de *Machine Learning* utilizando el dataset **Advertising**, cuyo objetivo es predecir las *ventas* en función de la inversión en:

- Televisión  
- Radio  
- Prensa escrita  

---

## Objetivo del proyecto

El propósito del trabajo es aplicar un pipeline completo de ciencia de datos:

1. **Exploración y análisis** del dataset.  
2. **Entrenamiento de un modelo** de regresión lineal.  
3. **Generación de predicciones**.  
4. **Documentación completa** usando Markdown y Jupyter Book.  
5. **Validación de código** con *pre-commit hooks*.

---

## Contenido del libro

Este Jupyter Book incluye:

- Explicaciones del proyecto en formato Markdown.  
- Notebooks con análisis y modelos entrenados.  
- Código comentado siguiendo buenas prácticas.  
- Visualizaciones y ejemplos reproducibles.

---

## Sobre el dataset

El dataset **Advertising** contiene:

| Columna | Descripción |
|--------|-------------|
| TV | Inversión en anuncios de televisión |
| Radio | Inversión en anuncios de radio |
| Newspaper | Inversión en prensa escrita |
| Sales | Ventas generadas (variable objetivo) |

---

## Estructura del pipeline

```mermaid
flowchart TD
    A[dataset.csv] --> B[training.py]
    B --> C[model.pkl]
    D[nuevos_datos.csv] --> E[prediction.py]
    C --> E
    E --> F[predicciones.csv]
