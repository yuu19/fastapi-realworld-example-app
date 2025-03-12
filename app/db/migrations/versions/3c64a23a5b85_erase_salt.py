"""erase salt

Revision ID: 3c64a23a5b85
Revises: fdf8821871d7
Create Date: 2025-03-11 00:40:22.446695

"""
from alembic import op
import sqlalchemy as sa


revision = '3c64a23a5b85'
down_revision = 'fdf8821871d7'
branch_labels = None
depends_on = None

def upgrade():
    op.drop_column("users", "salt")


def downgrade():
    op.add_column(
        "users",
        sa.Column("salt", sa.Text, nullable=False, server_default="")  # 必要に応じて適切なサーバーデフォルト値に変更してください
    )
