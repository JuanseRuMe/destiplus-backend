"""Eliminar_columna_my_table_test

Revision ID: 7a0db904b182
Revises: 
Create Date: 2024-10-15 12:41:09.747913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7a0db904b182'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column('my-table-test', 'name', new_column_name='nombre')


def downgrade() -> None:
    # Revertir cambios
    op.add_column('my-table-test', sa.Column('my_colum', sa.String(), nullable=True))

