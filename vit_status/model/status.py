from openerp import api, fields, models

class purchase_order(models.Model):
	_inherit = "purchase.order"
	_name = "purchase.order"

	status = fields.Char(string="status", 
						compute="_status",required=False)


	@api.depends('shipped')
	def _status(self):
		for rec in self:
			for picking in self.env['stock.picking'].search([('origin','=',rec.name)]):
				if picking.state=='cancel':
					rec.status= 'reject'
				elif picking.state=='done' :
					rec.status= 'transfer'
				