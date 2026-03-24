from fastapi import FastAPI, HTTPException, status, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from models import PasswordRequest, PasswordResponse, GenerateResponse

# Create the limiter — identifies users by their IP address
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="Password Strength Checker API",
    description="A cybersecurity tool to evaluate password strength.",
    version="1.0.0"
)

# Register the rate limit error handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/check", response_model=PasswordResponse)
@limiter.limit("10/minute")  # max 10 requests per minute per IP
def check_password(request: Request, body: PasswordRequest):
    if not body.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password cannot be empty."
        )
    from checker import check_password as analyze
    return analyze(body.password)


@app.get("/generate", response_model=GenerateResponse)
@limiter.limit("5/minute")  # stricter limit on generation
def generate_password(request: Request, length: int = 16):
    if length < 8 or length > 64:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Length must be between 8 and 64."
        )
    from checker import generate_strong_password, check_password as analyze
    pwd = generate_strong_password(length)
    result = analyze(pwd)
    return GenerateResponse(
        password=pwd,
        length=len(pwd),
        strength=result.strength,
        score=result.score
    )