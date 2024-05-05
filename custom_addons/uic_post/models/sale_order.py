from odoo import fields, models, _

SALE_ORDER_STATE = [
    ('received', _("Received")),
    ('canceled', _("Canceled")),
    ('on_the_way', _("On the way")),
    ('delivered', _("Delivered")),
    ('done', _("Done")),
]


class SaleOrder(models.Model):
    _inherit = "sale.order"

    state = fields.Selection(
        selection_add=SALE_ORDER_STATE,
        default="received",
        ondelete={'received': 'set default'}, readonly=False,
        copy=True, store=True, index=True
    )
    receiver_office_id = fields.Many2one(comodel_name='res.company', string=_("Receiver Office"), required=True)
    destination_office_id = fields.Many2one(comodel_name='res.company', string=_("Destination Office"), required=True)

    def action_taken(self):
        return self.write({'state': 'received'})

    def action_cancelled(self):
        return self.write({'state': 'canceled'})
