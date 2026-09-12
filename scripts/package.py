#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de empaquetado para generar el payload final listo para copiar y pegar en la Server Action de Odoo UI
"""
from pathlib import Path

def package_server_action():
    src_file = Path(__file__).parent.parent / 'src' / 'server_action.py'
    output_file = Path(__file__).parent.parent / 'dist' / 'odoo_server_action_payload.py'
    output_file.parent.mkdir(exist_ok=True)

    with open(src_file, 'r', encoding='utf-8') as f:
        code = f.read()

    # Agregar invocación final para Odoo Server Action Context
    payload = code + "\n# Invocación directa en el contexto de la Server Action de Odoo:\naction = generate_purchases_explosion_csv(env)\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(payload)

    print(f"📦 Código listo para Odoo Server Action generado exitosamente en:\n   {output_file}")

if __name__ == '__main__':
    package_server_action()
