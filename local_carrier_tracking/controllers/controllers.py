# -*- coding: utf-8 -*-
# from odoo import http


# class ProductPricing(http.Controller):
#     @http.route('/product_pricing/product_pricing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_pricing/product_pricing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_pricing.listing', {
#             'root': '/product_pricing/product_pricing',
#             'objects': http.request.env['product_pricing.product_pricing'].search([]),
#         })

#     @http.route('/product_pricing/product_pricing/objects/<model("product_pricing.product_pricing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_pricing.object', {
#             'object': obj
#         })
