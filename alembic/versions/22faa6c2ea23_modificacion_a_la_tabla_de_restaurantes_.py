"""Modificacion a la tabla de restaurantes, eliminar clumna doble con el nombre de conctato y crear una nueva con nombre numero_contacto

Revision ID: 22faa6c2ea23
Revises: 13361d0cc5b0
Create Date: 2024-11-04 11:29:35.388879

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22faa6c2ea23'
down_revision: Union[str, None] = '13361d0cc5b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop the cuplicates contact column
    op.drop_column('restaurantes', 'contacto')


def downgrade() -> None:
    pass
