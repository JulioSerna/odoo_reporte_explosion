---
name: odoo-reporte-explosion
description: "Procedimiento para actualizar, validar con TDD y empaquetar la Acción de Servidor del reporte de explosión de compras en Odoo."
---

# Skill: Odoo Reporte de Explosión de Compras

## Propósito
Este skill describe la rutina para modificar, probar y empaquetar el reporte de compras en Odoo.

## Pasos de Ejecución

1. **Revisar Especificaciones y ADRs**:
   - Leer `docs/specs/2026-09-12-reporte-explosion-compras-design.md`.
   - Consultar las decisiones en `docs/adrs/`.

2. **Modificar Código Fuente**:
   - Editar `src/server_action.py`.

3. **Ejecutar Pruebas TDD y Validación**:
   ```bash
   python3 scripts/validate.py
   python3 -m unittest discover tests
   ```

4. **Generar Entregable**:
   ```bash
   python3 scripts/package.py
   ```
   El archivo actualizado se guardará en `dist/odoo_server_action_payload.py`.
