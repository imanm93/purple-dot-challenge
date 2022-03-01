import React from "react"
import { ComponentStory, ComponentMeta } from "@storybook/react"

import { Button } from "./Button"

export default {
    title: "Example/Button",
    component: Button,
    argTypes: {
        backgroundColor: { control: "color" },
    },
} as ComponentMeta<typeof Button>

const Template: ComponentStory<typeof Button> = (args) => <Button {...args} />

export const Primary = Template.bind({})
Primary.args = {
    kind: "primary",
    label: "Add",
}

export const Secondary = Template.bind({})
Secondary.args = {
    kind: "secondary",
    label: "Save",
}

export const Tertiary = Template.bind({})
Tertiary.args = {
    kind: "tertiary",
    label: "Delete",
}

export const Large = Template.bind({})
Large.args = {
    size: "large",
    label: "Button",
}

export const Medium = Template.bind({})
Medium.args = {
    size: "medium",
    label: "Button",
}

export const Small = Template.bind({})
Small.args = {
    size: "small",
    label: "Button",
}
