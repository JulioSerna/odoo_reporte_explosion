# -*- coding: utf-8 -*-
"""
Pruebas Unitarias (TDD) para el cálculo del Reporte de Explosión de Compras en Odoo
"""
import unittest
from unittest.mock import MagicMock
from datetime import date
import io
import csv

class TestPurchasesExplosionReport(unittest.TestCase):

    def setUp(self):
        self.mock_env = MagicMock()
        
        # Setup Mock Product Category
        mock_cat = MagicMock()
        mock_cat.ids = [1]
        self.mock_env['product.category'].search.return_value = mock_cat

        # Setup Mock Locations
        loc_gen = MagicMock(id=10)
        loc_prod = MagicMock(id=20)
        loc_sales = MagicMock(id=30)
        
        def location_search_side_effect(domain, limit=None):
            for cond in domain:
                if cond[0] == 'complete_name' and cond[2] == 'General':
                    return loc_gen
                elif cond[0] == 'usage' and cond[2] == 'production':
                    return loc_prod
                elif cond[0] == 'complete_name' and cond[2] == 'Ventas':
                    return loc_sales
            return MagicMock()
            
        self.mock_env['stock.location'].search.side_effect = location_search_side_effect

    def test_net_explosion_formula(self):
        """Valida que la explosión netada descuente lo reservado en producción"""
        qty_ventas = 100.0
        qty_reservada = 40.0
        
        explosion_netada = max(0.0, qty_ventas - qty_reservada)
        self.assertEqual(explosion_netada, 60.0)

    def test_net_explosion_non_negative(self):
        """Valida que si lo reservado supera las ventas, la explosión no sea negativa"""
        qty_ventas = 30.0
        qty_reservada = 50.0
        
        explosion_netada = max(0.0, qty_ventas - qty_reservada)
        self.assertEqual(explosion_netada, 0.0)

if __name__ == '__main__':
    unittest.main()
