def response(data: any, code: int, message: str, error: bool):
    return {
        "data": data,
        'code': code,
        'message': message,
        'error': error
    }
