"""drop the protein_group - uniprot_metadata association table

Revision ID: 872099067902
Revises: 44ba6dcc835d
Create Date: 2022-02-22 19:19:48.288602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '872099067902'
down_revision = '44ba6dcc835d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        'idx_protein_group_uniprot_metadata_association_protein_group_id',
        table_name='protein_group_uniprot_metadata_association',
    )
    op.drop_index(
        'idx_protein_group_uniprot_metadata_association_uniprot_id',
        table_name='protein_group_uniprot_metadata_association',
    )
    op.drop_table('protein_group_uniprot_metadata_association')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'protein_group_uniprot_metadata_association',
        sa.Column('uniprot_id', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column('protein_group_id', sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ['protein_group_id'],
            ['mass_spec_protein_group.id'],
            name='fk_protein_group_uniprot_metadata_association_protein_g_debe',
        ),
        sa.ForeignKeyConstraint(
            ['uniprot_id'],
            ['uniprot_metadata.uniprot_id'],
            name='fk_protein_group_uniprot_metadata_association_uniprot_i_0738',
        ),
        sa.PrimaryKeyConstraint(
            'uniprot_id', 'protein_group_id', name='pk_protein_group_uniprot_metadata_association'
        ),
    )
    op.create_index(
        'idx_protein_group_uniprot_metadata_association_uniprot_id',
        'protein_group_uniprot_metadata_association',
        ['uniprot_id'],
        unique=False,
    )
    op.create_index(
        'idx_protein_group_uniprot_metadata_association_protein_group_id',
        'protein_group_uniprot_metadata_association',
        ['protein_group_id'],
        unique=False,
    )
    # ### end Alembic commands ###
