# python-web-api-bottle-basic-auth-neo4j-simple

## Description
Creates an api of `dog` with relationships
to `breed` and `color` in default namespace `neo4j`.
Has the ability to query by parameters.

Requires basic authentication.
| username | password |
| -------- | -------- |
| *user* | *pass* |

Remotely tested with *testify*.

## Tech stack
- python
  - bottle
  - neo4j
  - testify
  - requests

## Docker stack
- python:latest
- neo4j:latest

## To run
`sudo ./install.sh -u`
- [Web ui for neo4j](http://localhost:7474)
| username | password |
| -------- | -------- |
| *neo4j* | *secret* |
- Get all dogs: http://localhost/dogs
  - Schema name, breed, and color
- Query with params: 
  - http://localhost/dogs/name/<name>
  - http://localhost/dogs/breed/<breed>
  - http://localhost/dogs/color/<color>

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`
