"""empty message

Revision ID: 3a474543b9b0
Revises: 8dfb5002ecc4
Create Date: 2020-05-26 10:12:41.471809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a474543b9b0'
down_revision = '8dfb5002ecc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('path', sa.String(length=32), nullable=True),
    sa.Column('pid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_menu')
    # ### end Alembic commands ###