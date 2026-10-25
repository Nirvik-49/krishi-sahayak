from fastapi import FastAPI, Request, Form, Depends, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.database import get_db, User
from app.services.auth_service import AuthService
from app.api.v1_endpoints import router as api_router

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

# Add session middleware for login state
app.add_middleware(SessionMiddleware,
                   secret_key="krishi-sahayak-super-secret-key")

templates = Jinja2Templates(directory="app/templates")
app.include_router(api_router, prefix="/api/v1")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    user_name = request.session.get("user")
    return templates.TemplateResponse(request, "index.html", {"title": settings.APP_NAME, "user_name": user_name})


@app.get("/chat", response_class=HTMLResponse)
async def chat(request: Request):
    user_name = request.session.get("user")
    return templates.TemplateResponse(request, "chat.html", {"title": settings.APP_NAME, "user_name": user_name})


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    user_name = request.session.get("user")
    if not user_name:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse(request, "dashboard.html", {"title": settings.APP_NAME, "user_name": user_name})


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    user_name = request.session.get("user")
    return templates.TemplateResponse(request, "about.html", {"title": settings.APP_NAME, "user_name": user_name})


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    user_name = request.session.get("user")
    return templates.TemplateResponse(request, "contact.html", {"title": settings.APP_NAME, "user_name": user_name})

# --- Auth Routes ---


@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(request, "login.html", {"title": settings.APP_NAME})


@app.post("/login", response_class=HTMLResponse)
async def login_submit(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == email).first()
    # Wrapped user.hashed_password with str() to resolve type checker warnings
    if not user or not AuthService.verify_password(password, str(user.hashed_password)):
        return templates.TemplateResponse(
            request, "login.html", {
                "title": settings.APP_NAME, "error": "Invalid email or password"}
        )
    # Save user name in session
    request.session["user"] = user.full_name
    return RedirectResponse(url="/dashboard", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse(request, "register.html", {"title": settings.APP_NAME})


@app.post("/register", response_class=HTMLResponse)
async def register_submit(
    request: Request,
    full_name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        return templates.TemplateResponse(
            request, "register.html", {
                "title": settings.APP_NAME, "error": "Email already registered"}
        )
    hashed_pwd = AuthService.hash_password(password)
    new_user = User(full_name=full_name, email=email,
                    hashed_password=hashed_pwd)
    db.add(new_user)
    db.commit()
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
