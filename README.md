# 🟣

[![Python 3.8+](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![license](https://img.shields.io/badge/license-Apache-blue.svg)](https://img.shields.io/badge/license-Apache-blue)

source code for the 🟣 take home challenge

## App Setup

### Requirements

- docker
- docker-compose
- make

Please see installations instructions [here](../purple-dot-challenge/docs/setup.md).

Now, run `make start-init` - that's all, enjoy the app! 😎

## Table of Contents  

[1.0 Backend Design](./docs/api.md)  
[1.1 Frontend Design](./docs/client.md)

## Tests

The project was primary covered using unit tests. Though I have briefly used Cypress in the past, I would have taken up too much refreshing my memory and upskilling for this take home assignment to include integration tests.

run `make test` for all tests

## Next Steps

Some ideas around where we can take this app next. 

*this is by no means an exhaustive list of ideas (there never can be!)*

- **E2E Tests:** Add Cypress e2e tests to test user interactions from the browser and back. In general, keep adding better test coverage.

- **Pagination:** As the application scales it will become unrealistic to retrieve lists with more than hundreds of thousands or millions of tasks. Thus, pagination is one of the mechanisms through which we can minimize this load. It can be done by index or time at which a task is created.

- **Tasks w/ images, descriptions:** Atm tasks consists of only text. This is not great from an UX perspective where users may want to add links or images.

- **Multiple Lists:** A user may want to group certain tasks into one list and others into another list. Therefore, we can support for multiple lists. We can do this by adding a new set of endpoints which are the equivalent CRUD ops for tasks at the list level.
