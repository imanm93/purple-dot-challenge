## 🧑‍🎨 Frontend Design

We have used the concept of smart and dumb components to design our client.

- **Dumb components** are responsible for only visual representation of our data and passing back any interactions from the user. It does not care where or what is done to the data it displays.

We have also used storybook to allow non-tech teammates (designer or product ) to easily view and interact with the different states of the foundational UI components. Buttons, Filters, List, Items and so on.

- **Smart components** represent components that manipulate state / interact with data.

We want these components to represent concepts such as Tasks and Lists.

Other than the above smart and dump components we have a generic api client (using axios) which we use to interact with our backend through an intermediate `todoAPI` interface.

#### How to run storybook?

1. run `docker-compose up`
2. open your browser to `http://localhost:6006`

#### How to run client?

1. run `docker-compose up`
2. open your browser to `http://localhost:3000`
