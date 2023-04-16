from pydantic import BaseModel, Field
from psychonaut.lexicon.formats import (
    validate_did, validate_array, validate_cid
)
from typing import Optional, List, Any
from psychonaut.api.session import Session


class GetCommitPathReq(BaseModel):
    """
    Gets the path of repo commits
    """
    did: str = Field(..., description='The DID of the repo.', pre=True, validator=validate_did)
    latest: Optional[str] = Field(default=None, description='The most recent commit', pre=True, validator=validate_cid)
    earliest: Optional[str] = Field(default=None, description='The earliest commit to start from', pre=True, validator=validate_cid)

    @property
    def xrpc_id(self) -> str:
       return "com.atproto.sync.getCommitPath"


class GetCommitPathResp(BaseModel):
    commits: List[str] = Field(..., pre=True, validator=validate_array(validate_cid))

    @property
    def xrpc_id(self) -> str:
       return "com.atproto.sync.getCommitPath"


async def get_commit_path(sess: Session, req: GetCommitPathReq) -> GetCommitPathResp:
    resp = await sess.query(req)
    return GetCommitPathResp(**resp)
