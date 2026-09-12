# Reglas del Proyecto AGY: Reporte de Explosión de Compras en Odoo

## 🎯 Información del Proyecto
Este repositorio contiene la solución técnica y metodología para el **Reporte de Planificación y Explosión de Compras en Odoo**.

## 📏 Reglas y Metodología del Proyecto
1. **Regla de Cálculo de Explosión Netada**:
   $$\text{Explosión Netada} = \max(0, \text{Cantidad Necesitada en Ventas} - \text{Cantidad Reservada en Producción})$$
   * No volver a contar como necesidad de compras aquellos insumos que ya se encuentran reservados en órdenes de producción activas.

2. **Criterio de Consumos**:
   * Filtrar únicamente movimientos de inventario (`stock.move`) con destino a producción (`usage == 'production'`) cuyo estado sea realizado (`state == 'done'`). Excluir mermas y devoluciones.

3. **Entregable**:
   * Código autocontenido para **Acción de Servidor (`ir.actions.server`)** que genera y descarga dinámicamente un archivo `.csv`.

4. **Seguridad y Pruebas de Integración (`mcp-odoo`)**:
   * **Cero credenciales en código**: Jamás guardar credenciales, URLs, usuarios o contraseñas en archivos del repositorio.
   * Las pruebas de integración (verificar que la Server Action no falle y que los datos sean correctos) y el despliegue a producción se ejecutan a través de **AGY** utilizando el servidor MCP local de Odoo (`mcp-odoo`).

## 🧪 Comandos Obligatorios de Verificación
Antes de entregar cualquier cambio en la lógica de negocio, se deben ejecutar:
* **Validación de Sintaxis**: `python3 scripts/validate.py`
* **Pruebas Unitarias**: `python3 -m unittest discover tests`
* **Empaquetado de Entregable**: `python3 scripts/package.py`
