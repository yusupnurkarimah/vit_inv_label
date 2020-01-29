# -*- coding: utf-8 -*-
from odoo import http

# class VitInvLabel(http.Controller):
#     @http.route('/vit_inv_label/vit_inv_label/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_inv_label/vit_inv_label/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_inv_label.listing', {
#             'root': '/vit_inv_label/vit_inv_label',
#             'objects': http.request.env['vit_inv_label.vit_inv_label'].search([]),
#         })

#     @http.route('/vit_inv_label/vit_inv_label/objects/<model("vit_inv_label.vit_inv_label"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_inv_label.object', {
#             'object': obj
#         })