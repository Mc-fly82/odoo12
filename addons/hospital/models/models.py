# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hospital(models.Model):
    _name = 'hospital.hospital'

    patient_name = fields.Char(string='Name')
    patient_age = fields.Integer('Age')
    notes = fields.Text(string='Notes')
    # description = fields.Text()
