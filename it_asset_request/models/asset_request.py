from odoo import _, api, fields, models
from odoo.exceptions import UserError

class ItAssetRequest(models.Model):
    _name = 'it.asset.request'
    _description = 'IT Asset Request'

    company_id = fields.Many2one(
        comodel_name='res.company',
        required=True, 
        default=lambda self: self.env.company
    )

    name = fields.Char(
        required=True,
        default='New',
        copy=False,
    )

    employee_name = fields.Char(
        required=True
    )

    employee_email = fields.Char()

    request_date = fields.Date(
        default=lambda self: fields.Date.today(),
        copy=False,
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
        default='draft',
        copy=False,
    )

    approved_by_id = fields.Many2one(
        comodel_name='res.users',
        copy=False,
    )

    approval_date = fields.Datetime(
        copy=False,
    )

    is_urgent = fields.Boolean(
        string='Is Urgent?'
    )

    estimated_cost = fields.Float()
    
    display_name_info = fields.Char(
        compute='_compute_display_name_info'
    )

    @api.model_create_multi
    def create(self, vals_list):
        Sequence = self.env['ir.sequence']
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
               vals['name'] = Sequence.next_by_code('it.asset.request')

        return super(ItAssetRequest, self).create(vals)
    
    @api.constrains('estimated_cost')
    def _constrains_estimated_cost(self):
        for request in self:
            if request.estimated_cost < 0:
                raise UserError(_('The estimated cost cannot be negative.'))
    
    @api.depends('asset_type', 'employee_name', 'priority')
    def _compute_display_name_info(self):
        for request in self:
            features = [request.asset_type, request.employee_name, request.priority]
            request.display_name_info = " - ".join(filter(None, features))

    @api.onchange('asset_type')
    def _onchange_asset_type(self):
        self.is_urgent = True if self.asset_type in ('laptop', 'license') else False

    def action_send(self):
        return self.write({'state': 'submitted'})
    
    def action_approve(self):
        return self.write({
            'state': 'approved',
            'approved_by_id': self.env.uid,
            'approval_date': fields.Datetime.now()
        })
    
    def action_reject(self):
        return self.write({'state': 'rejected'})