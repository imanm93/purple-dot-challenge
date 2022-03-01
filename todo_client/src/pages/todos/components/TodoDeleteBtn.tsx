import React from "react"
import { Button } from "../../../stories/Button/Button"
import phrases from "../en-GB/phrases.json"

type TodoDeleteBtnProps = {
    onDelete?: () => void
}

export const TodoDeleteBtn: React.FC<TodoDeleteBtnProps> = ({ onDelete }: TodoDeleteBtnProps) => {
    const label = phrases.btnDelete
    return <Button kind="danger" size="medium" label={label} onClick={onDelete} />
}
