import { Item } from "../../../stories/Item/Item"

interface TodoTaskProps {
    id: string
    text: string
    status: string
    onSelect: (id: string) => void
    onDelete: (id: string) => void
}

export const TodoTask = ({ id, text, status, onSelect, onDelete }: TodoTaskProps) => (
    <>
        <Item
            id={id}
            text={text}
            status={status}
            onSelect={() => onSelect(id)}
            onDelete={onDelete}
        />
    </>
)
