from odoo import models, fields, api
from odoo.exceptions import UserError

class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    @api.onchange('price_unit')
    def _check_price_zero(self):
        if self.price_unit == 0:
            raise UserError(_("El precio no puede ser 0."))
