# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    attendance_id = fields.Many2one('hr.payslip.worked_days', string='Attendance', compute='_compute_attendance_id')
    attendance_hours = fields.Float(related="attendance_id.number_of_hours", string='Attendance Hours')

    @api.onchange('worked_days_line_ids')
    def _compute_attendance_id(self):
        for record in self:
            for line in record.worked_days_line_ids:
                if line.work_entry_type_id.name == "Attendance":
                    record.attendance_id = line.id
                    break
            else:
                record.attendance_id = 0
