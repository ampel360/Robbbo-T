import { create } from 'zustand'
import axios from 'axios'

type NodeInfo = {
  id: string
  name: string
  status: string
  lastPing: string
}

type UserMetric = {
  total: number
  active: number
  suspended: number
}

type AgentActivity = {
  id: string
  name: string
  role: string
  lastAction: string
}

type DashboardState = {
  loading: boolean
  nodes: NodeInfo[]
  users: UserMetric | null
  agents: AgentActivity[]
  fetchDashboard: () => void
}

export const useDashboardStore = create<DashboardState>((set) => ({
  loading: true,
  nodes: [],
  users: null,
  agents: [],
  fetchDashboard: async () => {
    set({ loading: true })
    try {
      const [nodesRes, usersRes, agentsRes] = await Promise.all([
        axios.get('/api/nodes'),
        axios.get('/api/users/metrics'),
        axios.get('/api/agents/activity')
      ])

      set({
        nodes: nodesRes.data,
        users: usersRes.data,
        agents: agentsRes.data,
        loading: false
      })
    } catch (err) {
      console.error('Dashboard fetch error:', err)
      set({ loading: false })
    }
  }
}))
