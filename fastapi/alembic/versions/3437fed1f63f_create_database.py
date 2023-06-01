"""create database

Revision ID: 3437fed1f63f
Revises: 
Create Date: 2023-05-19 18:07:38.320914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3437fed1f63f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.String(length=250), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('address', sa.String(length=250), nullable=True),
    sa.Column('state', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_address'), 'users', ['address'], unique=False)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_address'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###