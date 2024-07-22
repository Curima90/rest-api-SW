"""empty message

Revision ID: 046a7e921275
Revises: a5cffa318ac2
Create Date: 2024-07-22 19:20:41.382671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '046a7e921275'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('charId', sa.Integer(), nullable=False),
    sa.Column('charName', sa.String(length=250), nullable=True),
    sa.Column('charDescription', sa.String(length=2500), nullable=True),
    sa.Column('charOrigin', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('charId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('characters')
    # ### end Alembic commands ###
