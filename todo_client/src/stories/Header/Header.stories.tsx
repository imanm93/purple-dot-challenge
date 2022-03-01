import React from "react"
import { ComponentStory, ComponentMeta } from "@storybook/react"

import { Header } from "./Header"

export default {
    title: "Example/Header",
    component: Header,
    parameters: {
        layout: "fullscreen",
    },
} as ComponentMeta<typeof Header>

const Template: ComponentStory<typeof Header> = (args) => <Header {...args} />

export const RegularHeader = Template.bind({})
RegularHeader.args = {
    title: "Title",
    subtitle: "Subtitle",
}
