# 🎨 Interfaz Gráfica para Analizador Ruby

## ✅ Lo que se ha desarrollado

### 1. **gui.py** - Interfaz Gráfica Completa
Una aplicación gráfica moderna con tkinter que incluye:

#### Componentes:
- **📝 Editor de Código** 
  - Área de texto con scroll
  - Soporte para múltiples líneas
  - Fuente monoespaciada (Courier New)
  - Fondo claro para mejor legibilidad

- **🔍 Botones de Control**
  - Botón "Analizar Código" - Ejecuta análisis completo
  - Botón "Limpiar" - Borra editor y resultados

- **📊 Sistema de Pestañas para Resultados**
  - **Análisis Léxico** - Tokens encontrados con tipo, valor y línea
  - **Análisis Sintáctico** - Validación de estructura
  - **Análisis Semántico** - Validación de tipos
  - **Errores y Advertencias** - Resumen completo

#### Funcionalidades:
```python
✓ Análisis léxico completo
✓ Análisis sintáctico integrado
✓ Captura de errores semánticos
✓ Limpieza automática de errores previos
✓ Interfaz amigable con emojis
✓ Organización clara en pestañas
```

### 2. **test_analyzer.py** - Pruebas sin Interfaz Gráfica
Script de línea de comandos para probar la funcionalidad sin GUI:

```bash
# Ejecutar todos los ejemplos
python test_analyzer.py

# Ejecutar un ejemplo específico
python test_analyzer.py simple
python test_analyzer.py variables
python test_analyzer.py if
python test_analyzer.py while
python test_analyzer.py for
python test_analyzer.py array
python test_analyzer.py hash
```

Incluye 7 ejemplos de código Ruby válido para probar.

### 3. **Documentación Completa**

#### **LEEME.md**
- Instrucciones de instalación
- Guía de uso de la interfaz
- Ejemplos de código Ruby
- Troubleshooting
- Información sobre archivos

#### **GUI_USAGE.md**
- Guía detallada de uso de la GUI
- Descripción de cada sección
- Interpretación de resultados
- Tipos de errores
- Limitaciones conocidas

#### **setup.sh**
- Script de verificación automatizado
- Comprobación de dependencias
- Guía de instalación si hay problemas

## 🏗️ Arquitectura

```
Analizador Ruby
│
├─ ENTRADA: Código Ruby escrito en el editor
│
├─ ANÁLISIS LÉXICO (lexico.py)
│  └─ Tokenización de componentes
│
├─ ANÁLISIS SINTÁCTICO (main.py)
│  └─ Validación de estructura gramatical
│
├─ ANÁLISIS SEMÁNTICO (main.py)
│  └─ Validación de tipos y operaciones
│
└─ SALIDA: Resultados en pestañas
   ├─ Análisis Léxico
   ├─ Análisis Sintáctico
   ├─ Análisis Semántico
   └─ Errores y Advertencias
```

## 🎯 Características Principales

### ✨ Interfaz de Usuario
- Diseño limpio y organizado
- Uso intuitivo de pestañas
- Emojis para mejor visualización
- Colores diferenciados para estados

### 🔍 Análisis Completo
- **Análisis Léxico**: Identifica y clasifica tokens
- **Análisis Sintáctico**: Valida estructura del código
- **Análisis Semántico**: Detecta errores de tipo y lógica

### 📊 Presentación de Resultados
- Tokens con información completa
- Errores claramente identificados
- Advertencias destacadas
- Resumen ejecutivo

### 🛠️ Flexibilidad
- GUI para usuarios no-técnicos
- Terminal para desarrolladores
- Fácil de extender

## 📦 Archivos Creados/Modificados

