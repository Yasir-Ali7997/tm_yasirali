# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError


class Task(models.Model):
    _name = 'task'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Task'

    name = fields.Char(string='Title')
    deadline = fields.Date(string='Deadline', required=True, tracking=True)
    description = fields.Text(string='Description')
    no_of_days = fields.Float(compute="_compute_no_of_days", string='Days Left', store=True, tracking=True)
    state = fields.Selection(
        string='State',
        selection=[('draft', 'Draft'),
                   ('completed', 'Completed')],
        required=False, default='draft', tracking=True)

    @api.depends('deadline')
    def _compute_no_of_days(self):
        for record in self:
            if record.deadline:
                current_date = fields.date.today()
                difference = (record.deadline - current_date).days
                record.no_of_days = difference if difference >= 0 else 0
            else:
                record.no_of_days = 0

    def unlink(self):
        for record in self:
            if record.state != 'draft':
                raise ValidationError("You Cannot Delete a Record which Is Completed!")
        return super(Task, self).unlink()
