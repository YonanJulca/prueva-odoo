from odoo import models, fields, api
import qrcode
import io
import base64

class AccountMove(models.Model):
    _inherit = 'account.move'

    serial_number = fields.Char(string='Número de Serie', compute='_compute_serial_number')
    correlativo = fields.Char(string='Número Correlativo', compute='_compute_correlativo')
    issue_date = fields.Datetime(string='Fecha de Emisión', default=fields.Datetime.now)
    sales_channel_id = fields.Many2one('sales.channel', string='Canal de Ventas')
    picking_ids = fields.Many2many('stock.picking', string='Transferencias', compute='_compute_picking_ids')
    x_qr_invoice = fields.Binary(string='Código QR', compute='_generate_qr_code')

    @api.depends('name')
    def _compute_serial_number(self):
        for record in self:
            record.serial_number = 'FV' + str(record.date.year)

    @api.depends('name')
    def _compute_correlativo(self):
        for record in self:
            record.correlativo = str(record.id).zfill(8)

    @api.depends('sale_id')
    def _compute_picking_ids(self):
        for record in self:
            record.picking_ids = self.env['stock.picking'].search([('sale_id', '=', record.sale_id.id)])

    def _generate_qr_code(self):
        for record in self:
            qr_string = f"{record.name}|{record.partner_id.name}|{record.invoice_date}|{sum(line.quantity for line in record.invoice_line_ids)}|{record.amount_total}"
            qr = qrcode.QRCode(version=4, box_size=4, border=1)
            qr.add_data(qr_string)
            qr.make(fit=True)
            img = qr.make_image()
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            img_str = base64.b64encode(buffer.getvalue())
            record.x_qr_invoice = img_str
