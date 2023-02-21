"""rest of content table

Revision ID: 9179759973df
Revises: 8ba5188e4fbe
Create Date: 2023-02-20 19:58:29.939611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9179759973df"
down_revision = "8ba5188e4fbe"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts", sa.Column("created_at",sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text("now()"),))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
