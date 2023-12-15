"""empty message

Revision ID: bd70dc06bd9c
Revises: b71d9fad9e82
Create Date: 2023-12-15 19:20:21.366780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd70dc06bd9c'
down_revision = 'b71d9fad9e82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('climate', sa.String(length=120), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('orbital_period', sa.String(length=120), nullable=False),
    sa.Column('rotation_period', sa.String(length=120), nullable=False),
    sa.Column('diameter', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('climate'),
    sa.UniqueConstraint('diameter'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('orbital_period'),
    sa.UniqueConstraint('population'),
    sa.UniqueConstraint('rotation_period')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
