# -*- coding: utf-8 -*-
# from odoo import http


# class ShifaaHr(http.Controller):
#     @http.route('/shifaa_hr/shifaa_hr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shifaa_hr/shifaa_hr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shifaa_hr.listing', {
#             'root': '/shifaa_hr/shifaa_hr',
#             'objects': http.request.env['shifaa_hr.shifaa_hr'].search([]),
#         })

#     @http.route('/shifaa_hr/shifaa_hr/objects/<model("shifaa_hr.shifaa_hr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shifaa_hr.object', {
#             'object': obj
#         })
