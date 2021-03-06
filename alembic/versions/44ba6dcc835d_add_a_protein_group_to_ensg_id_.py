"""add a protein_group-to-ensg_id association table

Revision ID: 44ba6dcc835d
Revises: 7b75fd399c5e
Create Date: 2022-02-22 15:45:57.931794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44ba6dcc835d'
down_revision = '7b75fd399c5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'protein_group_ensembl_association',
        sa.Column('ensg_id', sa.String(), nullable=False),
        sa.Column('protein_group_id', sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ['ensg_id'],
            ['hgnc_metadata.ensg_id'],
            name=op.f('fk_protein_group_ensembl_association_ensg_id_hgnc_metadata'),
        ),
        sa.ForeignKeyConstraint(
            ['protein_group_id'],
            ['mass_spec_protein_group.id'],
            name=op.f(
                'fk_protein_group_ensembl_association_protein_group_id_mass_spec_protein_group'
            ),
        ),
        sa.PrimaryKeyConstraint(
            'ensg_id', 'protein_group_id', name=op.f('pk_protein_group_ensembl_association')
        ),
    )
    op.create_index(
        op.f('idx_protein_group_ensembl_association_ensg_id'),
        'protein_group_ensembl_association',
        ['ensg_id'],
        unique=False,
    )
    op.create_index(
        op.f('idx_protein_group_ensembl_association_protein_group_id'),
        'protein_group_ensembl_association',
        ['protein_group_id'],
        unique=False,
    )
    op.drop_table('ensg_protein_group_association')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'ensg_protein_group_association',
        sa.Column('ensg_id', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('protein_group_id', sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ['protein_group_id'],
            ['mass_spec_protein_group.id'],
            name='fk_ensg_protein_group_association_protein_group_id_mass_aad9',
        ),
        sa.PrimaryKeyConstraint('ensg_id', name='pk_ensg_protein_group_association'),
    )
    op.drop_index(
        op.f('idx_protein_group_ensembl_association_protein_group_id'),
        table_name='protein_group_ensembl_association',
    )
    op.drop_index(
        op.f('idx_protein_group_ensembl_association_ensg_id'),
        table_name='protein_group_ensembl_association',
    )
    op.drop_table('protein_group_ensembl_association')
    # ### end Alembic commands ###
