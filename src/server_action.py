# -*- coding: utf-8 -*-
"""
Acción de Servidor Odoo: Reporte de Explosión y Planificación de Compras en CSV
Autor: Julio Serna Hernández / Antigravity AI
Fecha: 2026-09-12
"""
import base64
import csv
import io
from datetime import date, datetime, timedelta

def generate_purchases_explosion_csv(env):
    today = date.today()
    first_day_this_month = today.replace(day=1)
    first_day_prev_month = (first_day_this_month - timedelta(days=1)).replace(day=1)
    last_day_prev_month = first_day_this_month - timedelta(days=1)

    # Filtrar productos de la categoría 'Materia Prima'
    categories = env['product.category'].search([('name', 'ilike', 'Materia Prima')])
    category_ids = categories.ids
    all_cat_ids = env['product.category'].search([('id', 'child_of', category_ids)]).ids

    products = env['product.product'].search([
        ('categ_id', 'in', all_cat_ids),
        ('active', '=', True)
    ])

    # Ubicaciones clave
    loc_general = env['stock.location'].search([('complete_name', 'ilike', 'General')], limit=1)
    loc_production = env['stock.location'].search([('usage', '=', 'production')], limit=1)
    loc_sales = env['stock.location'].search([('complete_name', 'ilike', 'Ventas')], limit=1)

    output = io.StringIO()
    writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow([
        'Clave / Referencia',
        'Producto',
        'Almacén General',
        'Almacén Proceso/Producción',
        'Almacén Ventas (Reservado)',
        'Explosión Netada',
        'Consumo Mes Actual',
        'Consumo Mes Anterior'
    ])

    for product in products:
        stock_gen = product.with_context(location=loc_general.id).qty_available if loc_general else 0.0
        stock_proc = product.with_context(location=loc_production.id).qty_available if loc_production else 0.0
        stock_ventas = product.with_context(location=loc_sales.id).outgoing_qty if loc_sales else 0.0

        sol_lines = env['sale.order.line'].search([
            ('product_id', '=', product.id),
            ('order_id.state', 'in', ['sale', 'done'])
        ])
        qty_ventas_necesaria = sum(sol_lines.mapped('product_uom_qty'))

        mrp_moves = env['stock.move'].search([
            ('product_id', '=', product.id),
            ('raw_material_production_id.state', 'in', ['confirmed', 'progress']),
            ('state', 'in', ['assigned', 'partially_available'])
        ])
        
        qty_reservada_prod = sum(
            mrp_moves.mapped('reserved_availability') if hasattr(mrp_moves, 'reserved_availability') 
            else mrp_moves.mapped('product_uom_qty')
        )

        explosion_netada = max(0.0, qty_ventas_necesaria - qty_reservada_prod)

        qty_attr_this = 'quantity_done' if hasattr(env['stock.move'], 'quantity_done') else 'product_uom_qty'

        moves_this_month = env['stock.move'].search([
            ('product_id', '=', product.id),
            ('location_dest_id.usage', '=', 'production'),
            ('state', '=', 'done'),
            ('date', '>=', first_day_this_month.strftime('%Y-%m-%d 00:00:00')),
            ('date', '<=', today.strftime('%Y-%m-%d 23:59:59'))
        ])
        consumo_mes_actual = sum(moves_this_month.mapped(qty_attr_this))

        moves_prev_month = env['stock.move'].search([
            ('product_id', '=', product.id),
            ('location_dest_id.usage', '=', 'production'),
            ('state', '=', 'done'),
            ('date', '>=', first_day_prev_month.strftime('%Y-%m-%d 00:00:00')),
            ('date', '<=', last_day_prev_month.strftime('%Y-%m-%d 23:59:59'))
        ])
        consumo_mes_anterior = sum(moves_prev_month.mapped(qty_attr_this))

        writer.writerow([
            product.default_code or '',
            product.name or '',
            round(stock_gen, 2),
            round(stock_proc, 2),
            round(stock_ventas, 2),
            round(explosion_netada, 2),
            round(consumo_mes_actual, 2),
            round(consumo_mes_anterior, 2)
        ])

    csv_content = output.getvalue().encode('utf-8')
    output.close()

    filename = 'Reporte_Planificacion_Compras_%s.csv' % today.strftime('%Y%m%d')

    attachment = env['ir.attachment'].create({
        'name': filename,
        'datas': base64.b64encode(csv_content),
        'mimetype': 'text/csv',
        'res_model': 'ir.actions.server',
    })

    return {
        'type': 'ir.actions.act_url',
        'url': '/web/content/%s?download=true' % attachment.id,
        'target': 'self',
    }

# Invocación directa en el contexto de Odoo Server Action:
if 'env' in locals() or 'env' in globals():
    action = generate_purchases_explosion_csv(env)
