import React from "react"
import { ComponentStory, ComponentMeta } from "@storybook/react"

import { Card } from "./Card"

export default {
    title: "Example/Card",
    component: Card,
    parameters: {
        layout: "fullscreen",
    },
} as ComponentMeta<typeof Card>

const Template: ComponentStory<typeof Card> = (args) => <Card {...args} />

export const RegularCard = Template.bind({})
RegularCard.args = {
    title: "Name",
}
