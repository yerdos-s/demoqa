import requests
import json
import pytest
import allure


@pytest.fixture(scope="function")
def demo_qa_host():
    yield "https://demoqa.com/Account"


@pytest.fixture(scope="function")
def request_body():
    json_file = 'user_data.json'
    with open(json_file, "r") as file:
        request_body = json.load(file)
    yield request_body


userID = None


class TestAccountRequests:
    @pytest.mark.smoke
    @pytest.mark.api_testing
    def test_create_user(self, request_body, demo_qa_host):
        with allure.step("Создаем пользователя"):
            global userID
            response = requests.post(f'{demo_qa_host}/v1/User', json=request_body, timeout=10)
            response_body = response.json()
            assert response.status_code == 201, 'The status code is not 201'
            assert response_body['username'] == request_body['userName'], \
                f'The user name is wrong, should be {request_body["userName"]}'
            userID = response_body["userID"]

    @pytest.mark.smoke
    @pytest.mark.api_testing
    def test_generate_token(self, request_body, demo_qa_host):
        with allure.step("Генерируем токен:"):
            response = requests.post(f'{demo_qa_host}/v1/GenerateToken', json=request_body, timeout=10)
            response_body = response.json()
            assert response.status_code == 200, 'The status code is not 200'
            assert response_body['status'] == 'Success', \
                f'Token generation failed, should be "Success"'
            assert response_body['result'] == 'User authorized successfully.', \
                f'User is not authorized yet. Should be "result": "User authorized successfully."'

    @pytest.mark.smoke
    @pytest.mark.api_testing
    def test_authorization(self, request_body, demo_qa_host):
        with allure.step("Авторизуемся:"):
            response = requests.post(f'{demo_qa_host}/v1/Authorized', json=request_body, timeout=10)
            response_body = response.json()
            assert response.status_code == 200, 'The status code is not 200'
            assert response_body is True, 'The user is unauthorized, expected response body to be "True"'
