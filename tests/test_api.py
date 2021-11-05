def test_get_item_list(app, client):
    del app
    res = client.get("/api/v1/items/")
    assert res.status_code == 200
    data = res.json
    assert data[0]["id"] == 1
    assert data[0]["name"] == "Item 1"
    assert len(data[0]["details"]) == 2


def test_post_item_to_list(app, client):
    del app
    res = client.post("/api/v1/items/", data={"id": 2, "name": "Item 2"})
    assert res.status_code == 200

    res = client.get("/api/v1/items/")
    data = res.json
    assert data[1]["id"] == 2
    assert data[1]["name"] == "Item 2"


def test_get_item(app, client):
    del app
    res = client.get("/api/v1/items/1")
    assert res.status_code == 200
    data = res.json
    assert data["id"] == 1
    assert data["name"] == "Item 1"
    assert len(data["details"]) == 2


def test_post_item_details(app, client):
    del app
    res = client.post("/api/v1/items/1", data={"id": 3, "name": "Detail 3"})
    assert res.status_code == 200

    res = client.get("/api/v1/items/1")
    data = res.json
    assert len(data["details"]) == 3
    assert data["details"][2]["id"] == 3
    assert data["details"][2]["name"] == "Detail 3"
