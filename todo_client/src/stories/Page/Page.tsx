import React from "react"
import "./page.css"

interface PageProps {
    children: JSX.Element[]
}

export const Page: React.VFC<PageProps> = ({ children }: PageProps) => <div className="page">{children}</div>
