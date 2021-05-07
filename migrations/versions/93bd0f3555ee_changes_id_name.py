"""changes id name

Revision ID: 93bd0f3555ee
Revises: 93e61e30803e
Create Date: 2021-05-05 20:00:36.101573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93bd0f3555ee'
down_revision = '93e61e30803e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('tasks', 'task_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('task_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('tasks', 'id')
    # ### end Alembic commands ###