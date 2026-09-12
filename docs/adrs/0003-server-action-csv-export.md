# 3. Entregable como Acción de Servidor en UI con Exportación CSV

* **Estado**: Aceptado
* **Fecha**: 2026-09-12
* **Autor**: Julio Serna Hernández

## Contexto
Se evaluó crear un módulo `custom_addons` tradicional en Odoo vs. un script de Acción de Servidor (`ir.actions.server`) ejecutable directamente desde la UI de Odoo. Crear un módulo completo implicaba reiniciar servicios y desplegar código en el servidor de Odoo.

## Decisión
Implementar el entregable como un script Python autocontenido ejecutado como **Acción de Servidor (`ir.actions.server`)** en Odoo, el cual construye dinámicamente el contenido del reporte en formato `.csv` y desencadena la descarga directa en el navegador vía `ir.attachment` e `ir.actions.act_url`.

## Consecuencias
* **Positivas**: Despliegue inmediato en producción sin necesidad de reiniciar el servidor Odoo ni instalar addons de terceros.
* **Negativas**: El código Python en la Server Action debe ser autocontenido y no depender de librerías externas no incluidas en Odoo.
