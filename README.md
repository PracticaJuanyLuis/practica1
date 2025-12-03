# Proyecto de Predicción — Advertising Dataset

 

## Introducción

Este proyecto forma parte de la **Práctica 2** de la asignatura **Herramientas de Trabajo Colaborativo**.

El objetivo es documentar el flujo de trabajo del proyecto, preparar un sistema de pre-commit funcional

y generar una documentación interactiva utilizando **Jupyter Book**.

 

## Problema a resolver

El objetivo es predecir la variable **Sales** en función de la inversión publicitaria en distintos medios:

**TV**, **Radio** y **Newspaper**.

 

## Descripción del dataset

Dataset original de Kaggle: **Advertising Dataset**.

 

| Columna     | Descripción |

|-------------|-------------|

| TV          | Inversión en televisión |

| Radio       | Inversión en radio |

| Newspaper   | Inversión en prensa escrita |

| Sales       | Ventas (variable objetivo) |

 

- ~200 muestras 

- Sin valores nulos 

- Problema de regresión 

 

## Pipeline del proyecto

 

```mermaid

flowchart TD

    A[dataset.csv] --> B[training.py]

    B --> C[model.pkl]

    C --> D[prediction.py]

    A --> E[test_training.py]