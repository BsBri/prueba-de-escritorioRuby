import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(__file__))

try:
    from lexico import lexer, errores_lexicos
    # Importar main para obtener el parser
    import main
    import ply.yacc as yacc
    from main import errores_sintacticos, errores_semanticos, advertencias_semanticas
except ImportError as e:
    print(f"Error importando módulos: {e}")
    sys.exit(1)

from datetime import datetime

class AnalizadorRubyGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Ruby - Léxico y Sintáctico")
        self.root.geometry("1200x700")
        
        # Estilo
        style = ttk.Style()
        style.theme_use('clam')
        
        # Frame principal
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame superior - Editor
        editor_frame = ttk.LabelFrame(main_frame, text="📝 Editor de Código Ruby", padding=10)
        editor_frame.pack(fill=tk.BOTH, expand=True, padx=0, pady=(0, 10))
        
        # Área de texto para código
        self.code_text = scrolledtext.ScrolledText(
            editor_frame,
            wrap=tk.WORD,
            height=20,
            font=("Courier New", 11),
            bg="#f5f5f5"
        )
        self.code_text.pack(fill=tk.BOTH, expand=True)
        
        # Frame de botones
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Botón Analizar
        analyze_btn = ttk.Button(
            button_frame,
            text="🔍 Analizar Código",
            command=self.analizar_codigo
        )
        analyze_btn.pack(side=tk.LEFT, padx=5)
        
        # Botón Limpiar
        clear_btn = ttk.Button(
            button_frame,
            text="🗑️  Limpiar",
            command=self.limpiar
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Frame para resultados
        results_frame = ttk.LabelFrame(main_frame, text="📊 Resultados del Análisis", padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Notebook para pestañas
        self.notebook = ttk.Notebook(results_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña Léxico
        lexico_frame = ttk.Frame(self.notebook)
        self.notebook.add(lexico_frame, text="Análisis Léxico")
        
        self.lexico_text = scrolledtext.ScrolledText(
            lexico_frame,
            wrap=tk.WORD,
            height=12,
            font=("Courier New", 10),
            bg="#f0f0f0"
        )
        self.lexico_text.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña Sintáctico
        sintactico_frame = ttk.Frame(self.notebook)
        self.notebook.add(sintactico_frame, text="Análisis Sintáctico")
        
        self.sintactico_text = scrolledtext.ScrolledText(
            sintactico_frame,
            wrap=tk.WORD,
            height=12,
            font=("Courier New", 10),
            bg="#f0f0f0"
        )
        self.sintactico_text.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña Semántico
        semantico_frame = ttk.Frame(self.notebook)
        self.notebook.add(semantico_frame, text="Análisis Semántico")
        
        self.semantico_text = scrolledtext.ScrolledText(
            semantico_frame,
            wrap=tk.WORD,
            height=12,
            font=("Courier New", 10),
            bg="#f0f0f0"
        )
        self.semantico_text.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña Errores
        errores_frame = ttk.Frame(self.notebook)
        self.notebook.add(errores_frame, text="Errores y Advertencias")
        
        self.errores_text = scrolledtext.ScrolledText(
            errores_frame,
            wrap=tk.WORD,
            height=12,
            font=("Courier New", 10),
            bg="#fff0f0"
        )
        self.errores_text.pack(fill=tk.BOTH, expand=True)
    
    def limpiar_errores_globales(self):
        """Limpia los errores globales de los módulos"""
        errores_lexicos.clear()
        errores_sintacticos.clear()
        errores_semanticos.clear()
        advertencias_semanticas.clear()
    
    def analizar_codigo(self):
        """Ejecuta el análisis completo del código"""
        codigo = self.code_text.get("1.0", tk.END).strip()
        
        if not codigo:
            messagebox.showwarning("Advertencia", "Por favor ingresa código Ruby para analizar")
            return
        
        # Limpiar errores previos
        self.limpiar_errores_globales()
        self.limpiar_resultados()
        
        try:
            # 1. ANÁLISIS LÉXICO
            self.analizar_lexico(codigo)
            
            # 2. ANÁLISIS SINTÁCTICO (solo si no hay errores léxicos)
            if not errores_lexicos:
                self.analizar_sintactico(codigo)
            
            # 3. Mostrar resultados
            self.mostrar_resultados()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error durante el análisis:\n{str(e)}")
    
    def analizar_lexico(self, codigo):
        """Realiza el análisis léxico"""
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
        
        # Mostrar en pestaña léxica
        resultado = "=== TOKENS ENCONTRADOS ===\n\n"
        for i, token in enumerate(tokens_encontrados, 1):
            resultado += f"{i}. Tipo: {token['tipo']:15} | Valor: {str(token['valor']):20} | Línea: {token['linea']}\n"
        
        resultado += f"\n\nTotal de tokens: {len(tokens_encontrados)}"
        
        if errores_lexicos:
            resultado += "\n\n=== ERRORES LÉXICOS ===\n"
            for error in errores_lexicos:
                resultado += f"❌ {error}\n"
        
        self.lexico_text.insert("1.0", resultado)
    
    def analizar_sintactico(self, codigo):
        """Realiza el análisis sintáctico"""
        try:
            # Obtener el parser de main
            parser = yacc.yacc(module=main, debug=False, write_tables=False)
            resultado = parser.parse(codigo, lexer=lexer)
            
            msg = "=== ANÁLISIS SINTÁCTICO ===\n\n"
            msg += "✅ El código tiene una estructura sintáctica válida\n"
            
            if errores_sintacticos:
                msg += "\n=== ERRORES SINTÁCTICOS ===\n"
                for error in errores_sintacticos:
                    msg += f"❌ {error}\n"
            
            self.sintactico_text.insert("1.0", msg)
            
        except Exception as e:
            msg = "=== ANÁLISIS SINTÁCTICO ===\n\n"
            msg += f"❌ Error sintáctico encontrado:\n{str(e)}\n"
            
            if errores_sintacticos:
                msg += "\n=== DETALLES ===\n"
                for error in errores_sintacticos:
                    msg += f"- {error}\n"
            
            self.sintactico_text.insert("1.0", msg)
    
    def mostrar_resultados(self):
        """Muestra un resumen de los resultados"""
        resultado = "=== RESUMEN DEL ANÁLISIS ===\n\n"
        
        # Contar elementos
        num_errores_lexicos = len(errores_lexicos)
        num_errores_sintacticos = len(errores_sintacticos)
        num_errores_semanticos = len(errores_semanticos)
        num_advertencias = len(advertencias_semanticas)
        
        resultado += f"📋 Errores Léxicos: {num_errores_lexicos}\n"
        resultado += f"📋 Errores Sintácticos: {num_errores_sintacticos}\n"
        resultado += f"📋 Errores Semánticos: {num_errores_semanticos}\n"
        resultado += f"⚠️  Advertencias: {num_advertencias}\n"
        
        total_errores = num_errores_lexicos + num_errores_sintacticos + num_errores_semanticos
        
        resultado += f"\n{'='*50}\n"
        if total_errores == 0 and num_advertencias == 0:
            resultado += "✅ ¡Análisis exitoso! El código es válido.\n"
        elif total_errores == 0:
            resultado += f"⚠️  Código válido pero con {num_advertencias} advertencia(s)\n"
        else:
            resultado += f"❌ Se encontraron {total_errores} error(es) en el análisis\n"
        
        # Errores semánticos
        if errores_semanticos:
            resultado += "\n=== ERRORES SEMÁNTICOS ===\n"
            for error in errores_semanticos:
                resultado += f"❌ {error}\n"
        
        # Advertencias
        if advertencias_semanticas:
            resultado += "\n=== ADVERTENCIAS ===\n"
            for advertencia in advertencias_semanticas:
                resultado += f"⚠️  {advertencia}\n"
        
        self.errores_text.insert("1.0", resultado)
    
    def limpiar_resultados(self):
        """Limpia las áreas de resultados"""
        self.lexico_text.delete("1.0", tk.END)
        self.sintactico_text.delete("1.0", tk.END)
        self.semantico_text.delete("1.0", tk.END)
        self.errores_text.delete("1.0", tk.END)
    
    def limpiar(self):
        """Limpia el editor y los resultados"""
        self.code_text.delete("1.0", tk.END)
        self.limpiar_resultados()
        self.limpiar_errores_globales()

def main():
    root = tk.Tk()
    app = AnalizadorRubyGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
