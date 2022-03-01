# REST API with Flask
REST API made with Flask (Python)

## Table of Contents
* [General Info](#general-information)
* [Setup](#setup)
* [Usage](#usage)
* [Contact](#contact)


## General Information

With this REST API you can get, post, update and delete data. To make this actions, you need to register and login. After login, it gives you a token which you need to send in your request header to get/post data.

## Setup
To run this Rest API, you need to download and unzip the code. If you don´t have python, you need to [install it first](https://www.python.org/downloads/).

Open a terminal command in API folder and run the follow command:
```
pip install -r requirements.txt
```

After you run this command to install all dependencies, you should run the follow command:
```
python app.py
```
Now you have a local server running which allow you test the API.

## Usage

After you start the API, i recommend you to test it first. 

To test this API, i recommend that you install [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/download). I use Insomnia but feel free to use whatever you want.

### API Resources:
------
- Item;
- Store;
- User;
- Auth (login to get JWT token);

### API Endpoints:
------
### Item Resource

**Single Items**
```
{your_url}/item/<string:name>
```
**HTTP Methods available:**
- Get - get an item by its name;
- Post - insert an item with its name in url, price and corresponding store_id in body request. Example of body:
```
{
    "price":1.99,
    "store_id": 1
}
```
- Delete - delete an item by its name;
- Put - same as post. If this item not exists, it will be created.


**Multiple Items**
```
{your_url}/items
```
**HTTP Methods available:**
- Get - get all items.

### Store Resource

**Single Store**
```
{your_url}/store/<string:name>
```
**HTTP Methods available:**
- Get - get a store by its name;
- Post - insert a store with its name in url request.
- Delete - delete a store by its name;

**Multiple Stores**
```
{your_url}/stores
```
**HTTP Methods available:**
- Get - get all stores.

### User Resource

**Single User**
```
{your_url}/user/<int:user_id>
```
**HTTP Methods available:**
- Get - get an user by its id;
- Delete - delete an user by its id;



**User Register**
```
{your_url}/register
```
**HTTP Methods available:**
- Post - create an user. you need to insert in body request an username and password for your account. Example of body request:

´´´
{
    "username": "teste",
    "password": "teste"
}
´´´

### Auth Resource

**Login**
```
{your_url}/auth
```
**HTTP Methods available:**
- Post - login with your username and password to receive a JWT token. You need to put this token in all requests (except in Register and obviously for Login ) 
Example of body request:
´´´
{
    "username": "teste",
    "password": "teste"
}
´´´

**JWT Token**
In all requests you need do put the jwt token given to you in login. Example in Insomnia:

![image](https://user-images.githubusercontent.com/99747197/156261151-dea57e7b-730c-47fd-9e2e-71a8d4559a32.png)


## Contact
If you have any question, feel free to [contact me](https://www.linkedin.com/in/lu%C3%ADs-costa-793a2414b/)

