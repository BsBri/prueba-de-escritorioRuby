#!/usr/bin/env python
"""
Script de prueba para el analizador Ruby sin interfaz gráfica
Útil para verificar que los módulos funcionen correctamente
"""

import sys
sys.path.insert(0, '.')

from lexico import lexer, errores_lexicos
import main
import ply.yacc as yacc

def analizar_codigo_ruby(codigo):
    """Analiza código Ruby y muestra los resultados"""
    print("\n" + "="*60)
    print("📋 ANALIZADOR RUBY - MODO TERMINAL")
    print("="*60)
    
    # Limpiar errores previos
    errores_lexicos.clear()
    main.errores_sintacticos.clear()
    main.errores_semanticos.clear()
    main.advertencias_semanticas.clear()
    
    print(f"\n📝 Código a analizar:\n{codigo}\n")
    
    # ANÁLISIS LÉXICO
    print("-" * 60)
    print("🔤 ANÁLISIS LÉXICO")
    print("-" * 60)
    
    lexer.input(codigo)
    tokens_encontrados = []
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens_encontrados.append({
            'tipo': tok.type,
            'valor': tok.value,
            'linea': tok.lineno
        })
    
    if tokens_encontrados:
        print(f"✅ Se encontraron {len(tokens_encontrados)} tokens:\n")
        for i, token in enumerate(tokens_encontrados, 1):
            print(f"  {i}. {token['tipo']:15} = {str(token['valor']):20} (línea {token['linea']})")
    else:
        print("⚠️  No se encontraron tokens")
    
    if errores_lexicos:
        print(f"\n❌ Errores léxicos encontrados:")
        for error in errores_lexicos:
            print(f"  - {error}")
        return
    
    # ANÁLISIS SINTÁCTICO
    print("\n" + "-" * 60)
    print("🔧 ANÁLISIS SINTÁCTICO")
    print("-" * 60)
    
    try:
        parser = yacc.yacc(module=main, debug=False, write_tables=False)
        resultado = parser.parse(codigo, lexer=lexer)
        print("✅ Estructura sintáctica válida")
        
        if main.errores_sintacticos:
            print(f"\n❌ Errores sintácticos:")
            for error in main.errores_sintacticos:
                print(f"  - {error}")
        
    except Exception as e:
        print(f"❌ Error sintáctico: {e}")
        if main.errores_sintacticos:
            for error in main.errores_sintacticos:
                print(f"  - {error}")
    
    # ERRORES SEMÁNTICOS
    if main.errores_semanticos:
        print("\n" + "-" * 60)
        print("⚠️  ERRORES SEMÁNTICOS")
        print("-" * 60)
        for error in main.errores_semanticos:
            print(f"  ❌ {error}")
    
    # ADVERTENCIAS
    if main.advertencias_semanticas:
        print("\n" + "-" * 60)
        print("⚠️  ADVERTENCIAS")
        print("-" * 60)
        for advertencia in main.advertencias_semanticas:
            print(f"  ⚠️  {advertencia}")
    
    # RESUMEN
    print("\n" + "=" * 60)
    print("📊 RESUMEN")
    print("=" * 60)
    print(f"Tokens léxicos:     {len(tokens_encontrados)}")
    print(f"Errores léxicos:    {len(errores_lexicos)}")
    print(f"Errores sintácticos: {len(main.errores_sintacticos)}")
    print(f"Errores semánticos: {len(main.errores_semanticos)}")
    print(f"Advertencias:       {len(main.advertencias_semanticas)}")
    
    total_errores = len(errores_lexicos) + len(main.errores_sintacticos) + len(main.errores_semanticos)
    
    if total_errores == 0:
        if len(main.advertencias_semanticas) == 0:
            print("\n✅ ¡Análisis exitoso! El código es válido.")
        else:
            print(f"\n⚠️  Código válido pero con {len(main.advertencias_semanticas)} advertencia(s)")
    else:
        print(f"\n❌ Se encontraron {total_errores} error(es)")
    
    print("=" * 60 + "\n")

# Ejemplos de código Ruby
EJEMPLOS = {
    "simple": "x = 5\nputs x",
    "variables": 'nombre = "Juan"\nedad = 30\nputs nombre',
    "if": "if x > 0\n  puts \"positivo\"\nend",
    "while": "i = 0\nwhile i < 10\n  puts i\n  i = i + 1\nend",
    "for": "for i in 1..5\n  puts i\nend",
    "array": "arr = [1, 2, 3, 4, 5]\nputs arr[0]",
    "hash": 'persona = { nombre: "Juan", edad: 30 }\nputs persona[:nombre]',
}

if __name__ == "__main__":
    print("\n🚀 Iniciando pruebas del analizador Ruby...\n")
    
    if len(sys.argv) > 1 and sys.argv[1] in EJEMPLOS:
        # Analizar un ejemplo específico
        ejemplo = sys.argv[1]
        codigo = EJEMPLOS[ejemplo]
        analizar_codigo_ruby(codigo)
    else:
        # Mostrar ejemplos disponibles
        print("📚 Ejemplos disponibles:")
        for nombre in EJEMPLOS.keys():
            print(f"  python test_analyzer.py {nombre}")
        
        print("\n🔄 Ejecutando todos los ejemplos...\n")
        for nombre, codigo in EJEMPLOS.items():
            print(f"\n{'#'*60}")
            print(f"# Ejemplo: {nombre.upper()}")
            print(f"{'#'*60}")
            analizar_codigo_ruby(codigo)
            input("Presiona Enter para continuar...")
