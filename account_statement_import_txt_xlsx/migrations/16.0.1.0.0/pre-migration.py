# Copyright 2023 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade

_field_renames = [
    (
        "account.statement.import.sheet.mapping",
        "account_statement_import_sheet_mapping",
        "footer_lines_count",
        "footer_lines_skip_count",
    )(
        "account.statement.import.sheet.mapping",
        "account_statement_import_sheet_mapping",
        "column_labels_row",
        "header_lines_skip_count",
    )
]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_fields(env, _field_renames)
