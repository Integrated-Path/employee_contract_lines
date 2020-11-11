# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ShifaaHrExt(models.Model):
    _inherit="hr.contract"

    
    fixed_allowance_line = fields.One2many("fixed.allowance","conn")
    fixed_deduction_line = fields.One2many("fixed.deduction","conn")







class FixedAllowance(models.Model):
    _name="fixed.allowance"
    _rec_name="name"

    conn=fields.Integer()
    name=fields.Char(string="Name")
    description = fields.Char(string="Description")
    date=fields.Date(string="Date")
    amount = fields.Float(string="amount")
    


class FiexedDeduction(models.Model):
    _name="fixed.deduction"
    _rec_name="name"

    conn=fields.Integer()
    name=fields.Char(string="Name")
    description = fields.Char(string="Description")
    date=fields.Date(string="Date")
    amount = fields.Float(string="amount")