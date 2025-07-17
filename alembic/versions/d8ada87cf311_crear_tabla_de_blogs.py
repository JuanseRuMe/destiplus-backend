"""Crear tabla de blogs

Revision ID: d8ada87cf311
Revises: 69b521c501ff
Create Date: 2025-05-15 10:46:33.904010

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'd8ada87cf311'
down_revision: Union[str, None] = '69b521c501ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('articles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('slug', sa.String(length=255), nullable=False),
    sa.Column('title', sa.Text(), nullable=False),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.Column('author', sa.String(length=150), nullable=True),
    sa.Column('publication_date', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('display_date', sa.String(length=50), nullable=True),
    sa.Column('reading_time', sa.String(length=30), nullable=True),
    sa.Column('hero_image_url', sa.Text(), nullable=True),
    sa.Column('hero_image_alt', sa.Text(), nullable=True),
    sa.Column('excerpt', sa.Text(), nullable=True),
    sa.Column('meta_description', sa.Text(), nullable=True),
    sa.Column('keywords', postgresql.ARRAY(sa.Text()), nullable=True),
    sa.Column('content', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('related_articles', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug', name=op.f('uq_articles_slug')) # Usamos op.f para nombres de constraints consistentes
    )


def downgrade() -> None:
    op.drop_table('articles')

