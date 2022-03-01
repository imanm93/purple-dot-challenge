import React from "react"
import { Button } from "../../../stories/Button/Button"

type TodoFilterBtnProps = {
    onFilter: (status: string) => void
}

export const TodoFilterBtn: React.FC<TodoFilterBtnProps> = ({ onFilter }: TodoFilterBtnProps) => {
    return (
        <>
            <Button kind="filter" size="small" label="Active" onClick={() => onFilter("ACTIVE")} />
            <Button kind="filter" size="small" label="Completed" onClick={() => onFilter("COMPLETED")} />
        </>
    )
}
