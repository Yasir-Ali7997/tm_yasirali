# -*- coding: utf-8 -*-
{
    'name': "Task Management",

    'summary': "Task Management Module is about to task and its deadline",

    'description': """
    Task Management Module is about to task and its deadline
    """,
    'author': "Yasir Ali Khan",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '17.0',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/task_wizard.xml',
        'views/task.xml',
        'report/report.xml',
        'report/task_report.xml',
    ],
}
