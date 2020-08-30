"""empty message

Revision ID: 49f7674bfcb8
Revises: 
Create Date: 2020-08-29 00:18:02.821863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49f7674bfcb8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Casting')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Casting',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Casting_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Casting_pkey')
    )
    # ### end Alembic commands ###
