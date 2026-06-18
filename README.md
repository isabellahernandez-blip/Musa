# Musa:
Musa es una aplicación desarrollada en **Python** utilizando la librería **Tkinter**, diseñada para ayudar a creadores de contenido, influencers y community managers a organizar proyectos, dar seguimiento a su estado y estimar cuánto cobrar por cada trabajo.

## Funcionalidades

### 📝 Registrar proyectos
El usuario puede ingresar:
* Título del proyecto
* Marca o cliente
* Plataforma
* Fecha límite
* Prioridad
* Dificultad

### 📋 Agenda de proyectos
Los proyectos se organizan automáticamente en tres estados:
* Pendiente
* Completando
* Completado
Cada proyecto puede avanzar entre estados mediante botones dentro de la agenda.

### 💰 Finanzas
La aplicación calcula automáticamente:

* Total ganado por proyectos completados
* Total pendiente de cobrar
* Cantidad total de proyectos registrados
* Lista de proyectos completados

## Cálculo de precios

### Dificultad
| Dificultad | Precio Base |
| ---------- | ----------- |
| Baja       | Q100        |
| Media      | Q200        |
| Alta       | Q300        |

### Prioridad
| Prioridad  | Incremento |
| ---------- | ---------- |
| Flexible   | Q0         |
| Importante | Q50        |
| Crítico    | Q100       |

### Fórmula
Precio Final = Precio Base + Incremento por Prioridad

## Requisitos
* Python 3.14 o superior
* Tkinter (incluido por defecto en Python)

## Cómo ejecutar el proyecto
1. Clonar el repositorio:
```bash
git clone https://github.com/isabellahernandez-blip/Musa.git
```

2. Entrar a la carpeta del proyecto:
```bash
cd Musa
```

3. Ejecutar la aplicación:
```bash
python main.py
```

## Tecnologías utilizadas
* Python
* Tkinter
* Git
* GitHub

## Autora
**Isabella Reyes Hernández**
Proyecto desarrollado para el curso de Programación 1.
