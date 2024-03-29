"""@

Revision ID: bc88ebe76b95
Revises:
Create Date: 2022-02-28 23:13:25.000301

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "bc88ebe76b95"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "todo_task",
        sa.Column("id", postgresql.UUID(), nullable=False),
        sa.Column("text", sa.String(length=150), nullable=False),
        sa.Column("status", sa.String(length=100), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_todo_task_id"), "todo_task", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_todo_task_id"), table_name="todo_task")
    op.drop_table("todo_task")
    # ### end Alembic commands ###
