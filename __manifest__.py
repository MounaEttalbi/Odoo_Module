{
    'name': 'Gestion Commandes',
    'version': '1.0',
    'author': 'Hajar et Mouna',
    'category': 'Custom',
    'summary': 'Module pour gérer les commandes des clients',
    'description': """
Gestion des commandes pour les clients, incluant :
- Création de commandes
- Suivi de l’état des commandes
    """,
    'depends': ['base', 'sale'],
    'data': [
        'views/gestion_commandes_views.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
