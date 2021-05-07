"""empty message

Revision ID: b7aad9405bd7
Revises: fae8912bf04b
Create Date: 2021-05-07 20:48:42.796496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7aad9405bd7'
down_revision = 'fae8912bf04b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parent', sa.Column('parent_1', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'parent', 'parent', ['parent_1'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'parent', type_='foreignkey')
    op.drop_column('parent', 'parent_1')
    # ### end Alembic commands ###
