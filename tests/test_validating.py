from . import client


# PARAMS


def test_with_params_not_being_object_should_return_invalid_params_exception():
    payload = {
        "jsonrpc": "2.0",
        "method": "substract",
        "params": [],
        "id": "1"
    }
    response = client.post('/api/', json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {
                "params": "Must be an object."
            }
        }
    }

# ID


def test_with_id_as_string_should_return_invalid_params_exception():
    payload = {
        "jsonrpc": "2.0",
        "method": "substract",
        "params": {},
        "id": 1
    }
    response = client.post('/api/', json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {
                "id": "Must be a string."
            }
        }
    }

# JSONRPC


def test_with_jsonrpc_as_integer():
    payload = {
        "jsonrpc": 2,
        "method": "substract",
        "params": {},
        "id": "1"
    }
    response = client.post('/api/', json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {
                "jsonrpc": "Must be a string."
            }
        }
    }


def test_with_empty_jsonrpc():
    payload = {
        "jsonrpc": "",
        "method": "substract",
        "params": {},
        "id": "1"
    }
    response = client.post('/api/', json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {
                "jsonrpc": "Must not be blank."
            }
        }
    }


def test_jsonrpc_wrong_value():
    payload = {
        "jsonrpc": "3.0",
        "method": "substract",
        "params": {},
        "id": "1"
    }
    response = client.post('/api/', json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {
                "jsonrpc": "Must match the pattern /2.0/."
            }
        }
    }


def test_payload_without_jsonrpc():
    payload = {
        "method": "substract",
        "params": {},
        "id": "1"
    }
    response = client.post('/api/', json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {
                "jsonrpc": "This field is required."
            }
        }
    }

# METHOD


def test_with_not_registered_method_should_return_method_not_found():
    payload = {
        "jsonrpc": "2.0",
        "method": "non_existing_method",
        "params": {},
        "id": "1"
    }
    response = client.post('/api/', json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32601,
            "message": "Method not found.",
            "data": {}
        }
    }


# def test_request_without_params_returns_200():
#     payload = {
#         "jsonrpc": "2.0",
#         "method": "my_method",
#         "id": "1"
#     }
#     response = client.post('/api/', json=payload)
#     assert response.status_code == 200
#
#
# def test_without_method():
#     pass
#
#
# def test_id_must_be_string():
#     pass
#


# def test_with_method_name_starting_with_rpc_period():
#     pass
#
#
# def test_without_id():
#     pass
#
#
# def test_with_empty_id():
#     pass
#
#
# def test_without_params_ok():
#     pass