"""add feedback report metrics"""

from alembic import op
import sqlalchemy as sa


revision = "0002_add_feedback_metrics"
down_revision = "0001_initial"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("feedback_reports", sa.Column("role_alignment", sa.Float(), nullable=False, server_default="0"))
    op.add_column("feedback_reports", sa.Column("answer_quality", sa.Float(), nullable=False, server_default="0"))
    op.add_column("feedback_reports", sa.Column("improvement_momentum", sa.Float(), nullable=False, server_default="0"))


def downgrade() -> None:
    op.drop_column("feedback_reports", "improvement_momentum")
    op.drop_column("feedback_reports", "answer_quality")
    op.drop_column("feedback_reports", "role_alignment")
