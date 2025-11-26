#!/bin/bash

# Script de verificación e instalación para el Analizador Ruby GUI

echo "╔════════════════════════════════════════════════════════════╗"
echo "║    🎯 ANALIZADOR RUBY - VERIFICACIÓN DE CONFIGURACIÓN     ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Contadores
PASSED=0
FAILED=0

# Función para verificar
check_item() {
    local name=$1
    local command=$2
    
    if eval "$command" > /dev/null 2>&1; then
        echo -e "${GREEN}✅ $name${NC}"
        ((PASSED++))
    else
        echo -e "${RED}❌ $name${NC}"
        ((FAILED++))
    fi
}

# Función para listar
list_item() {
    local name=$1
    echo -e "${BLUE}   • $name${NC}"
}

echo "📋 Verificando Python..."
check_item "Python 3.7+" "python3 --version | grep -E 'Python 3\.[7-9]'"

echo ""
echo "📦 Verificando dependencias de Python..."
check_item "ply (PLY Lex-Yacc)" "python3 -c 'import ply.lex; import ply.yacc'"
check_item "tkinter (para GUI)" "python3 -m tkinter -c ''"

echo ""
echo "📁 Verificando archivos necesarios..."
check_item "gui.py (Interfaz gráfica)" "test -f gui.py"
check_item "main.py (Analizador sintáctico)" "test -f main.py"
check_item "lexico.py (Analizador léxico)" "test -f lexico.py"
check_item "test_analyzer.py (Pruebas)" "test -f test_analyzer.py"

echo ""
echo "🔍 Verificando compilación..."
check_item "gui.py compila" "python3 -m py_compile gui.py"
check_item "main.py compila" "python3 -m py_compile main.py"
check_item "lexico.py compila" "python3 -m py_compile lexico.py"
check_item "test_analyzer.py compila" "python3 -m py_compile test_analyzer.py"

echo ""
echo "═════════════════════════════════════════════════════════════"
echo -e "${GREEN}✅ Verificaciones pasadas: $PASSED${NC}"
echo -e "${RED}❌ Verificaciones fallidas: $FAILED${NC}"
echo "═════════════════════════════════════════════════════════════"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}🎉 ¡Todo está listo! Puedes iniciar la aplicación.${NC}"
    echo ""
    echo "🚀 Para iniciar la interfaz gráfica:"
    echo "   python gui.py"
    echo ""
    echo "🧪 Para probar sin interfaz gráfica:"
    echo "   python test_analyzer.py simple"
    exit 0
else
    echo -e "${YELLOW}⚠️  Se encontraron problemas. Necesitas instalar las dependencias.${NC}"
    echo ""
    echo "📝 Instalación de dependencias:"
    echo ""
    echo "1. Instalar dependencias Python:"
    echo "   pip install -r requirements.txt"
    echo ""
    echo "2. En Ubuntu/Debian (para tkinter):"
    echo "   sudo apt-get install python3-tk"
    echo ""
    echo "3. En Fedora (para tkinter):"
    echo "   sudo dnf install python3-tkinter"
    echo ""
    echo "4. En macOS (para tkinter):"
    echo "   brew install python-tk@3.x"
    echo ""
    exit 1
fi
