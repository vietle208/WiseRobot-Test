# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Project Module',
    'version': '1.0',
    'description': 'Custom project module to modify the user_ids field from res.users to hr.employee',
    'depends': ['base', 'project', 'employees'],
    'installable': True, 
}