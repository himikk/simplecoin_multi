"""empty message

Revision ID: 2b1f3f73f8a2
Revises: 27a4875d33de
Create Date: 2014-03-22 12:54:29.724196

"""

# revision identifiers, used by Alembic.
revision = '2b1f3f73f8a2'
down_revision = '27a4875d33de'

from alembic import op
import sqlalchemy as sa
from simpledoge.models import Payout


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bonus_payout', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('payout', sa.Column('created_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('payout', 'created_at')
    op.drop_column('bonus_payout', 'created_at')
    ### end Alembic commands ###