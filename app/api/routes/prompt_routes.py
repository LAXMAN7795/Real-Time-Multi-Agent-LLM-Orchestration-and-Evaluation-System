from fastapi import (
    APIRouter,
    HTTPException
)

from pydantic import BaseModel

from app.core.prompt_store import (
    PROMPT_REWRITE_STORE
)


router = APIRouter()


class PromptApprovalRequest(BaseModel):

    rewrite_id: str

    decision: str


@router.post("/prompt-review")

async def review_prompt_rewrite(

    request: PromptApprovalRequest

):

    rewrite_id = request.rewrite_id

    decision = request.decision.lower()

    if rewrite_id not in PROMPT_REWRITE_STORE:

        raise HTTPException(

            status_code=404,

            detail={

                "error_code":
                    "REWRITE_NOT_FOUND",

                "message":
                    "Prompt rewrite not found.",

                "rewrite_id":
                    rewrite_id

            }

        )

    if decision not in [

        "approve",
        "reject"

    ]:

        raise HTTPException(

            status_code=400,

            detail={

                "error_code":
                    "INVALID_DECISION",

                "message":
                    "Decision must be "
                    "'approve' or 'reject'."

            }

        )

    if decision == "approve":

        PROMPT_REWRITE_STORE[
            rewrite_id
        ]["status"] = "approved"

    else:

        PROMPT_REWRITE_STORE[
            rewrite_id
        ]["status"] = "rejected"

    return {

        "rewrite_id": rewrite_id,

        "status":
            PROMPT_REWRITE_STORE[
                rewrite_id
            ]["status"]

    }