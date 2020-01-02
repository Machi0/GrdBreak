"""empty message

Revision ID: 12d8868b21d4
Revises: 
Create Date: 2020-01-01 15:56:25.938182

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12d8868b21d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('unib_combos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character', sa.String(length=15), nullable=False),
    sa.Column('ver', sa.String(length=10), nullable=False),
    sa.Column('damage', sa.Integer(), nullable=False),
    sa.Column('cs', sa.Boolean(), nullable=False),
    sa.Column('ch', sa.Boolean(), nullable=False),
    sa.Column('starter', sa.String(length=10), nullable=False),
    sa.Column('meter', sa.Integer(), nullable=False),
    sa.Column('yt', sa.String(length=300), nullable=True),
    sa.Column('tw', sa.String(length=300), nullable=True),
    sa.Column('bullets', sa.Integer(), nullable=True),
    sa.Column('enh', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_unib_combos_bullets'), 'unib_combos', ['bullets'], unique=False)
    op.create_index(op.f('ix_unib_combos_ch'), 'unib_combos', ['ch'], unique=False)
    op.create_index(op.f('ix_unib_combos_character'), 'unib_combos', ['character'], unique=False)
    op.create_index(op.f('ix_unib_combos_cs'), 'unib_combos', ['cs'], unique=False)
    op.create_index(op.f('ix_unib_combos_damage'), 'unib_combos', ['damage'], unique=False)
    op.create_index(op.f('ix_unib_combos_enh'), 'unib_combos', ['enh'], unique=False)
    op.create_index(op.f('ix_unib_combos_meter'), 'unib_combos', ['meter'], unique=False)
    op.create_index(op.f('ix_unib_combos_starter'), 'unib_combos', ['starter'], unique=False)
    op.create_index(op.f('ix_unib_combos_tw'), 'unib_combos', ['tw'], unique=False)
    op.create_index(op.f('ix_unib_combos_ver'), 'unib_combos', ['ver'], unique=False)
    op.create_index(op.f('ix_unib_combos_yt'), 'unib_combos', ['yt'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_unib_combos_yt'), table_name='unib_combos')
    op.drop_index(op.f('ix_unib_combos_ver'), table_name='unib_combos')
    op.drop_index(op.f('ix_unib_combos_tw'), table_name='unib_combos')
    op.drop_index(op.f('ix_unib_combos_starter'), table_name='unib_combos')
    op.drop_index(op.f('ix_unib_combos_meter'), table_name='unib_combos')
    op.drop_index(op.f('ix_unib_combos_enh'), table_name='unib_combos')
    op.drop_index(op.f('ix_unib_combos_damage'), table_name='unib_combos')
    op.drop_index(op.f('ix_unib_combos_cs'), table_name='unib_combos')
    op.drop_index(op.f('ix_unib_combos_character'), table_name='unib_combos')
    op.drop_index(op.f('ix_unib_combos_ch'), table_name='unib_combos')
    op.drop_index(op.f('ix_unib_combos_bullets'), table_name='unib_combos')
    op.drop_table('unib_combos')
    # ### end Alembic commands ###
