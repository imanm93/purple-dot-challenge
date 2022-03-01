import axios from "axios"
import Axios from "axios"

type apiClientParams = {
    host: string
}

interface IApiClient {
    get: any
    put: any
    post: any
    delete: any
}

type Request = {
    ep: string
    data?: any
    params?: any
}

export function apiClient({ host }: apiClientParams): IApiClient {
    const client = Axios.create({
        baseURL: host,
        headers: { "Content-Type": "application/json" },
        timeout: 25 * 1000,
    })
    return {
        get: async ({ ep, params }: Request): Promise<any> => client.get(ep, { params: params }),
        put: async ({ ep, data }: Request): Promise<any> => axios({
            method: 'put',
            url: `${host}${ep}`,
            headers: {'Content-Type': 'application/json'},
            data : data
        }),
        post: async ({ ep, data }: Request): Promise<any> => axios({
            method: 'post',
            url: `${host}${ep}`,
            headers: {'Content-Type': 'application/json'},
            data : data
        }),
        delete: async ({ ep }: Request): Promise<any> => axios({
            method: 'delete',
            url: `${host}${ep}`,
            headers: {'Content-Type': 'application/json'},
        }),
    }
}
