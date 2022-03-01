import React from "react"
import { ComponentStory, ComponentMeta } from "@storybook/react"

import { List } from "./List"
import { Item } from "../Item/Item"

export default {
    title: "Example/List",
    component: List,
    parameters: {
        layout: "fullscreen",
    },
} as ComponentMeta<typeof List>

const Template: ComponentStory<typeof List> = (args) => <List {...args} />

export const ItemList = Template.bind({})
ItemList.args = {
    items: [
        Item({ id: "one", text: "Item One", status: "ACTIVE", onSelect: () => {}, onDelete: () => {} }),
        Item({ id: "two", text: "Item Two", status: "COMPLETED", onSelect: () => {}, onDelete: () => {} }),
    ],
}
