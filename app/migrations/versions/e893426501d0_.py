"""empty message

Revision ID: e893426501d0
Revises: 3ad2a5f88944
Create Date: 2020-02-15 12:07:28.594274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e893426501d0'
down_revision = '3ad2a5f88944'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo', sa.Column('completed', sa.Boolean(), nullable=True))

    op.execute('UPDATE todo SET completed = False WHERE completed IS NULL;')
    op.alter_column('todo', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo', 'completed')
    # ### end Alembic commands ###
