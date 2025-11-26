# 🎯 Guía de Uso - Analizador Ruby GUI

## Descripción General
Esta interfaz gráfica permite analizar código Ruby de manera sencilla, mostrando los resultados del análisis léxico, sintáctico y semántico.

## Cómo Usar

### 1. Iniciar la Aplicación
```bash
python gui.py
```

### 2. Interfaz Principal
La aplicación tiene las siguientes secciones:

#### **Sección Superior - Editor de Código**
- Área de texto donde puedes escribir o pegar código Ruby
- Soporta múltiples líneas
- Puedes usar atajos de teclado estándar (Ctrl+C, Ctrl+V, etc.)

#### **Botones de Control**
- **🔍 Analizar Código**: Ejecuta el análisis completo del código ingresado
- **🗑️ Limpiar**: Limpia el editor y los resultados

#### **Sección Inferior - Resultados**
La interfaz muestra los resultados en 4 pestañas:

1. **Análisis Léxico**
   - Muestra todos los tokens encontrados
   - Tipo de token
   - Valor del token
   - Número de línea
   - Total de tokens encontrados
   - Errores léxicos (si los hay)

2. **Análisis Sintáctico**
   - Indica si el código tiene una estructura sintáctica válida
   - Muestra errores sintácticos (si los hay)
   - Detalles de los problemas encontrados

3. **Análisis Semántico**
   - Información sobre análisis semántico
   - Advertencias de tipo o casting indebido
   - Validaciones de uso de variables

4. **Errores y Advertencias**
   - Resumen completo de todos los errores encontrados
   - Contadores de cada tipo de error
   - Estado final del análisis
   - Lista de advertencias semánticas

## Ejemplos de Código Ruby

### ✅ Código Válido
```ruby
x = 5
puts x
```

### ✅ Código con Variables
```ruby
nombre = "Juan"
edad = 30
puts nombre
```

### ✅ Estructura de Control
```ruby
if x > 0
  puts "positivo"
end
```

### ✅ Bucle While
```ruby
i = 0
while i < 10
  puts i
  i = i + 1
end
```

### ✅ Bucle For
```ruby
for i in 1..5
  puts i
end
```

### ✅ Array
```ruby
arr = [1, 2, 3, 4, 5]
puts arr[0]
```

### ✅ Hash
```ruby
persona = { nombre: "Juan", edad: 30 }
puts persona[:nombre]
```

## Interpretación de Resultados

### Estados Posibles

#### ✅ Análisis Exitoso
- El código es válido en todas las fases
- No hay errores sintácticos, léxicos ni semánticos

#### ⚠️ Código Válido con Advertencias
- El código es sintácticamente correcto
- Pero existen advertencias semánticas
- Por ejemplo: casting de tipos indebido

#### ❌ Análisis con Errores
- Se encontraron errores en una o más fases
- Verifica las pestañas para identificar el tipo de error

## Tipos de Errores

### Errores Léxicos (❌)
- Caracteres no reconocidos en el código
- Tokens mal formados
- Secuencias de caracteres inválidas

### Errores Sintácticos (❌)
- Estructura incorrecta del código
- Palabras clave mal utilizadas
- Paréntesis, corchetes o llaves desbalanceadas
- Orden incorrecto de operadores

### Errores Semánticos (❌)
- Variables utilizadas sin ser declaradas
- Tipos incompatibles en operaciones
- Operaciones no permitidas en Ruby

### Advertencias (⚠️)
- Posibles problemas que no son errores
- Casting indebido de tipos
- Código sospechoso o problemático

## Características

✨ **Interfaz Amigable**
- Diseño limpio y organizado
- Uso intuitivo de pestañas
- Emojis para mejor visualización

✨ **Análisis Completo**
- Integración con analizador léxico
- Integración con analizador sintáctico
- Captura de errores semánticos

✨ **Resultados Detallados**
- Información completa de tokens
- Líneas donde se encuentran los errores
- Tipos de error claramente identificados

## Limitaciones

- Se analiza el código tal como está escrito
- No se ejecuta el código Ruby
- Solo se valida la sintaxis y semántica básica
- Algunos comportamientos dinámicos de Ruby no se detectan

## Troubleshooting

### La interfaz no abre
```bash
# Asegúrate de que tkinter esté instalado
python -m tkinter

# Si no funciona, instálalo:
# En Ubuntu/Debian:
sudo apt-get install python3-tk

# En macOS:
brew install python-tk@3.x
```

### Error al analizar el código
- Verifica que el código Ruby sea válido
- Revisa los errores mostrados en la pestaña correspondiente
- Comprueba que uses la sintaxis correcta de Ruby

### Algunos tokens no se reconocen
- Asegúrate de que estés usando tokens válidos en Ruby
- Revisa la documentación de tokens soportados
- Verifica que no haya caracteres ocultos o especiales

## Soporte

Para reportar problemas o sugerencias:
1. Revisa la pestaña "Errores y Advertencias"
2. Verifica que el código sea válido
3. Intenta con ejemplos más simples

---

**Versión:** 1.0
**Última actualización:** Noviembre 2025
