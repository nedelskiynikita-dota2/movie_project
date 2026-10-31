def test_root(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Movies API готов к работе!"}


def test_create_movie(client):
    movie_data = {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "rating": 8.7,
        "year": 2014
    }

    response = client.post("/movies/", json=movie_data)

    assert response.status_code == 200
    assert response.json()["title"] == "Interstellar"
    assert response.json()["id"] is not None


def test_get_movies(client):
    movie_data = {
        "title": "Inception",
        "genre": "Sci-Fi",
        "rating": 8.8,
        "year": 2010
    }

    client.post("/movies/", json=movie_data)
    response = client.get("/movies/")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Inception"


def test_update_movie(client):
    movie_data = {
        "title": "Inception",
        "genre": "Sci-Fi",
        "rating": 8.8,
        "year": 2010
    }

    movie_id = client.post("/movies/", json=movie_data).json()["id"]

    updated_data = {
        "title": "Inception 2",
        "genre": "Sci-Fi",
        "rating": 9.0,
        "year": 2012
    }

    response = client.put(f"/movies/{movie_id}", json=updated_data)

    assert response.status_code == 200
    assert response.json()["title"] == "Inception 2"


def test_patch_movie(client):
    movie_data = {
        "title": "The Matrix",
        "genre": "Action",
        "rating": 8.7,
        "year": 1999
    }

    movie_id = client.post("/movies/", json=movie_data).json()["id"]

    response = client.patch(
        f"/movies/{movie_id}",
        json={"rating": 9.5}
    )

    assert response.status_code == 200
    assert response.json()["rating"] == 9.5


def test_delete_movie(client):
    movie_data = {
        "title": "Avatar",
        "genre": "Fantasy",
        "rating": 7.9,
        "year": 2009
    }

    movie_id = client.post("/movies/", json=movie_data).json()["id"]

    response = client.delete(f"/movies/{movie_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Фильм удалён"

    get_response = client.get(f"/movies/{movie_id}")
    assert get_response.status_code == 404


def test_invalid_movie(client):
    movie_data = {
        "title": "A",
        "genre": "Sci-Fi",
        "rating": 15,
        "year": 1800
    }

    response = client.post("/movies/", json=movie_data)

    assert response.status_code == 422
