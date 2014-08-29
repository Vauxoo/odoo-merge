# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012 Serpent Consulting Services (<http://www.serpentcs.com>)
#    Copyright (C) 2010-Today OpenERP SA (<http://www.openerp.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################


{
    "name" : "Mass Editing",
    "version" : "1.1",
    "author" : "Serpent Consulting Services",
    "category" : "Tools",
    "website" : "http://www.serpentcs.com",
    "description": """This module provides the functionality to add, update or remove the values of more than one records on the fly at the same time.
        You can configure merge editing for any OpenERP model. 
        The video explaining the features is available at http://t.co/wukYMx1A
        The menu is now Under Settings/Configuration.
        For more details/customization/feedback contact us on contact@serpentcs.com. 
    """,
    'depends': ['base'],
    'data': [
        'security/merge_security.xml',
        'security/ir.model.access.csv',
        'merge_editing_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
