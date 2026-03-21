# -*- coding: utf-8 -*-
# from odoo import http


# class .\odoo-it-assest\itAssetRequest(http.Controller):
#     @http.route('/.\odoo-it-assest\it_asset_request/.\odoo-it-assest\it_asset_request', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/.\odoo-it-assest\it_asset_request/.\odoo-it-assest\it_asset_request/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('.\odoo-it-assest\it_asset_request.listing', {
#             'root': '/.\odoo-it-assest\it_asset_request/.\odoo-it-assest\it_asset_request',
#             'objects': http.request.env['.\odoo-it-assest\it_asset_request..\odoo-it-assest\it_asset_request'].search([]),
#         })

#     @http.route('/.\odoo-it-assest\it_asset_request/.\odoo-it-assest\it_asset_request/objects/<model(".\odoo-it-assest\it_asset_request..\odoo-it-assest\it_asset_request"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('.\odoo-it-assest\it_asset_request.object', {
#             'object': obj
#         })

