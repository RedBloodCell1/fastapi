"""add content column to posts table

Revision ID: f5635bc27969
Revises: 2f264e91145a
Create Date: 2023-04-19 18:15:41.104946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5635bc27969'
down_revision = '2f264e91145a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
