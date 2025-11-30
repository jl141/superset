# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""add on delete cascade or set null for ab_user.id references

Revision ID: 5d5866f4c88a
Revises: c233f5365c9e
Create Date: 2025-11-30 08:38:38.140661

"""

# revision identifiers, used by Alembic.
revision = '5d5866f4c88a'
down_revision = 'c233f5365c9e'

from superset.migrations.shared.constraints import ForeignKey, redefine_exact

cascade_fks = [
    ForeignKey(table="favstar", referent_table="ab_user", local_cols=["user_id"], remote_cols=["id"]),
    ForeignKey(table="query", referent_table="ab_user", local_cols=["user_id"], remote_cols=["id"]),
    ForeignKey(table="saved_query", referent_table="ab_user", local_cols=["user_id"], remote_cols=["id"]),
    ForeignKey(table="tab_state", referent_table="ab_user", local_cols=["user_id"], remote_cols=["id"]),
    ForeignKey(table="user_attribute", referent_table="ab_user", local_cols=["user_id"], remote_cols=["id"]),
    ForeignKey(table="user_favorite_tag", referent_table="ab_user", local_cols=["user_id"], remote_cols=["id"]),
]

set_null_fks = [
    ForeignKey(table="logs", referent_table="ab_user", local_cols=["user_id"], remote_cols=["id"]),
    ForeignKey(table="ab_user", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="ab_user", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="annotation", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="annotation", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="annotation_layer", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="annotation_layer", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="css_templates", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="css_templates", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="dashboards", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="dashboards", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="database_user_oauth2_tokens", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="database_user_oauth2_tokens", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="dbs", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="dbs", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="dynamic_plugin", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="dynamic_plugin", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="key_value", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="key_value", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="report_recipient", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="report_recipient", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="report_schedule", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="report_schedule", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="row_level_security_filters", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="row_level_security_filters", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="saved_query", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="saved_query", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="slices", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="slices", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="slices", referent_table="ab_user", local_cols=["last_saved_by_fk"], remote_cols=["id"]),
    ForeignKey(table="sql_metrics", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="sql_metrics", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="tab_state", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="tab_state", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="table_columns", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="table_columns", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="table_schema", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="table_schema", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="tables", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="tables", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="tag", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="tag", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="tagged_object", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="tagged_object", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="themes", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="themes", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
    ForeignKey(table="user_attribute", referent_table="ab_user", local_cols=["changed_by_fk"], remote_cols=["id"]),
    ForeignKey(table="user_attribute", referent_table="ab_user", local_cols=["created_by_fk"], remote_cols=["id"]),
]

def upgrade():
    for foreign_key in cascade_fks:
        redefine_exact(foreign_key, on_delete="CASCADE")
    for foreign_key in set_null_fks:
        redefine_exact(foreign_key, on_delete="SET NULL")


def downgrade():
    for foreign_key in cascade_fks:
        redefine_exact(foreign_key)
    for foreign_key in set_null_fks:
        redefine_exact(foreign_key)
