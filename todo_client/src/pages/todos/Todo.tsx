import React, { useCallback, useEffect, useState } from "react"
import { Page } from "../../stories/Page/Page"
import { Header } from "../../stories/Header/Header"
import { TodoListContainer } from "./components/TodoListContainer"
import { TodoClearBtn } from "./components/TodoClearBtn"
import { TodoForm } from "./components/TodoForm"
import { List, Task, TasksDict, TaskStatus } from "../../types/Types"
import { todoApi } from "../../services/todoApi"
import { v4 } from "uuid"
import phrases from "./en-GB/phrases.json"
import "./styles.css"

const getFilteredTasks = (status: TaskStatus, tasks: Task[]): TasksDict =>
    tasks
        .filter((task) => task.status === status)
        .reduce(
            (prevTask, task) => ({
                ...{ [task.id]: { ...task } },
                ...prevTask,
            }),
            {}
        )

export const ToDo: React.FC<{}> = () => {
    const api = todoApi()
    const [tasks, setTasks] = useState<Task[]>([])

    const [activeList, setActiveList] = useState<List>({
        id: "active_list",
        name: "Active",
        tasks: getFilteredTasks("ACTIVE", tasks),
    })
    const [completedList, setCompletedList] = useState<List>({
        id: "completed_list",
        name: "Completed",
        tasks: getFilteredTasks("COMPLETED", tasks),
    })

    const fetchTasks = useCallback(() => {
        api
            .retrieveTasks()
            .then(resp => {
                let tasks = resp.data
                setTasks(tasks)
                setActiveList({ ...activeList, ...{ tasks: getFilteredTasks("ACTIVE", tasks) } })
                setCompletedList({ ...completedList, ...{ tasks: getFilteredTasks("COMPLETED", tasks) } })
            })
            .catch(err => { throw new Error(err) })
    }, [])

    useEffect(() => {
        fetchTasks()
    }, [fetchTasks])

    const _handlePromise = (promise: Promise<any>): void => {
        promise
            .then(() => fetchTasks())
            .catch(err => { throw new Error(err) })
    }

    const onTaskUpdate = (id: string, status: string) => {
        console.log("onTaskUpdate", id, status)
        const currentTask = tasks.filter((task) => task.id === id)[0]
        const newStatus: TaskStatus = status === "ACTIVE" ? "COMPLETED" : "ACTIVE"
        const updatedTask: Task = Object.assign({}, { ...currentTask, ...{ status: newStatus } })
        _handlePromise(api.updateTask(updatedTask))
    }

    const onTaskAdd = ({ text }: { [text: string]: string }) => {
        console.log("onTaskAdd", text)
        const newTask: Task = {
            id: v4(),
            text: text,
            status: "ACTIVE",
            created_at: new Date().toISOString(),
            updated_at: new Date().toISOString(),
        }
        _handlePromise(api.addTask(newTask))
    }

    const onTaskDelete = (id: string) => {
        console.log("onTaskDelete", id)
        _handlePromise(api.deleteTask(id))
    }

    const onTaskClear = () => {
        console.log("onTaskClear")
        _handlePromise(api.clearTasks())
    }

    return (
        <Page>
            <Header title={phrases.title} subtitle={phrases.subtitle} />
            <div className="todo-page-container">
                <div className="todo-lists-container">
                    <TodoListContainer
                        key="1"
                        data-testid="active-tasks-list"
                        list={activeList}
                        onTaskSelect={onTaskUpdate}
                        onTaskDelete={onTaskDelete}
                    />
                    <TodoListContainer
                        key="2"
                        data-testid="completed-tasks-list"
                        list={completedList}
                        onTaskSelect={onTaskUpdate}
                        onTaskDelete={onTaskDelete}
                    />
                </div>
                <div>
                    <TodoForm onAdd={onTaskAdd} />
                    <div className="todo-page-controls">
                        <TodoClearBtn onClear={() => onTaskClear()} />
                    </div>
                </div>
            </div>
        </Page>
    )
}
