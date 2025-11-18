from app.services.product_service import ProductService

def test_add_product():
    ProductService.add_product("Test", 10, 5)
    products = ProductService.get_products()
    assert any(p["name"] == "Test" for p in products)