"""split MicroscopyThumbnail table into separate tables for FOVs and ROIs

Revision ID: 7df168a61e78
Revises: 910a37a26ff9
Create Date: 2021-05-25 16:17:34.912246

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "7df168a61e78"
down_revision = "910a37a26ff9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "microscopy_fov_thumbnail",
        sa.Column(
            "date_created",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("fov_id", sa.Integer(), nullable=True),
        sa.Column("size", sa.Integer(), nullable=True),
        sa.Column("data", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["fov_id"],
            ["microscopy_fov.id"],
            name=op.f("fk_microscopy_fov_thumbnail_fov_id_microscopy_fov"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_microscopy_fov_thumbnail")),
    )
    op.create_table(
        "microscopy_fov_roi_thumbnail",
        sa.Column(
            "date_created",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("roi_id", sa.Integer(), nullable=True),
        sa.Column("size", sa.Integer(), nullable=True),
        sa.Column("data", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["roi_id"],
            ["microscopy_fov_roi.id"],
            name=op.f("fk_microscopy_fov_roi_thumbnail_roi_id_microscopy_fov_roi"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_microscopy_fov_roi_thumbnail")),
    )
    op.drop_table("microscopy_thumbnail")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "microscopy_thumbnail",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("fov_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("roi_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("size", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("channel", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("data", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column(
            "date_created",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["fov_id"],
            ["microscopy_fov.id"],
            name="fk_microscopy_thumbnail_fov_id_microscopy_fov",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["roi_id"],
            ["microscopy_fov_roi.id"],
            name="fk_thumbnail_roi_id_microscopy_fov_roi",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_thumbnail"),
    )
    op.drop_table("microscopy_fov_roi_thumbnail")
    op.drop_table("microscopy_fov_thumbnail")
    # ### end Alembic commands ###
