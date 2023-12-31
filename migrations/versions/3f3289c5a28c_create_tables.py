"""Create Tables

Revision ID: 3f3289c5a28c
Revises: 320c33f0524f
Create Date: 2023-06-02 12:51:19.014341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f3289c5a28c'
down_revision = '320c33f0524f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('league',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('stadium', sa.String(length=100), nullable=False),
    sa.Column('nickname', sa.String(length=100), nullable=False),
    sa.Column('id_league', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_league'], ['league.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('id_team', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_team'], ['team.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player')
    op.drop_table('team')
    op.drop_table('league')
    # ### end Alembic commands ###
