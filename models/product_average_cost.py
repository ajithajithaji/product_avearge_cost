# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Productaveragecost(models.Model):
    """Here I created a model and add a new field in product.template model"""
    _inherit = 'product.template'

    average_cost = fields.Monetary(string='Average Cost',
                                   compute='_compute_product_average_cost')

    @api.depends('average_cost')
    def _compute_product_average_cost(self):
        """Here I calculate the Average cost in a product"""
        purchase_order = self.env['purchase.order.line']
        # Loop through each product and calculate average cost
        for product in self:

            purchase_orders = purchase_order.search([('product_id', '=', product.id)])
            total_cost = sum(order.price_unit for order in purchase_orders)
            average_cost = total_cost / len(purchase_orders) if len(
                purchase_orders) > 0 else 0.0
            # Update the average cost field for the product
            product.write({'average_cost': average_cost})
