"""empty message

Revision ID: 9ea3085d0529
Revises: 64bc212abfd6
Create Date: 2022-05-23 14:20:54.654774

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ea3085d0529'
down_revision = '64bc212abfd6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercise',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exercise_type', sa.String(length=200), nullable=False),
    sa.Column('exercise_time', sa.Integer(), nullable=False),
    sa.Column('exercise_note', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('profile_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile_data',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('height', sa.INTEGER(), nullable=False),
    sa.Column('weight', sa.INTEGER(), nullable=False),
    sa.Column('bmi', sa.INTEGER(), nullable=False),
    sa.Column('body_fat', sa.INTEGER(), nullable=False),
    sa.Column('body_muscle', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('exercise')
    # ### end Alembic commands ###
