import { List } from "../../../stories/List/List"

interface TodoListProps {
    id: string
    emptyListDisplayText: string
    tasks: JSX.Element[]
}

export const TodoList = ({ tasks, emptyListDisplayText }: TodoListProps) => (
    <List items={tasks} emptyListDisplayText={emptyListDisplayText} />
)
