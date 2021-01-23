# VGSI Engineering Coding Exercise: House API

## Tyler's README.md inside the README.md
### How to build and run the solution
Pre-req:

* Python3

You can run this solution by installing the requirements from the `requirements.txt` in the root of the project. Example: `pip install -r /path/to/project/requirements.txt`. Once you have successfully installed the requirements you can run the project by typing, while in the root of the project, `python app.py`.

### Notes about any improvements you'd like to make but did not have time to make
I would like to have created a data access template so that I could have more simply switched between the "in-memory db" and a production db. A good POC would have been to add an optional SQLite3 datebase option with data persistence (outside of required scope). I also could have integrated the Postman tests and unittests so that they would run automagically via something like Github Actions.
### Notes on any API design choices
I tried to keep the project as simple as I possibly could. Using only basic components of the flask library and some basic validation. The PUT endpoint was implemented to also add new data to the database (if the specified house id was not found in the database). This wasn't explicitly outlined in the document but is expected of a PUT request if there isn't a matching existing data point.
### Notes on the security implications of the implementation
Anyone with cURL installed on their phone can completely nuke the entire dataset with little trouble. There isn't a ton of data validation other than:
1) Does the request have all the fields.
2) Are they all semi-appropriate datatypes.

So in theory you could just fill every data point with garbage erasing any valuable data.

Could be fixed with some simple authorization and better validation to make sure that the fields are really valid.

## Overview

The goal of this coding exercise will be to build a small application to serve housing data from a 
REST API. You'll need to start from scratch. The only items that will be provided are this README
file and a data file which will contain housing data. You may use any framework and libraries that
are needed. This may include ASP.NET, Spring Framework, Spring Boot, Gorilla Mux, and any others
(depending on the language that you are using).

## Completion and Expectations

This exercise is meant to provide insight into how you write code for production use. It is also
mean to check your knowledge of HTTP, REST, and API design from an implementation perspective. 
The API is simple, it's not meant to be complicated. However, it does provide a good sample for
demonstrating your ability to write good code, as well as your understanding of API implementations.

While implementing this solution, think about implementing this as part of a large product and
larger team. You'll need to consider aspects such as:

* Code Quality - Following common code quality principles
* Testability - How easily can this code be tested in both isolation as well as part of a larger test suite
* Maintainability - How easy will it be to change this code in the future
* Collaboration - How easy will it be for others to take the code and update it or maintain it
* Unit Test Coverage - Are there sufficient unit tests to cover the implementation and ensure bugs don't appear in the code base
* Performance - As this code is added to a larger project and used at scale, will the implementation still perform well

There are also specific aspects in HTTP and REST to consider:

* Error Handling - Which error conditions should be handled
* Error Responses - How should errors be communicated back as HTTP Responses
* HTTP Protocol - Which aspects of the HTTP protocol should be used in the API implementation
* Model - How should the API and its representation be modelled in your solution
* Stability and Versioning - Can the API be kept stable, under which circumstances would you need to make a new version

**Please keep in mind that the goal of the implementation isn't to produce the right answer (that should be simple, this is
not a complicated API), but to demonstrate your ability to write quality, testable code as part of a team.**

## Delivery

Your solution should include:

* README.md
* Implementation
* Tests
* Any necessary scripts for building, running, or deploying

In particular, the README.md file should document:

* How to build and run the solution
* Notes about any improvements you'd like to make but did not have time to make
* Notes on any API design choices
* Notes on the security implications of the implementation

## Housing Data File

The data file included here is in CVS format. The data file include a header line to describe what
each field in the data file is. The file should be read as part of your solution and it's contents
should be used as the data source for the API.

## API

The solution should have three API endpoints. The definition of the API will be described here.

### House List Resource

URL: http://<host[:port]>/api/houses
HTTP Request: GET

### Request Headers

Accepts: application/json

### Request Body

<none>

### Response Headers

Content-Type: application/json

### Response Body

```json
{
    "itemCount": 2,
    "items":
    [
        {
            "firstName": "Jack",
            "lastName": "Smith",
            "street": "Broad St",
            "city": "Hudson",
            "state": "MA",
            "zip": "01749",
            "propertyType": "Single Family",
            "location":"http://<host[:port]>/api/houses/{id}"
        },
        {
            "firstName": "Fred",
            "lastName": "Mack",
            "street": "South St",
            "city": "Husdon",
            "state": "MA",
            "zip": "01749",
            "propertyType": "Multi Family",
            "location":"http://<host[:port]>/api/houses/{id}"
        }
    ]
}
```

### Get Single House Resource

URL: http://<host[:port]>/api/houses/{id}
HTTP Request: GET

### Request Headers

Accepts: application/json

### Request Body

<none>

### Response Headers

Content-Type: application/json

### Response Body

```json
{
    "firstName": "Jack",
    "lastName": "Smith",
    "street": "Broad St",
    "city": "Hudson",
    "state": "MA",
    "zip": "01749",
    "propertyType": "Single Family",
    "location":"http://<host[:port]>/api/houses/{id}"
}
```

### Update Single House Resource

URL: http://<host[:port]>/api/houses/{id}
HTTP Request: PUT

### Request Headers

Accepts: application/json

### Request Body

```json
{
    "firstName": "John",
    "lastName": "Smith",
    "street": "Broad St",
    "city": "Hudson",
    "state": "MA",
    "zip": "01749",
    "propertyType": "Single Family",
    "location":"http://<host[:port]>/api/houses/{id}"
}
```

### Response Headers

Content-Type: application/json

### Response Body

```json
{
    "firstName": "John",
    "lastName": "Smith",
    "street": "Broad St",
    "city": "Hudson",
    "state": "MA",
    "zip": "01749",
    "propertyType": "Single Family",
    "location":"http://<host[:port]>/api/houses/{id}"
}
```

## Notes on API Design

There is one thing here that I'll clarify. This API is based on hypermedia design principles.
The one implication that has here for the design is that instead of having IDs in the responses
and having clients need to determine which URL to be called, a `location` is provided instead.
The `location` attribute should be consider metadata and should not be considered useful for
the PUT request and also should not be updatable by the PUT request.

The format of `{id}` is up to the implementation. The API definition makes no assertions
about it and it should be opaque to clients of this API.


## Notes on Storage

This project doesn't need to implement storage. Once the data file is read into memory, any subsequent
updates do not need to be persisted, they can be stored in memory and lost upon a server restart.