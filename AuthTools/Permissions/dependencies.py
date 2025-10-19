from typing import Callable

from fastapi import Depends
from rfc9457 import UnauthorisedProblem

from AuthTools.Permissions.serialize import get_user
from AuthTools.models.user import HeaderUser


def require_permissions(*required_permissions: str)-> Callable[[HeaderUser], HeaderUser]:
    """
    Check if user has required permissions

    Args:
        required_permissions: list of required permissions
    Raises:
         UnauthorisedProblem: if user doesn't have required permissions
    Returns:
        Dependency for FastAPI
    """
    def dependency(user: HeaderUser = Depends(get_user)) -> HeaderUser:
        missing_permissions = [
            perm for perm in required_permissions
            if perm not in user.permissions
        ]

        if missing_permissions:
            raise UnauthorisedProblem(
                detail=f"Insufficient rights. Required: {', '.join(missing_permissions)}"
            )
        return user
    return dependency

def require_one_of_permissions(*permissions: str)-> Callable[[HeaderUser], HeaderUser]:
    """
    Check if user has one of required permissions
    Args:
        *permissions: list of required permissions

    Returns:
        HeaderUser:

    """

    def dependency(user: HeaderUser = Depends(get_user)) -> HeaderUser:
        founded_permissions = []
        for prem in permissions:
            if prem in user.permissions:
                founded_permissions.append(prem)
        if not founded_permissions:
            raise UnauthorisedProblem(
                detail=f"Insufficient rights. Required: {', '.join(permissions)}"
            )
        return user
    return dependency



def require_roles(*required_roles: str):
    def dependency(user: HeaderUser = Depends(get_user)) -> HeaderUser:
        if not any(role in user.roles for role in required_roles):
            raise UnauthorisedProblem(
                detail=f"One of the roles is required: {', '.join(required_roles)}"
            )
        return user
    return dependency