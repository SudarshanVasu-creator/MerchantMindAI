import { Routes, Route, Navigate } from 'react-router-dom'
import DashboardPage from './pages/DashboardPage'

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<DashboardPage />} />
      <Route path="/review" element={<DashboardPage />} />
      <Route path="/sales" element={<DashboardPage />} />
      <Route path="/inventory" element={<DashboardPage />} />
      <Route path="/marketing" element={<DashboardPage />} />
      <Route path="/strategy" element={<DashboardPage />} />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
