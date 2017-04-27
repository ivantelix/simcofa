# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Empresa(models.Model):
	_name = 'simcofa.empresa'

	rif = fields.Char(string="rif", size=10, required=True, unique=True, help='Ingrese el rif EJ:j204875366')
	nombre = fields.Char(size=100, required=True, unique=True, help='Razon Social de la Empresa')
	fecha_ini = fields.Datetime(auto_now=True)	