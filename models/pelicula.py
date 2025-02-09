from odoo import models, fields

class Pelicula(models.Model):
    _name = 'rental.pelicula'
    _description = 'Película para alquiler'

    name = fields.Char(string="Título", required=True, help="Nombre de la película")
    description = fields.Text(string="Descripción", help="Descripción breve de la película")
    release_year = fields.Integer(string="Año de Lanzamiento", help="Año en que se lanzó la película")
    state = fields.Selection([
        ('available', 'Disponible'),
        ('rented', 'Alquilada'),
        ('maintenance', 'En mantenimiento')
    ], string="Estado", default='available', required=True, help="Estado actual de la película")
    category_id = fields.Many2one('rental.categoria', string="Categoría", required=True, help="Categoría de la película")
    actor_ids = fields.Many2many('rental.actor', string="Actores", help="Actores que participan en la película")
