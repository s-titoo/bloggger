"""add language column to post table

Revision ID: 964b7c074c7e
Revises: 5bc8bf848dfb
Create Date: 2020-12-28 17:15:13.218467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '964b7c074c7e'
down_revision = '5bc8bf848dfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.String(length=5), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    # ### end Alembic commands ###