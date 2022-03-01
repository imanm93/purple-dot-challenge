import React from "react"
import { Card } from "../../../stories/Card/Card"
import { TodoList } from "./TodoList"
import { TodoTask } from "./TodoTask"
import { List, TaskStatus } from "../../../types/Types"
import phrases from "../en-GB/phrases.json"

interface TodoListContainerProps {
    list: List
    onTaskSelect: (id: string, status: TaskStatus) => void
    onTaskDelete: (id: string) => void
}

export const TodoListContainer: React.FC<TodoListContainerProps> = ({
    list,
    onTaskSelect,
    onTaskDelete,
}: TodoListContainerProps) => (
    <div>
        <Card title={list.name} />
        <TodoList
            id={list.id}
            emptyListDisplayText={phrases.emptyListDisplayText}
            tasks={Object.keys(list.tasks).map((id) => (
                <TodoTask
                    key={id}
                    id={list.tasks[id].id}
                    text={list.tasks[id].text}
                    status={list.tasks[id].status}
                    onSelect={() => onTaskSelect(list.tasks[id].id, list.tasks[id].status)}
                    onDelete={() => onTaskDelete(id)}
                />
            ))}
        />
    </div>
)
