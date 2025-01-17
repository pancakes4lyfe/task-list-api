"""updates goals and tasks models

Revision ID: ea6ab613aa95
Revises: 6860bcb9a8b0
Create Date: 2021-05-10 21:58:20.465521

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea6ab613aa95'
down_revision = '6860bcb9a8b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'tasks', 'goals', ['goal_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tasks', type_='foreignkey')
    op.drop_column('tasks', 'goal_id')
    # ### end Alembic commands ###
