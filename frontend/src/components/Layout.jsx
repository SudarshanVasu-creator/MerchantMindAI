import { Activity, BarChart3, Boxes, MessageSquareQuote, ShoppingCart, Sparkles, Target } from 'lucide-react'

const sections = [
  { name: 'Executive Summary', id: 'executive-summary', icon: Sparkles },
  { name: 'Review', id: 'review-section', icon: MessageSquareQuote },
  { name: 'Sales', id: 'sales-section', icon: ShoppingCart },
  { name: 'Inventory', id: 'inventory-section', icon: Boxes },
  { name: 'Marketing', id: 'marketing-section', icon: BarChart3 },
  { name: 'Strategy', id: 'strategy-section', icon: Target },
]

export default function Layout({ children }) {
  const handleSectionClick = (sectionId) => {
    const element = document.getElementById(sectionId)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }

  return (
    <div className="min-h-screen bg-transparent text-slate-100">
      <header className="border-b border-white/10 bg-slate-950/70 backdrop-blur">
        <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-5 sm:px-6 lg:px-8">
          <div>
            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-cyan-300">MerchantMind AI</p>
            <h1 className="text-xl font-semibold text-white">Business Intelligence Dashboard</h1>
          </div>
          <div className="rounded-full border border-cyan-500/30 bg-cyan-500/10 px-4 py-2 text-sm text-cyan-200">
            <span className="mr-2 inline-flex h-2.5 w-2.5 rounded-full bg-emerald-400" />
            Live workflow insights
          </div>
        </div>
      </header>

      <div className="mx-auto flex max-w-7xl flex-col gap-6 px-4 py-6 sm:px-6 lg:flex-row lg:px-8">
        <aside className="w-full rounded-2xl border border-white/10 bg-slate-900/70 p-4 shadow-2xl shadow-black/30 lg:w-72">
          <div className="mb-6 rounded-2xl border border-cyan-500/20 bg-gradient-to-br from-cyan-500/10 to-violet-500/10 p-4">
            <div className="flex items-center gap-3">
              <div className="rounded-xl bg-cyan-500/20 p-2">
                <Activity className="h-5 w-5 text-cyan-300" />
              </div>
              <div>
                <p className="text-sm font-semibold text-white">Sunrise Café</p>
                <p className="text-sm text-slate-400">Demo business</p>
              </div>
            </div>
          </div>

          <nav className="space-y-2">
            {sections.map(({ name, id, icon: Icon }) => (
              <button
                key={id}
                type="button"
                onClick={() => handleSectionClick(id)}
                className="flex w-full items-center gap-3 rounded-xl px-3 py-3 text-sm text-slate-300 transition hover:bg-white/5 hover:text-white"
              >
                <Icon className="h-4 w-4" />
                {name}
              </button>
            ))}
          </nav>
        </aside>

        <main className="flex-1">{children}</main>
      </div>
    </div>
  )
}
