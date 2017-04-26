# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Empresa(models.Model):
	_name = 'simcofa.empresa'

	rif = fields.Char(string="rif", size=10, required=True, unique=True, help='Ingrese el rif EJ:j204875366')
	nombre = fields.Char(size=100, required=True, unique=True, help='Razon Social de la Empresa')
	fecha_ini = fields.DateTime(auto_now=True)
	fecha_act = fields.DateTime(auto_now=False, required=False, default=None)

	#usuario_ini
	#usuario_act

# class simcofa-coop(models.Model):
#     _name = 'simcofa-coop.simcofa-coop'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100