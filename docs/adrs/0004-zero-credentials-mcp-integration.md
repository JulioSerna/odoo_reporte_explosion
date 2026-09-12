# 4. Cero Credenciales en Código y Pruebas de Integración vía MCP Odoo

* **Estado**: Aceptado
* **Fecha**: 2026-09-12
* **Autor**: Julio Serna Hernández

## Contexto
Para validar que la Server Action no genere errores y que los datos sean correctos en un entorno Odoo vivo, se requiere ejecutar pruebas de integración E2E. Almacenar credenciales, contraseñas o URLs de Odoo en archivos del repositorio (especialmente en repositorios públicos) representa un grave riesgo de seguridad.

## Decisión
1. Prohibir estrictamente guardar credenciales, URLs, usuarios o contraseñas en archivos del repositorio (`src/`, `tests/`, `scripts/`, `docs/`).
2. Realizar la verificación de integración E2E y el despliegue a producción de forma interactiva a través de **AGY** utilizando el servidor MCP de Odoo local (`mcp-odoo`), manteniendo las credenciales exclusivamente en el entorno local del usuario.

## Consecuencias
* **Positivas**: Seguridad total de credenciales del cliente en repositorios públicos; validación E2E en tiempo real en Odoo antes de liberar a producción.
* **Negativas**: Las pruebas de integración E2E requieren la presencia de AGY con el servidor `mcp-odoo` activo en el entorno local.
