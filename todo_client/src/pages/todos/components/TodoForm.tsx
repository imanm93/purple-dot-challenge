import React, { useState } from "react"
import { Card } from "../../../stories/Card/Card"
import phrases from '../en-GB/phrases.json'

interface TodoFormProps {
    onAdd: ({ text }: { [text: string]: string }) => void
}

export const TodoForm = ({ onAdd }: TodoFormProps) => {
    const [text, setText] = useState("");

    let handleSubmit = (e: React.SyntheticEvent) => {
        e.preventDefault();
        const target = e.target as typeof e.target & {
            text: { value: string }
        }
        const taskText = target.text.value
        setText("")
        onAdd({ text: taskText })
    };

    return (
        <Card>
            <form
                onSubmit={handleSubmit}>
                <label>
                    Task
                    <input
                        type="text"
                        name="text"
                        placeholder={phrases.formTextPlaceholder}
                        value={text}
                        onChange={(e: any) => setText(e.target.value)}
                    />
                </label>
                <button
                    className="todo-button todo-button--primary"
                    style={{ margin: "5px 0px" }}
                    type="submit"
                >
                    Add Task
                </button>
            </form>
        </Card>
    )
}
