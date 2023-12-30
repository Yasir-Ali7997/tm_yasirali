# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class TaskWizard(models.TransientModel):
    _name = 'task.wizard'
    _description = 'Task Wizard'

    from_date = fields.Date(string='From Date')
    to_date = fields.Date(string='Till Date', default=fields.Date.today)

    def process_pdf_report(self):
        data = {
            'from_date': self.from_date,
            'to_date': self.to_date,
        }
        return self.env.ref("task_manager.task_report_action").report_action(self, data=data)
