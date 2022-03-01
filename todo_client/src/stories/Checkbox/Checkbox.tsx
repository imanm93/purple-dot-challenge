import React from "react"
import "./checkbox.css"

interface CheckboxProps {
    checked: boolean
    onChange?: (e: React.ChangeEvent) => void
}

export const Checkbox = ({ checked, onChange }: CheckboxProps) => (
    <label>
        <input type="checkbox" onChange={onChange} />
        <svg
            className={`checkbox ${checked ? "checkbox--active" : ""}`}
            // This element is purely decorative so
            // we hide it for screen readers
            aria-hidden="true"
            viewBox="0 0 15 11"
            fill="none">
            <path d="M1 4.5L5 9L14 1" strokeWidth="2" stroke={checked ? "#fff" : "none"} />
        </svg>
    </label>
)
