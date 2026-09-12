# 2. Regla de Cálculo para Explosión Netada de Materiales

* **Estado**: Aceptado
* **Fecha**: 2026-09-12
* **Autor**: Julio Serna Hernández / Margarita Ponce (Compras)

## Contexto
El reporte nativo de Odoo mostraba cantidades a explosionar infladas porque no descontaba las materias primas que ya estaban reservadas en las órdenes de producción activas. Esto obligaba al departamento de planeación a generar reportes manuales paralelos en Excel.

## Decisión
Se establece la regla de negocio explícita:
$$\text{Explosión Netada} = \max(0, \text{Cantidad Necesitada en Ventas} - \text{Cantidad Reservada en Producción})$$

Si un material ya fue reservado para una orden de producción lanzada/en proceso, se resta de las necesidades de ventas para evitar compras duplicadas.

## Consecuencias
* **Positivas**: Elimina la duplicación de necesidades de compra y alinea las cifras entre Compras y Planeación.
* **Negativas**: Requiere consultar en tiempo real las líneas de orden de venta (`sale.order.line`) y los movimientos de insumos (`stock.move`) en Odoo.
