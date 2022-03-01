import React from "react"
import { Button } from "../../../stories/Button/Button"
import phrases from "../en-GB/phrases.json"

type TodoClearBtnProps = {
    onClear?: () => void
}

export const TodoClearBtn: React.FC<TodoClearBtnProps> = ({ onClear }: TodoClearBtnProps) => {
    const label = phrases.btnClear
    return <Button kind="tertiary" size="medium" label={label} onClick={onClear} />
}
