# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    attendance_hours = fields.Float(compute='_compute_attendance_hours', store=True)

    def _compute_attendance_hours(self):
        for record in self:
            for line in record.worked_days_line_ids:
                if line.work_entry_type_id.name == "Attendance":
                    record.attendance_hours = line.number_of_hours
                    break
                else:
                    record.attendance_hours = 0