```
✅ gui.py (9.5 KB)
   - Interfaz gráfica completa con tkinter
   - Integración con analizadores léxico y sintáctico
   - Sistema de pestañas para resultados
   - Manejo de errores robusto

✅ test_analyzer.py (4.8 KB)
   - Script de pruebas sin GUI
   - 7 ejemplos de código Ruby
   - Interfaz de línea de comandos
   - Salida formateada y legible

✅ LEEME.md (5.6 KB)
   - Guía en español
   - Instrucciones completas
   - Ejemplos de código
   - Troubleshooting

✅ GUI_USAGE.md (4.6 KB)
   - Guía detallada de la GUI
   - Interpretación de resultados
   - Tipos de errores
   - Limitaciones

✅ setup.sh (Mejorado)
   - Script de verificación
   - Detección de dependencias
   - Instrucciones de instalación
```

## 🚀 Cómo Usar

### Inicio Rápido - Interfaz Gráfica
```bash
python gui.py
```

1. Escriba código Ruby en el editor
2. Haga clic en "🔍 Analizar Código"
3. Revise los resultados en las pestañas

### Pruebas - Línea de Comandos
```bash
python test_analyzer.py simple
```

Muestra análisis completo en terminal sin necesidad de GUI.

## 💻 Requisitos

- **Python 3.7+** (probado con Python 3.12)
- **ply** (PLY Lex-Yacc) - Ya incluido en requirements.txt
- **tkinter** - Para la GUI (viene con Python en la mayoría de distribuciones)

## 🔄 Flujo de Análisis

```
┌─────────────────────┐
│  Código Ruby        │
│   (ingresado)       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ ANÁLISIS LÉXICO     │
│ (lexico.py)         │
│ Genera tokens       │
└──────────┬──────────┘
           │
           ▼ ¿Errores léxicos?
           ├─ Sí → Mostrar errores
           │
           └─ No
             │
             ▼
┌─────────────────────┐
│ ANÁLISIS SINTÁCTICO │
│ (main.py)           │
│ Valida estructura   │
└──────────┬──────────┘
           │
           ▼ ¿Errores sintácticos?
           ├─ Sí → Mostrar errores
           │
           └─ No
             │
             ▼
┌─────────────────────┐
│ ANÁLISIS SEMÁNTICO  │
│ (main.py)           │
│ Validar tipos       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ RESULTADOS FINALES  │
│ (gui.py - pestañas) │
│ ✅ ó ❌             │
└─────────────────────┘
```

## 📋 Ejemplos Incluidos

1. **simple**: `x = 5; puts x`
2. **variables**: Asignación de strings y números
3. **if**: Estructura condicional
4. **while**: Bucle while
5. **for**: Bucle for in
6. **array**: Manejo de arrays
7. **hash**: Manejo de hashes

## 🎓 Educativo

Este proyecto demuestra:
- ✅ Construcción de analizadores léxicos
- ✅ Implementación de parsers sintácticos
- ✅ Análisis semántico básico
- ✅ Diseño de interfaces gráficas
- ✅ Manejo de errores
- ✅ Integración de componentes

## 🔧 Extensibilidad

El código es fácil de extender:

1. **Nuevos tokens**: Agregar en `lexico.py`
2. **Nuevas reglas**: Agregar en `main.py`
3. **Nuevas pestañas**: Modificar `gui.py`
4. **Nuevos ejemplos**: Agregar a `EJEMPLOS` en `test_analyzer.py`

## 📞 Soporte

### Si la GUI no abre:
```bash
# En Ubuntu/Debian
sudo apt-get install python3-tk

# En Fedora
sudo dnf install python3-tkinter

# En macOS
brew install python-tk@3.x
```

### Si hay error de importación:
```bash
# Verificar que los archivos estén en el mismo directorio
ls -la *.py

# Reinstalar dependencias
pip install -r requirements.txt
```

## ✨ Conclusión

Se ha desarrollado una **interfaz gráfica completa y funcional** para el analizador Ruby que permite:

✅ Escribir código Ruby directamente en la aplicación
✅ Analizar código con un solo clic
✅ Ver resultados organizados y claros
✅ Identificar errores fácilmente
✅ Usar tanto GUI como línea de comandos

**¡La aplicación está lista para usar!**

---

**Versión:** 1.0
**Fecha:** Noviembre 2025
**Estado:** ✅ Completo y funcional