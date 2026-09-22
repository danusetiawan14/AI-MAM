from sqlalchemy.orm import Session

from app.models.role import Role


def get_role_by_name(
    db: Session,
    role_name: str
):
    return (
        db.query(Role)
        .filter(Role.name == role_name)
        .first()
    )