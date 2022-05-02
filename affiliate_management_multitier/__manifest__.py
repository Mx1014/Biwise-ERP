# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "Two-Tier marketing in Odoo",
  "summary"              :  """Two-Tier marketing in Odoo (Parent Commission) Extension for Odoo Affiliate Management""",
  "category"             :  "Website",
  "version"              :  "1.0.0",
  "sequence"             :  1,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "maintainer"           :  "Saurabh Gupta",
  "website"              :  "https://store.webkul.com/Odoo.html",
  "description"          :  """Two-Tier marketing in Odoo (Parent Commission) Extension for Odoo Affiliate Management""",
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=affiliate_management_multitier&version=12.0&lifetime=90&lout=1&custom_url=/",
  "depends"              :  ['affiliate_management'],
  "data"                 :  [
                             'views/affiliate_program_inherit_view.xml',
                             'views/affiliate_request_inherit_view.xml',
                             'views/affiliate_res_partner_inherit_view.xml',
                             'views/affiliate_visit_inherit_view.xml',
                             'views/report_template_inherit_view.xml',
                             'views/about_inherit_template.xml',
                             'views/affiliate_config_setting_inherit_view.xml',
                             'views/sign_up_view.xml',
                            ],
  "demo"                 :  ['data/demo_data_view.xml'],
  "images"               :  ['static/description/affiliate_multi-tier_banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "price"                :  50,
  "currency"             :  "USD",
}
