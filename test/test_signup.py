import pytest
import requests
import json

@pytest.fixture
def url():
	return "https://stagingapi.autographamt.com"

def sign_up(url,firstName,lastName,email,password):
	url = url + "/v1/registrations"  
	data = {'firstName':firstName,
            'lastName':lastName,
            'email':email,
			'password':password}
	resp = requests.post(url, data=data)
	return resp

def test_signup_load():
	url = "https://staging.autographamt.com/signup"
	resp = requests.get(url)
	assert resp.status_code == 200, resp.text

@pytest.mark.parametrize("firstName,lastName,email, password",[('ag','ag','ag19*@yopmail.com',"1189")])
def test_sign_up_successful(url,firstName,lastName,email,password):
	resp = sign_up(url,firstName,lastName,email,password)
	j = json.loads(resp.text)
	assert resp.status_code == 200, request.text
	assert j['success'] == True,str(j['success'])
	assert j['message'] == "Verification Email has been sent to your email id",str(j['message'])


@pytest.mark.parametrize("firstName,lastName,email, password",[('ag','2','ag2@yopmil.com',"1189")])
def test_sign_up_fail(url,firstName,lastName,email,password):
	resp = sign_up(url,firstName,lastName,email,password)
	j = json.loads(resp.text)
	assert resp.status_code == 200, request.text
	assert j['success'] == False,str(j['success'])
	assert j['message'] == "This email has already been Registered, ",str(j['message'])

