# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class HrContract(models.Model):
    _inherit = "hr.contract"

    fixed_allowance_lines = fields.One2many("fixed.allowance", "hr_contract_id")
    fixed_deduction_lines = fields.One2many("fixed.deduction", "hr_contract_id")


class FixedAllowance(models.Model):
    _name = "fixed.allowance"
    _rec_name = "name"


    hr_contract_id = fields.Many2one('hr.contract', string='Contract')
    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
    date = fields.Date(string="Date")
    amount = fields.Float(string="Amount")
    is_work_hours = fields.Boolean(string="Work Hours ?")



class FiexedDeduction(models.Model):
    _name="fixed.deduction"
    _rec_name="name"


    hr_contract_id = fields.Many2one('hr.contract', string='Contract')
    name = fields.Char(string="Name")
    description = fields.Char(string="Description")
    date = fields.Date(string="Date")
    amount = fields.Float(string="Amount")
    is_work_hours = fields.Boolean(string="Work Hours ?")
