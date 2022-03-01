import React from "react"
import { Button } from "../../../stories/Button/Button"
import phrases from "../en-GB/phrases.json"

type TodoSaveBtnProps = {
    onSave?: () => void
}

export const TodoSaveBtn: React.FC<TodoSaveBtnProps> = ({ onSave }: TodoSaveBtnProps) => {
    const label = phrases.btnSave
    return <Button kind="secondary" size="medium" label={label} onClick={onSave} />
}
