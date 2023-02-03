"""Nullable input_ooi

Revision ID: e09d8780e34b
Revises: 65a39ab3e224
Create Date: 2022-12-02 08:45:30.638883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e09d8780e34b"
down_revision = "65a39ab3e224"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("boefje_meta", "input_ooi", existing_type=sa.VARCHAR(length=128), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("boefje_meta", "input_ooi", existing_type=sa.VARCHAR(length=128), nullable=False)
    # ### end Alembic commands ###
