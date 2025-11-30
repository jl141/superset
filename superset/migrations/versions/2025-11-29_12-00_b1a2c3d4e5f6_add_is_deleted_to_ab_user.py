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
"""Add is_deleted and deleted_on to ab_user

Revision ID: b1a2c3d4e5f6
Revises: ec54aca4c8a2
Create Date: 2025-11-29 12:00:00.000000

"""

# revision identifiers, used by Alembic.
revision = "b1a2c3d4e5f6"
down_revision = "a9c01ec10479"
branch_labels = None
depends_on = None

from alembic import op  # noqa: E402
import sqlalchemy as sa  # noqa: E402


def upgrade():
    # Add columns with server defaults for safe backfill during migration
    with op.batch_alter_table("ab_user") as batch_op:
        batch_op.add_column(
            sa.Column(
                "is_deleted",
                sa.Boolean(),
                nullable=False,
                server_default=sa.false(),
            )
        )
        batch_op.add_column(
            sa.Column(
                "deleted_on",
                sa.DateTime(timezone=True),
                nullable=True,
            )
        )

    # Remove server default so future inserts rely on application defaults
    op.execute("ALTER TABLE ab_user ALTER COLUMN is_deleted DROP DEFAULT")

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
