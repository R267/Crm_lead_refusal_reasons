# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'CRM Lead Refusal Reasons',
    'version': '1.0',
    'category': 'Sales/CRM',
    'summary': 'Add refusal reasons to leads',
    'description': """
        This module adds a refusal reasons selection field to CRM Leads.
    """,
    'website': 'https://www.odoo.com/app/crm',
    'depends': ['crm'],
    'data': [
        'views/crm_lead_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'LGPL-3',
}