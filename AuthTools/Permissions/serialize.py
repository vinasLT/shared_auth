from fastapi import Header

from AuthTools.models.user import HeaderUser


def get_user(
    x_user_id: str = Header(..., alias="X-User-ID"),
    x_user_email: str = Header(..., alias="X-User-Email"),
    x_user_role: str = Header(..., alias="X-User-Role"),
    x_permissions: str = Header(..., alias="X-Permissions"),
    x_token_expires: str = Header(..., alias="X-Token-Expires")
    )-> HeaderUser:
    return HeaderUser(
        uuid=x_user_id,
        email=x_user_email,
        roles=x_user_role.split(",") if x_user_role else [],
        permissions=x_permissions.split(",") if x_permissions else [],
        token_expire=x_token_expires
    )

