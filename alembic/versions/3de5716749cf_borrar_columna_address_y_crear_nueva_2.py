"""Borrar columna address y crear nueva 2

Revision ID: 3de5716749cf
Revises: c29596143df8
Create Date: 2024-11-28 16:06:09.671565

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision: str = '3de5716749cf'
down_revision: Union[str, None] = 'c29596143df8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass

def downgrade() -> None:
   pass
