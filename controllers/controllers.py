# -*- coding: utf-8 -*-
# from odoo import http


# class HrFamilyFarisaffandi(http.Controller):
#     @http.route('/hr_family_farisaffandi/hr_family_farisaffandi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_family_farisaffandi/hr_family_farisaffandi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_family_farisaffandi.listing', {
#             'root': '/hr_family_farisaffandi/hr_family_farisaffandi',
#             'objects': http.request.env['hr_family_farisaffandi.hr_family_farisaffandi'].search([]),
#         })

#     @http.route('/hr_family_farisaffandi/hr_family_farisaffandi/objects/<model("hr_family_farisaffandi.hr_family_farisaffandi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_family_farisaffandi.object', {
#             'object': obj
#         })
