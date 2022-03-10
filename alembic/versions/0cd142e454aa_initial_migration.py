"""initial revision

Revision ID: 0cd142e454aa
Revises:
Create Date: 2021-01-07 11:38:35.545518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0cd142e454aa"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    # these two constraints were not added/removed from the database schema
    op.create_unique_constraint(
        op.f("uq_mass_spec_cluster_heatmap_cluster_id"),
        "mass_spec_cluster_heatmap",
        ["cluster_id", "row_index", "col_index", "analysis_type"],
    )
    op.drop_constraint(
        "uq_mass_spec_cluster_heatmap_analysis_type", "mass_spec_cluster_heatmap", type_="unique"
    )

    # adding ON DELETE CASCADE to the FOV-related foreign keys without it
    op.drop_constraint(
        "fk_microscopy_fov_annotation_fov_id_microscopy_fov",
        "microscopy_fov_annotation",
        type_="foreignkey",
    )
    op.create_foreign_key(
        op.f("fk_microscopy_fov_annotation_fov_id_microscopy_fov"),
        "microscopy_fov_annotation",
        "microscopy_fov",
        ["fov_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_thumbnail_fov_id_microscopy_fov", "microscopy_thumbnail", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_microscopy_thumbnail_fov_id_microscopy_fov"),
        "microscopy_thumbnail",
        "microscopy_fov",
        ["fov_id"],
        ["id"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("fk_microscopy_thumbnail_fov_id_microscopy_fov"),
        "microscopy_thumbnail",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_thumbnail_fov_id_microscopy_fov",
        "microscopy_thumbnail",
        "microscopy_fov",
        ["fov_id"],
        ["id"],
    )
    op.drop_constraint(
        op.f("fk_microscopy_fov_annotation_fov_id_microscopy_fov"),
        "microscopy_fov_annotation",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_microscopy_fov_annotation_fov_id_microscopy_fov",
        "microscopy_fov_annotation",
        "microscopy_fov",
        ["fov_id"],
        ["id"],
    )
    op.create_unique_constraint(
        "uq_mass_spec_cluster_heatmap_analysis_type",
        "mass_spec_cluster_heatmap",
        ["analysis_type", "cluster_id", "row_index", "col_index"],
    )
    op.drop_constraint(
        op.f("uq_mass_spec_cluster_heatmap_cluster_id"),
        "mass_spec_cluster_heatmap",
        type_="unique",
    )
    # ### end Alembic commands ###