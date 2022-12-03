from fastapi import HTTPException, status


class UserExceptions:

    def __init__(self):
        self.name = "user exceptions"

    @staticmethod
    def raise_not_found(message):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=message)

    @staticmethod
    def raise_conflict(message):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=message)

    @staticmethod
    def raise_forbidden(message):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=message)