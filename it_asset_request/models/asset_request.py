from odoo import _, api, fields, models

class ItAssetRequest(models.Model):
    _name = 'it.asset.request'
    _description = 'IT Asset Request'
    
    name = fields.Char('name')

    employee_name = fields.Char(
        required=True
    )

    employee_email = fields.Char()

    request_date = fields.Date(
        default=lambda self: fields.Date.today()
    )

    asset_type = fields.Selection(
        selection=[
            ('laptop', 'Laptop'),
            ('monitor', 'Monitor'),
            ('keyboard', 'Keyboard'),
            ('mouse', 'Mouse'),
            ('license', 'License'),
        ],
        required=True
    )

    justification = fields.Text()

    priority = fields.Selection(
        selection=[
            ('no_priority', 'No Priority'),
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High'),
        ]
    )

    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('submitted', 'Submitted'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ],
        default='draft'   
    )

    approved_by_id = fields.Many2one('res.users')

    approval_date = fields.Datetime()

    is_urgent = fields.Boolean(
        string='Is Urgent?'
    )

    estimated_cost = fields.Float('estimated_cost')