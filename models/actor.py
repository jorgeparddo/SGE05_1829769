from odoo import models, fields

class Actor(models.Model):
    _name = 'rental.actor'
    _description = 'Actor'

    name = fields.Char(string="Nombre", required=True, help="Nombre del actor")
    biography = fields.Text(string="Biografía", help="Breve biografía del actor")
    pelicula_ids = fields.Many2many('rental.pelicula', string="Películas", help="Películas en las que ha actuado")
