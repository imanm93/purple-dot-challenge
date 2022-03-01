import React from "react"
import { ComponentStory, ComponentMeta } from "@storybook/react"

import { Item } from "./Item"

export default {
    title: "Example/Item",
    component: Item,
    parameters: {
        layout: "fullscreen",
    },
} as ComponentMeta<typeof Item>

const Template: ComponentStory<typeof Item> = (args) => <Item {...args} />

export const ActiveItem = Template.bind({})
ActiveItem.args = {
    status: "ACTIVE",
    text: "active task",
}

export const CompletedItem = Template.bind({})
CompletedItem.args = {
    status: "COMPLETED",
    text: "completed task",
}
