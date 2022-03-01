import React from "react"
import "./list.css"

export interface ListProps {
    items: JSX.Element[]
    emptyListDisplayText: string
    className?: string
}

export const List = ({ items, emptyListDisplayText, className }: ListProps) => (
    <div className={`todo-list-container ${className ? className : ""}`}>
        <div className="todo-list">
            <div className="todo-list__container">
                {items.length > 0
                    ? items.map((item) => <div className="todo-list-item">{item}</div>)
                    : emptyListDisplayText
                }
            </div>
        </div>
    </div>
)
