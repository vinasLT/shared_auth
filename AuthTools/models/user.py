from pydantic import BaseModel

class HeaderUser(BaseModel):
    uuid: str
    email: str
    roles: list[str]
    token_expire: str
    permissions: list[str]

