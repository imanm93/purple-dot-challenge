import React from "react"
import { ComponentStory, ComponentMeta } from "@storybook/react"

import { Checkbox } from "./Checkbox"

export default {
    title: "Example/Checkbox",
    component: Checkbox,
    parameters: {
        // More on Story layout: https://storybook.js.org/docs/react/configure/story-layout
        layout: "fullscreen",
    },
} as ComponentMeta<typeof Checkbox>

const Template: ComponentStory<typeof Checkbox> = (args) => <Checkbox {...args} />

export const Checked = Template.bind({})
Checked.args = {
    checked: true,
}

export const UnChecked = Template.bind({})
UnChecked.args = {
    checked: false,
}
