"""add_secure_hash_link_boefje_meta

Revision ID: 0005
Revises: 0004
Create Date: 2022-03-23 14:28:54.048206

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0005"
down_revision = "0004"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    op.add_column("boefje_meta", sa.Column("secure_hash", sa.String(), nullable=True))
    op.add_column("boefje_meta", sa.Column("hash_retrieval_link", sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_column("boefje_meta", "hash_retrieval_link")
    op.drop_column("boefje_meta", "secure_hash")

    # ### end Alembic commands ###
