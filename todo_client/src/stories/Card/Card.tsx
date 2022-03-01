import React from "react"
import "./card.css"

export interface CardProps {
    title?: string
    children?: JSX.Element
}

export const Card = ({ title, children }: CardProps) => (
    <div className="todo-card-container">
        <div className="todo-card">
            <div className="todo-card__container">
                <h1 className="todo-card__header">{title ? title : ""}</h1>
                {children}
            </div>
        </div>
    </div>
)
