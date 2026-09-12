# Especificación de Diseño Arquitectónico: Reporte de Explosión de Compras en Odoo

**Fecha**: 2026-09-12  
**Estado**: Aprobado  
**Metodología**: AI-Driven Odoo Component (ADRs + TDD + Scripts + Git)

---

## 🎯 1. Propósito del Proyecto
Establecer un proyecto estructurado y versionado para la solución del **Reporte de Explosión y Planificación de Compras en Odoo**. Aunque el entregable final en producción es un script autocontenido ejecutado como **Acción de Servidor (`ir.actions.server`)**, el desarrollo sigue una metodología rigurosa guiada por IA con registros de decisiones arquitectónicas (ADRs), pruebas unitarias simuladas y scripts de automatización.

---

## 🏗️ 2. Estructura de Proyecto Aprobada

```text
odoo-reporte-explosion/
├── .gitignore
├── README.md
├── docs/
│   ├── adrs/
│   │   ├── 0001-record-architecture-decisions.md
│   │   ├── 0002-net-explosion-formula.md
│   │   ├── 0003-server-action-csv-export.md
│   │   └── 0004-zero-credentials-mcp-integration.md
│   └── specs/
│       └── 2026-09-12-reporte-explosion-compras-design.md
├── src/
│   └── server_action.py
├── tests/
│   └── test_server_action.py
└── scripts/
    ├── validate.py
    └── package.py
```

---

## 💡 3. Decisiones Arquitectónicas Principales (Resumen ADRs)

* **ADR-0001**: Adopción del estándar Nygard para Architecture Decision Records en la carpeta `docs/adrs/`.
* **ADR-0002**: Definición de la regla de Explosión Netada:
  $$\text{Explosión Netada} = \max(0, \text{Cantidad Necesitada en Ventas} - \text{Cantidad Reservada en Producción})$$
* **ADR-0003**: Elección de Server Action (`ir.actions.server`) en Odoo con exportación dinámica a archivo CSV como mecanismo de entrega.
* **ADR-0004**: Cero credenciales en código del repositorio y ejecución de pruebas E2E y despliegue a producción vía el servidor MCP de Odoo (`mcp-odoo`) en AGY.

---

## 🧪 4. Estrategia de Pruebas y Validación (TDD)

* **Pruebas Unitarias (`tests/test_server_action.py`)**: Utiliza `unittest` / `pytest` simulando la API ORM de Odoo mediante objetos Mock para validar:
  1. Que la resta entre ventas y reservado en producción sea exacta.
  2. Que los consumos de mes actual y mes anterior filtren por `state == 'done'` y `usage == 'production'`.
  3. Que el archivo CSV contenga las 8 columnas requeridas con formato de 2 decimales.
* **Pruebas de Integración E2E (`mcp-odoo`)**: Se ejecutan de manera interactiva a través de AGY conectándose al servidor local de Odoo mediante `mcp-odoo` sin incluir credenciales en archivos.
* **Scripts de Automatización (`scripts/`)**:
  1. `validate.py`: Valida sintaxis Python y restricciones del contexto de Odoo.
  2. `package.py`: Formatea el script de `src/server_action.py` en una cadena lista para copiar a la UI de Odoo o un snippet XML.

---

## ✅ 5. Criterios de Aceptación
1. Todos los tests en `tests/test_server_action.py` pasan exitosamente.
2. `scripts/validate.py` reporta sintaxis limpia.
3. Cero credenciales o datos sensibles guardados en archivos del repositorio.
4. La integración E2E ejecutada vía `mcp-odoo` confirma que la Server Action no arroja errores en Odoo y genera los datos correctos.
