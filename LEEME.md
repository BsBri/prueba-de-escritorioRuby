# 🎯 Analizador Ruby - Interfaz Gráfica

Un analizador completo de código Ruby que realiza análisis léxico, sintáctico y semántico a través de una interfaz gráfica intuitiva.

## ✨ Características

- **📝 Editor de código integrado** - Escriba o pegue código Ruby directamente
- **🔍 Análisis Léxico** - Tokenización y validación de componentes básicos
- **🔧 Análisis Sintáctico** - Validación de estructura y gramática
- **⚙️ Análisis Semántico** - Validación de tipos y operaciones
- **📊 Resultados organizados en pestañas** - Fácil visualización de cada fase
- **❌ Detección de errores** - Identificación clara de problemas
- **⚠️ Advertencias** - Avisos sobre código sospechoso

## 🚀 Inicio Rápido

### Opción 1: Interfaz Gráfica (Recomendado)

```bash
python gui.py
```

Esto abrirá una ventana gráfica donde podrás:
1. Escribir código Ruby en el área de editor
2. Hacer clic en "🔍 Analizar Código"
3. Ver los resultados en las pestañas

### Opción 2: Terminal (Sin interfaz gráfica)

```bash
# Ejecutar todos los ejemplos
python test_analyzer.py

# Ejecutar un ejemplo específico
python test_analyzer.py simple
python test_analyzer.py for
python test_analyzer.py array
```

## 📦 Requisitos

- Python 3.7+
- `ply` (Python Lex-Yacc) - Ya incluido en `requirements.txt`
- `tkinter` (para la interfaz gráfica)

### Instalación de dependencias

```bash
# Instalar dependencias Python
pip install -r requirements.txt

# En Ubuntu/Debian (si tkinter no está disponible)
sudo apt-get install python3-tk

# En macOS
brew install python-tk@3.x
```

## 📖 Uso

### Interfaz Gráfica

1. **Escribir código**
   - Ingresa código Ruby en el editor superior
   - Puedes usar múltiples líneas
   - Usa copiar/pegar normalmente

2. **Analizar**
   - Haz clic en el botón "🔍 Analizar Código"
   - Los resultados aparecerán en las pestañas inferiores

3. **Revisar resultados**
   - **Análisis Léxico**: Lista de tokens encontrados
   - **Análisis Sintáctico**: Validación de estructura
   - **Análisis Semántico**: Validación de tipos y operaciones
   - **Errores y Advertencias**: Resumen completo

### Ejemplos de código válido

```ruby
# Asignación simple
x = 5

# Variables y salida
nombre = "Juan"
puts nombre

# Estructura if
if x > 0
  puts "positivo"
else
  puts "no positivo"
end

# Bucle while
i = 0
while i < 10
  puts i
  i = i + 1
end

# Bucle for
for i in 1..5
  puts i
end

# Array
arr = [1, 2, 3, 4, 5]
puts arr[0]

# Hash
persona = { nombre: "Juan", edad: 30 }
puts persona[:nombre]
```

## 📊 Estructura de archivos

```
.
├── gui.py                    # 🎨 Interfaz gráfica principal
├── test_analyzer.py         # 🧪 Script de pruebas sin GUI
├── main.py                  # 🔧 Analizador sintáctico (yacc)
├── lexico.py                # 🔤 Analizador léxico (lex)
├── GUI_USAGE.md            # 📖 Guía detallada de uso
├── requirements.txt         # 📦 Dependencias Python
└── algoritmos/             # 📁 Algoritmos de ejemplo
    ├── algoritmo1E.rb
    ├── algoritmo2B.rb
    └── ... (más algoritmos)
```

## 🔍 Tipos de análisis

### Análisis Léxico
- Identifica componentes básicos (tokens)
- Detecta palabras reservadas
- Reconoce literales (números, strings, símbolos)
- Valida operadores y delimitadores

### Análisis Sintáctico
- Valida la estructura del código
- Comprueba paréntesis, corchetes, llaves balanceadas
- Verifica orden correcto de elementos
- Detecta palabras clave mal utilizadas

### Análisis Semántico
- Valida tipos de datos
- Detecta variables sin declarar
- Advierte sobre operaciones incompatibles
- Identifica casting de tipos indebido

## 🛠️ Desarrollo

### Estructura de la GUI

```python
AnalizadorRubyGUI
├── __init__()          # Inicialización de interfaz
├── analizar_codigo()   # Ejecuta análisis completo
├── analizar_lexico()   # Fase léxica
├── analizar_sintactico() # Fase sintáctica
├── mostrar_resultados() # Muestra resumen
└── limpiar()           # Limpia todo
```

### Extensión de funcionalidades

Para añadir nuevos tipos de análisis:

1. Modifica `main.py` para agregar nuevas reglas gramaticales
2. Actualiza `lexico.py` para nuevos tokens si es necesario
3. Modifica `gui.py` para mostrar los nuevos resultados
4. Prueba con `test_analyzer.py`

## 📝 Notas importantes

- El analizador sigue la sintaxis estándar de Ruby
- No ejecuta el código, solo lo valida
- Algunos comportamientos dinámicos de Ruby pueden no detectarse
- Las advertencias no impiden que se muestre el código como válido

## 🐛 Troubleshooting

### "No module named 'tkinter'"
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# macOS
brew install python-tk@3.x
```

### "Error al importar main"
- Verifica que `main.py` existe en el mismo directorio
- Revisa que `lexico.py` también esté presente
- Ejecuta `python -c "import main"` para ver el error exacto

### La interfaz se congela
- Código muy complejo puede tardar en analizarse
- Espera a que termine el análisis
- Para abortar, cierra la ventana

## 📞 Soporte

Para reportar problemas:
1. Guarda el código problemático
2. Ejecuta `test_analyzer.py` con ese código
3. Revisa los errores mostrados en cada pestaña
4. Verifica la documentación en `GUI_USAGE.md`

## 📜 Licencia

Proyecto educativo desarrollado en equipo.

---

**Versión:** 1.0  
**Última actualización:** Noviembre 2025  
**Autores:** BrayanBriones, emrubio85, Juseperez
