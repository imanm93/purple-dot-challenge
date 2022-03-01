import React from "react"
import { Button } from "../../../stories/Button/Button"
import phrases from "../en-GB/phrases.json"

type TodoAddBtnProps = {
    onAdd?: () => void
}

export const TodoAddBtn: React.FC<TodoAddBtnProps> = ({ onAdd }: TodoAddBtnProps) => {
    const label = phrases.btnSubmit
    return <Button kind="primary" size="medium" label={label} onClick={onAdd} />
}
