#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de validación de sintaxis Python para Odoo Server Actions
"""
import ast
import sys
from pathlib import Path

def validate_python_syntax(file_path):
    print(f"🔍 Validando sintaxis de {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        ast.parse(code)
        print(f"✅ Sintaxis correcta en {file_path}")
        return True
    except SyntaxError as e:
        print(f"❌ Error de sintaxis en {file_path}: {e}")
        return False

if __name__ == '__main__':
    src_file = Path(__file__).parent.parent / 'src' / 'server_action.py'
    success = validate_python_syntax(src_file)
    if not success:
        sys.exit(1)
