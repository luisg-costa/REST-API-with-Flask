# REST API with Flask
REST API made with Flask (Python)

## Table of Contents
* [General Info](#general-information)
* [Setup](#setup)
* [Usage](#usage)
* [Contact](#contact)


## General Information

With this REST API you can get, post, update and delete data. To make this actions, you need to register and login. After login, it gives you a token which you need to send in you request header to get/post data.

## Setup
To run this game, you need to download and unzip the code. If you don´t have python, you need to [install it first](https://www.python.org/downloads/).

Run a terminal command in game folder and run the follow command:
```
pip install -r requirements.txt
```

After you run this command to install all dependencies, you should run the follow command:
```
py app.py
```

## Usage

After you start the API, i recommend you to test it first. 

To test this API, i recommend that you install [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/download). I personal use Insomnia but feel free to use whatever you want.

### API Resources:
- Item;
- Store;
- User;

### API Endpoints:
#### Item Resource
**Single Items**
```
{your_url}/item/<string:name>
```
**HTTP Methods available:**

| Method | Description |
| --- | --- |
| Get | Get an item by its name |
| Post | Insert an item with its name in url, price and corresponding store_id in body request. Example of body:
```
{
    "price":1.99,
    "store_id": 1
}
``` |
|||
- Get - get an item by its name;
- Post - Insert an item with its name in url, price and corresponding store_id in body request. Example of body:
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




## Contact
Created by [Luís Costa](https://www.linkedin.com/in/lu%C3%ADs-costa-793a2414b/)

