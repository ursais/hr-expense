# Copyright (C) 2021 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "HR Expense Journal",
    "version": "14.0.1.0.0",
    "author": "Open Source Integrators, Odoo Community Association (OCA)",
    "summary": "Expenses that are submitted are also paid by corporate credit cards.\
     Users would like to create expense reports and specify payment type,\
     i.e. Credit Card, Bank, Employee etc. Presently the option of payment\
    is available after Expense report is created under Other info tab.",
    "website": "https://github.com/OCA/hr-expense",
    "license": "AGPL-3",
    "depends": ["hr_expense"],
    "category": "HR",
    "data": [
        "views/hr_expense_views.xml",
    ],
    "installable": True,
    "maintainer": "dreispt",
    "development_status": "Beta",
}
