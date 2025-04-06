from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    website_slogan = fields.Char(
        string="Anasayfa Sloganı",
        config_parameter='website_slogan_snippet.slogan'
    )