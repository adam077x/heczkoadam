"""empty message

Revision ID: 801a2f9426df
Revises: 5fd11cd04b70
Create Date: 2022-04-30 22:00:04.833834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '801a2f9426df'
down_revision = '5fd11cd04b70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('content', sa.Text(), nullable=True))
    op.add_column('project', sa.Column('content', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'content')
    op.drop_column('blog', 'content')
    # ### end Alembic commands ###
