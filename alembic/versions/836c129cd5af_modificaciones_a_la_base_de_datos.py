"""Modificaciones a la base de datos

Revision ID: 836c129cd5af
Revises: bfd5ede32360
Create Date: 2024-11-04 13:38:35.793225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '836c129cd5af'
down_revision: Union[str, None] = 'bfd5ede32360'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass

def downgrade() -> None:
    pass
