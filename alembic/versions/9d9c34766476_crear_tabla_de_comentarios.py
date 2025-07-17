"""Crear tabla de comentarios

Revision ID: 9d9c34766476
Revises: 94b4068ce8b7
Create Date: 2025-05-27 19:02:40.526263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d9c34766476'
down_revision: Union[str, None] = '94b4068ce8b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
