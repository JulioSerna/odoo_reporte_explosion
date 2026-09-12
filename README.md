# Proyecto: Reporte de Explosión de Compras en Odoo (AI-Driven Component)

Este proyecto gestiona el desarrollo, pruebas unitarias y empaquetado del **Reporte de Explosión y Planificación de Compras para Odoo**.

## 📁 Estructura del Repositorio
* `docs/adrs/`: Architecture Decision Records (ADR-0001, ADR-0002, ADR-0003).
* `docs/specs/`: Especificación técnica detallada del proyecto.
* `src/`: Código fuente principal Python de la Acción de Servidor.
* `tests/`: Pruebas unitarias TDD con Mocks.
* `scripts/`: Scripts de automatización (validación de sintaxis y empaquetado).

## 🚀 Comandos Rápidos

### Validar Sintaxis Python
```bash
python3 scripts/validate.py
```

### Ejecutar Pruebas Unitarias
```bash
python3 -m unittest discover tests
```

### Empaquetar Código para Odoo UI
```bash
python3 scripts/package.py
```
El archivo resultante estará en `dist/odoo_server_action_payload.py`.
