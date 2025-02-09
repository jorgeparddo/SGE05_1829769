{
    'name': "Alquiler de Películas",
    'version': '1.0',
    'summary': "Módulo para gestionar el alquiler de películas",
    'description': """
        Este módulo permite gestionar un sistema de alquiler de películas, 
        definiendo modelos para películas, categorías y actores, con vistas,
        menús, datos de ejemplo e informes básicos.
    """,
    'author': "JorgePardoSGE1829769",
    'website': "http://www.peliculasbyJorge.com",
    'category': 'Management',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/pelicula_view.xml',
        'views/categoria_view.xml',
        'views/actor_view.xml',
        'views/rental_menu.xml',
        'data/demo.xml',
        'reports/report_peliculas.xml',  # Archivo del informe
    ],
    'installable': True,
    'application': True,
}
