import React from "react"
import "./header.css"

interface HeaderProps {
    title: string
    subtitle: string
}

export const Header = ({ title, subtitle }: HeaderProps) => (
    <header>
        <div className="wrapper">
            <div>
                <h1>{title}</h1>
                <h2>{subtitle}</h2>
            </div>
        </div>
    </header>
)
