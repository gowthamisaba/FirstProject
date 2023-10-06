{
    'name': "Ks Device Management",

    'summary': """

        Manage Ksolves Devices 

        """,

    'description': """
        With this module you can manage company devices in a software-driven manner , Where module will care take about 
        which employee is using a specfic device for a particular task. And also this module will take care how long a
        particular device employee will use.
    """,

    'author': "Ksolves",
    'website': "http://www.ksolves.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'inhouse_management', 'ks_onboarding'],

    # always loaded
    'data': ['security/ir.model.access.csv',
             'security/security.xml',
             'data/ks_category_data.xml',
             'data/mail_template.xml',
             'views/ks_device_category_view.xml',
             'views/ks_devices_view.xml',
             'views/ks_brands_view.xml',
             'views/ks_device_stage_view.xml',
             'views/ks_device_software_view.xml',
             'views/ks_device_employee_request_view.xml',
             'views/ks_device_it_team_request_view.xml',
             'views/ks_hr_employee_view.xml',
             'views/ks_device_menu.xml',
             ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
# -*- coding: utf-8 -*-

