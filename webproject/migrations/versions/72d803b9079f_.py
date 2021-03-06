"""empty message

Revision ID: 72d803b9079f
Revises: 7bf9b014e1a3
Create Date: 2022-05-26 15:40:02.915329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72d803b9079f'
down_revision = '7bf9b014e1a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercise__data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exercise_type', sa.String(length=200), nullable=False),
    sa.Column('exercise_time', sa.Integer(), nullable=False),
    sa.Column('exercise_note', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('health__data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('body_fat', sa.Integer(), nullable=False),
    sa.Column('body_muscle', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('signup__data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=150), nullable=False),
    sa.Column('user_id', sa.String(length=200), nullable=False),
    sa.Column('user_password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=150), nullable=False),
    sa.Column('phone', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('signup__data')
    op.drop_table('health__data')
    op.drop_table('exercise__data')
    # ### end Alembic commands ###
