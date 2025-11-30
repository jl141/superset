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
"""add soft delete columns

Revision ID: 1493aa956263
Revises: a9c01ec10479
Create Date: 2025-11-30 10:09:33.671802

"""

# revision identifiers, used by Alembic.
revision = '1493aa956263'
down_revision = 'a9c01ec10479'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # Add columns with server defaults for safe backfill during migration
    with op.batch_alter_table("ab_user") as batch_op:
        batch_op.add_column(
            sa.Column(
                "is_deleted",
                sa.Boolean(),
                nullable=False,
                server_default=sa.text("false"),
            )
        )
        batch_op.add_column(
            sa.Column(
                "deleted_on",
                sa.DateTime(timezone=True),
                nullable=True,
            )
        )

    # Index to accelerate filtering by is_deleted
    op.create_index(
        "idx_ab_user_is_deleted",
        "ab_user",
        ["is_deleted"],
        unique=False,
    )


def downgrade():
    # Drop index and columns
    op.drop_index("idx_ab_user_is_deleted", table_name="ab_user")
    with op.batch_alter_table("ab_user") as batch_op:
        batch_op.drop_column("deleted_on")
        batch_op.drop_column("is_deleted")

