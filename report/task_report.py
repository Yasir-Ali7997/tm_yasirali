from odoo import fields, models, api, tools, _
from odoo.exceptions import ValidationError
from datetime import datetime


class TaskReport(models.AbstractModel):
    _name = 'report.task_manager.task_report_custom'
    _description = 'Task Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        docs = self.env[model].browse(self.env.context.get('active_id'))
        date_from = docs.from_date
        date_to = docs.to_date
        domain = []
        if docs.from_date:
            domain.append(('deadline', '>=', docs.from_date))

        if docs.to_date:
            domain.append(('deadline', '<=', docs.to_date))
        records = self.env['task'].search(domain)
        return {
            'task_record': records,
            'docs': docs,
            'data': data,
            'date_from': date_from,
            'date_to': date_to,
        }
