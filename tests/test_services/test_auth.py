from app.services.auth import AuthService

def test_invalid_login():
    assert AuthService.authenticate("wrong", "wrong") is None