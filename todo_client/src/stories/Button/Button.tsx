import React from "react"
import "./button.css"

type ButtonKind = "primary" | "secondary" | "tertiary" | "danger" | "filter"

interface ButtonProps {
    label?: string
    kind?: ButtonKind
    className?: string
    backgroundColor?: string
    size?: "small" | "medium" | "large"
    /**
     * Optional click handler
     */
    onClick?: () => void
}

/**
 * Button UI component
 */
export const Button = ({
    kind = "primary",
    size = "medium",
    backgroundColor,
    className,
    label,
    ...props
}: ButtonProps) => {
    const mode = kind ? `todo-button--${kind}` : `todo-button`
    return (
        <button
            type="button"
            className={["todo-button", `todo-button--${size}`, className, mode].join(" ")}
            style={{ backgroundColor }}
            {...props}
        >
            {label}
        </button>
    )
}
