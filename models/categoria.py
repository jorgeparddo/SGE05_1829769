from odoo import models, fields

class Categoria(models.Model):
    _name = 'rental.categoria'
    _description = 'Categoría de Películas'

    name = fields.Char(string="Nombre", required=True, help="Nombre de la categoría")
    description = fields.Text(string="Descripción", help="Descripción de la categoría")
    pelicula_ids = fields.One2many('rental.pelicula', 'category_id', string="Películas", help="Películas asociadas a esta categoría")
