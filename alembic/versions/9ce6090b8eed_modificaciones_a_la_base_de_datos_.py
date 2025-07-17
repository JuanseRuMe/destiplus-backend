"""Modificaciones a la base de datos, renombrar tabla restaurante_1

Revision ID: 9ce6090b8eed
Revises: 836c129cd5af
Create Date: 2024-11-04 14:35:18.351664

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ce6090b8eed'
down_revision: Union[str, None] = '836c129cd5af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('restaurantes_1', 'restaurante')


def downgrade() -> None:
    pass
