# 1. Registro de Decisiones de Arquitectura (ADRs)

* **Estado**: Aceptado
* **Fecha**: 2026-09-12
* **Autor**: Julio Serna Hernández / Antigravity AI

## Contexto
El proyecto requiere una metodología de desarrollo limpia y estructurada cuando se trabaja con asistentes de inteligencia artificial. Es necesario mantener una trazabilidad histórica de por qué se tomaron ciertas decisiones de diseño, algoritmos o arquitectura en Odoo.

## Decisión
Adoptamos el formato Nygard para Architecture Decision Records (ADR). Todos los registros se guardarán secuencialmente en `docs/adrs/NNNN-titulo.md` con las secciones:
1. Título y Estado
2. Contexto
3. Decisión
4. Consecuencias

## Consecuencias
* **Positivas**: Trazabilidad completa para el cliente, desarrolladores futuros y la IA en sesiones posteriores.
* **Negativas**: Mantenimiento mínimo de documentos Markdown al tomar decisiones clave.
