"""add users table

Revision ID: 283cb0cea0c9
Revises: 45493d3f4adc
Create Date: 2023-02-20 19:31:46.341431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '283cb0cea0c9'
down_revision = '45493d3f4adc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                  server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
