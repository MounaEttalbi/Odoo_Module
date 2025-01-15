from odoo import models, fields, api

class Commande(models.Model):
    _name = 'gestion.commande'
    _description = 'Gestion des Commandes'

    name = fields.Char(string='Numéro de Commande', required=True)
    customer_id = fields.Many2one('res.partner', string='Client', required=True)
    order_date = fields.Date(string='Date de Commande', default=fields.Date.today)
    product_ids = fields.Many2many('product.product', string='Produits')
    total_amount = fields.Float(string='Montant Total', compute='_compute_total_amount', store=True)

    @api.depends('product_ids')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = sum(product.list_price for product in record.product_ids)
