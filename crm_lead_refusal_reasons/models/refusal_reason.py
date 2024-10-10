# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class LeadRefusalReason(models.Model):
    _inherit = 'crm.lead'

    refusal_reason_id = fields.Many2one(
        'crm.lead.refusal.reason', string='Refusal Reason',
        help='The reason for refusing this lead/opportunity.')

class RefusalReason(models.Model):
    _name = 'crm.lead.refusal.reason'
    _description = 'Lead Refusal Reason'

    name = fields.Char('Refusal Reason', required=True)

