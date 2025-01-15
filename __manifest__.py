{
    'name': 'Gestion Commandes',
    'version': '1.0',
    'author': 'Votre Nom',
    'category': 'Custom',
    'summary': 'Module pour gérer les commandes des clients',
    'description': """
Gestion des commandes pour les clients, incluant :
- Création de commandes
- Suivi de l’état des commandes
    """,
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/gestion_commandes_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}