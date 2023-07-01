# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HRFamily(models.Model):
    _name = 'hr.family'
    _description = 'HR Family'

    def default_family_id(self):
        family = self.env['hr.family'].search([('employee_id', '=', self.env.uid)], limit=1)
        return family

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    marriage_status = fields.Selection([
        ('father', 'Ayah'),
        ('mother', 'Ibu'),
        ('child', 'Anak'),
    ], string='Status')
    birthday = fields.Date(string='Birthday', required=True)
    sex = fields.Selection([('man','Laki-laki'),('woman','Perempuan')], string='Gender')
    marital = fields.Selection([('single','Single'),('married','Married'),('divorced','Divorced')], string='Marital Status')
    employee_id = fields.Many2one('hr.employee', string='Employee', default=default_family_id)

class Employee(models.Model):
    _inherit = 'hr.employee'

    family_ids = fields.One2many('hr.family', 'employee_id', string='Family')
    notes = fields.Text(string='Notes')
    status = fields.Boolean(string='Status')