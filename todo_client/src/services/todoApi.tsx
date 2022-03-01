import { apiClient } from "../api"
import { Task } from "../types/Types"

export interface ITodoApi {
    clearTasks: () => Promise<any>
    retrieveTasks: () => Promise<any>
    addTask: (task: Task) => Promise<any>
    updateTask: (task: Task) => Promise<any>
    retrieveTask: (id: string) => Promise<any>
    deleteTask: (id: string) => Promise<any>
}

export function todoApi(): ITodoApi {
    console.log("init todoApi")
    const api = apiClient({
        host: process.env.TODO_API_URL ? process.env.TODO_API_URL : "http://localhost:8000/v1",
    })
    return {
        retrieveTasks: async () => await api.get({ ep: "/" }),
        retrieveTask: async (id: string) => await api.get({ ep: `/filter/${id}` }),
        addTask: async (task: Task) => await api.post({ ep: "/create", data: task }),
        updateTask: async (task: Task) => await api.put({ ep: `/${task.id}`, data: task }),
        deleteTask: async (id: string) => await api.delete({ ep: `/${id}` }),
        clearTasks: async () => await api.delete({ ep: "/clear" }),
    }
}
