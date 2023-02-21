"""add content column to posts table

Revision ID: 45493d3f4adc
Revises: 3fb4d4a841fc
Create Date: 2023-02-20 19:25:48.685557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "45493d3f4adc"
down_revision = "3fb4d4a841fc"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "posts",
        sa.Column("content", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
