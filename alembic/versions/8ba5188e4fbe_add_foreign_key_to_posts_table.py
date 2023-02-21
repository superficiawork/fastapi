"""add foreign key to posts table

Revision ID: 8ba5188e4fbe
Revises: 283cb0cea0c9
Create Date: 2023-02-20 19:50:30.073237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8ba5188e4fbe"
down_revision = "283cb0cea0c9"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer, nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', tablename="posts")
    op.drop_column('posts', "owner_id")
    pass
