import React from "react"
import { Checkbox } from "../Checkbox/Checkbox"
import "./item.css"

interface ItemProps {
    id: string
    text: string
    status: string
    onSelect: (id: string) => void
    onDelete: (id: string) => void
}

export const Item = ({ id, text, status, onSelect, onDelete }: ItemProps) => (
    <div className={`todo-item todo-item-${status}`}>
        <div className="todo-item-checkbox-container">
            <Checkbox checked={status === "ACTIVE" ? false : true} onChange={(e: React.ChangeEvent) => onSelect(id)} />
        </div>
        {text}
        <button
            className="todo-item-btn"
            onClick={() => onDelete(id)}
        >
            🗑
        </button>
    </div>
)
