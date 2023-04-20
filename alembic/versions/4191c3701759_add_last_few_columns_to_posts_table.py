"""add last few columns to posts table

Revision ID: 4191c3701759
Revises: 970e47fa20ce
Create Date: 2023-04-19 19:05:53.175202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4191c3701759'
down_revision = '970e47fa20ce'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
