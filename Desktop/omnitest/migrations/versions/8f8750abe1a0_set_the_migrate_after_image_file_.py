"""set the migrate after image_file lengthe sessioncls

Revision ID: 8f8750abe1a0
Revises: 
Create Date: 2024-11-14 10:38:14.332031

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8f8750abe1a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('image_file',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=225),
               existing_nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('image_file',
               existing_type=mysql.VARCHAR(length=20),
               type_=sa.String(length=225),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('image_file',
               existing_type=sa.String(length=225),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=False)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.alter_column('image_file',
               existing_type=sa.String(length=225),
               type_=mysql.VARCHAR(length=20),
               existing_nullable=False)

    # ### end Alembic commands ###
