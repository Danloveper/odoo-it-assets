from odoo import http
from odoo.http import request

class ItAssetRequestController(http.Controller):

    @http.route('/asset-request', type='http', auth='public', website=True)
    def render_asset_form(self, **kwargs):
        AssetRequest = request.env['it.asset.request']
        fields_selection = AssetRequest.fields_get(['asset_type', 'priority'])

        asset_type_options = fields_selection.get('asset_type', {}).get('selection', [])
        priority_options = fields_selection.get('priority', {}).get('selection', [])
        priority_filter = [p for p in priority_options if p[0] != 'no_priority']

        values = {
            'asset_types': asset_type_options,
            'priorities': priority_filter,
        }

        return request.render("it_asset_request.asset_request_template", values)
    
    @http.route('/asset-request/<int:request_id>', type='http', auth='public', website=True)
    def render_asset_request_info(self, request_id):

        asset_request = request.env['it.asset.request'].sudo().browse(request_id)

        if not asset_request.exists():
            return request.render('website.404')
        
        return request.render('it_asset_request.asset_request_page', {
            'asset': asset_request,
        })


    @http.route('/asset-request/submit', type='http', auth='public', methods=['POST'], website=True, csrf=True)
    def submit_asset_request(self, **post):

        asset_request_id = request.env['it.asset.request'].sudo().create({
            'employee_name': post.get('name'),
            'employee_email': post.get('email'),
            'asset_type': post.get('asset_type'),
            'priority': post.get('priority'),
            'estimated_cost': float(post.get('cost') or 0.0),
            'justification': post.get('justification'),
            'state': 'submitted',
        })
        asset_request_id._onchange_asset_type()

        return request.redirect(f'/asset-request/{asset_request_id.id}')

