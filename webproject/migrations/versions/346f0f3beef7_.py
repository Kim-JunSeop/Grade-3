"""empty message

Revision ID: 346f0f3beef7
Revises: f6185ed5c637
Create Date: 2022-05-29 00:26:05.597841

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '346f0f3beef7'
down_revision = 'f6185ed5c637'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('health__data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_health__data_user_id_signup__data'), 'signup__data', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('health__data', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_health__data_user_id_signup__data'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###