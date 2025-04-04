---

### (Zustand Store opcional) 🧠 

```ts
import { create } from 'zustand'
import axios from 'axios'

type NodeInfo = {
  name: string
  status: string
}

type DashboardState = {
  nodes: NodeInfo[]
  loading: boolean
  fetchNodes: () => void
}

export const useDashboardStore = create<DashboardState>((set) => ({
  nodes: [],
  loading: true,
  fetchNodes: async () => {
    set({ loading: true })
    try {
      const res = await axios.get('/api/nodes') // o endpoint federado
      set({ nodes: res.data, loading: false })
    } catch (err) {
      console.error('Error al cargar nodos', err)
      set({ loading: false })
    }
  },
}))
