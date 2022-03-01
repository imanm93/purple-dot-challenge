export type TaskStatus = "ACTIVE" | "COMPLETED"
export type TasksDict = { [id: string]: Task }

export type Task = {
    id: string
    text: string
    status: TaskStatus
    created_at: string
    updated_at: string
}

export type List = {
    id: string
    name: string
    tasks: TasksDict
}
