import { useEffect, useMemo, useState } from 'react'
import { AlertCircle, Loader2, Sparkles, Star } from 'lucide-react'
import ReactMarkdown from 'react-markdown'
import Layout from '../components/Layout'
import SectionPanel from '../components/SectionPanel'
import StatusCard from '../components/StatusCard'
import { analyzeBusiness, getHealth } from '../services/api'

const initialState = {
  executive_report: '',
  review_analysis: {},
  sales_analysis: {},
  inventory_analysis: {},
  marketing_plan: {},
  strategy: {},
  review_intelligence: {},
  sales_metrics: {},
  inventory_metrics: {},
}

export default function DashboardPage() {
  const [isLoading, setIsLoading] = useState(false)
  const [isHealthLoading, setIsHealthLoading] = useState(true)
  const [health, setHealth] = useState(null)
  const [error, setError] = useState('')
  const [result, setResult] = useState(initialState)
  const [businessName, setBusinessName] = useState('Sunrise Café')

  useEffect(() => {
    const loadHealth = async () => {
      try {
        const data = await getHealth()
        setHealth(data)
      } catch (err) {
        setError('Backend unavailable. Start the FastAPI server to enable analysis.')
      } finally {
        setIsHealthLoading(false)
      }
    }

    loadHealth()
  }, [])

  const handleAnalyze = async () => {
    setIsLoading(true)
    setError('')
    try {
      const data = await analyzeBusiness()
      setResult({ ...initialState, ...data })
    } catch (err) {
      const message = err?.response?.status
        ? `Request failed with status ${err.response.status}.`
        : 'Unable to reach backend. Please try again.'
      setError(message)
    } finally {
      setIsLoading(false)
    }
  }

  const formatIndianRupees = (value) => {
    if (value === null || value === undefined || value === '') return '—'
    if (typeof value === 'number') {
      return new Intl.NumberFormat('en-IN', {
        style: 'currency',
        currency: 'INR',
        maximumFractionDigits: 0,
      }).format(value)
    }

    return value
  }

  const renderListItems = (items = []) => {
    if (!Array.isArray(items) || items.length === 0) {
      return <p className="text-slate-400">No details available.</p>
    }

    const isObjectArray = items.some((item) => item && typeof item === 'object' && !Array.isArray(item))

    if (!isObjectArray) {
      return (
        <ul className="list-disc space-y-2 pl-5">
          {items.map((item, index) => (
            <li key={`${String(item)}-${index}`}>{item}</li>
          ))}
        </ul>
      )
    }

    return (
      <div className="space-y-3">
        {items.map((item, index) => {
          const fields = Object.entries(item || {}).filter(([, value]) => value !== undefined && value !== null && value !== '')

          if (fields.length === 0) {
            return null
          }

          return (
            <div key={`${item?.name || item?.strategy_name || item?.platform_focus || 'item'}-${index}`} className="rounded-xl border border-white/10 bg-slate-950/50 p-3">
              {fields.map(([field, value]) => {
                const label = field.replace(/_/g, ' ').replace(/\b\w/g, (char) => char.toUpperCase())

                if (typeof value === 'string' || typeof value === 'number') {
                  return (
                    <div key={`${field}-${index}`} className="mb-2 last:mb-0">
                      <p className="text-xs uppercase tracking-[0.2em] text-slate-500">{label}</p>
                      <p className="text-sm text-slate-200">{value}</p>
                    </div>
                  )
                }

                if (Array.isArray(value)) {
                  return (
                    <div key={`${field}-${index}`} className="mb-2 last:mb-0">
                      <p className="text-xs uppercase tracking-[0.2em] text-slate-500">{label}</p>
                      <div className="mt-1 space-y-1">
                        {value.map((entry, entryIndex) => (
                          <div key={`${field}-${entryIndex}`} className="rounded-lg bg-white/5 px-2 py-1 text-sm text-slate-200">
                            {typeof entry === 'string' ? entry : JSON.stringify(entry)}
                          </div>
                        ))}
                      </div>
                    </div>
                  )
                }

                return null
              })}
            </div>
          )
        })}
      </div>
    )
  }

  const metrics = useMemo(() => {
    const reviewSummary = result.review_intelligence?.average_rating ?? '—'
    const revenue = result.sales_metrics?.total_revenue ?? '—'
    const inventory = result.inventory_metrics?.stock_summary?.healthy ?? '—'

    return [
      {
        title: 'Average review rating',
        value: (
          <div className="flex items-center gap-2">
            <span>{reviewSummary}</span>
            <div className="flex items-center gap-1 text-amber-300">
              <span className="text-sm text-slate-300">/5</span>
              <Star className="h-4 w-4 fill-current" />
            </div>
          </div>
        ),
        subtitle: 'Customer sentiment pulse',
        accent: 'cyan',
      },
      {
        title: 'Total revenue',
        value: formatIndianRupees(revenue),
        subtitle: 'Sales intelligence snapshot',
        accent: 'emerald',
      },
      { title: 'Healthy stock items', value: inventory, subtitle: 'Inventory health', accent: 'violet' },
    ]
  }, [result])

  return (
    <Layout>
      <div className="space-y-6">
        <SectionPanel title="Executive Summary" description="A polished operating view for the demo business.">
          <div className="grid gap-4 lg:grid-cols-[1.4fr_0.8fr]">
            <div className="rounded-2xl border border-cyan-500/20 bg-gradient-to-br from-cyan-500/10 to-violet-500/10 p-5">
              <label className="mb-2 block text-sm font-medium text-slate-300" htmlFor="business-name">
                Business Name
              </label>
              <input
                id="business-name"
                value={businessName}
                onChange={(event) => setBusinessName(event.target.value)}
                disabled
                className="w-full rounded-xl border border-white/10 bg-slate-950/70 px-3 py-2 text-sm text-white outline-none ring-0 opacity-70"
                aria-label="Business Name"
              />
              <p className="mt-2 text-xs text-slate-400">Demo value only — the current backend workflow does not use this field.</p>
              <button
                onClick={handleAnalyze}
                disabled={isLoading || isHealthLoading}
                className="mt-4 inline-flex items-center gap-2 rounded-xl bg-cyan-500 px-4 py-2 font-semibold text-slate-950 transition hover:bg-cyan-400 disabled:cursor-not-allowed disabled:opacity-60"
              >
                {isLoading ? <Loader2 className="h-4 w-4 animate-spin" /> : <Sparkles className="h-4 w-4" />}
                Analyze Business
              </button>
              <div className="mt-3 text-sm text-slate-400">
                {isHealthLoading ? 'Checking backend connection…' : health ? `${health.project} • ${health.status}` : 'Backend unavailable'}
              </div>
            </div>

            <div className="space-y-3">
              {metrics.map((metric) => (
                <StatusCard key={metric.title} {...metric} />
              ))}
            </div>
          </div>
        </SectionPanel>

        {error ? (
          <div className="flex items-center gap-2 rounded-2xl border border-amber-500/30 bg-amber-500/10 p-4 text-sm text-amber-200">
            <AlertCircle className="h-4 w-4" />
            {error}
          </div>
        ) : null}

        <div className="grid gap-6 xl:grid-cols-2">
          <section id="review-section" className="scroll-mt-24">
            <SectionPanel title="Review" description="Customer sentiment and feedback themes.">
              <div className="space-y-3 text-sm text-slate-300">
                <p>{result.review_analysis?.summary || 'Waiting for analysis…'}</p>
                {renderListItems(result.review_analysis?.strengths || [])}
              </div>
            </SectionPanel>
          </section>

          <section id="sales-section" className="scroll-mt-24">
            <SectionPanel title="Sales" description="Revenue dynamics and sales opportunities.">
              <div className="space-y-3 text-sm text-slate-300">
                <p>{result.sales_analysis?.summary || 'Waiting for analysis…'}</p>
                {renderListItems(result.sales_analysis?.trends || [])}
              </div>
            </SectionPanel>
          </section>

          <section id="inventory-section" className="scroll-mt-24">
            <SectionPanel title="Inventory" description="Stock health and operational risks.">
              <div className="space-y-3 text-sm text-slate-300">
                <p>{result.inventory_analysis?.summary || 'Waiting for analysis…'}</p>
                {renderListItems(result.inventory_analysis?.weaknesses || [])}
              </div>
            </SectionPanel>
          </section>

          <section id="marketing-section" className="scroll-mt-24">
            <SectionPanel title="Marketing" description="Go-to-market recommendations and customer engagement.">
              <div className="space-y-4 text-sm text-slate-300">
                <div>
                  <p className="mb-2 font-medium text-cyan-200">Campaigns</p>
                  {renderListItems((result.marketing_plan?.campaigns || []).slice(0, 3))}
                </div>
                <div>
                  <p className="mb-2 font-medium text-cyan-200">Promotions</p>
                  {renderListItems((result.marketing_plan?.promotions || []).slice(0, 3))}
                </div>
                <div>
                  <p className="mb-2 font-medium text-cyan-200">Retention & social</p>
                  <div className="space-y-3">
                    {renderListItems((result.marketing_plan?.customer_retention || []).slice(0, 2))}
                    {renderListItems((result.marketing_plan?.social_media || []).slice(0, 2))}
                  </div>
                </div>
              </div>
            </SectionPanel>
          </section>
        </div>

        <section id="strategy-section" className="scroll-mt-24">
          <SectionPanel title="Strategy" description="Longer-term priorities and growth opportunities.">
            <div className="space-y-4 text-sm text-slate-300">
              <div>
                <p className="mb-2 font-medium text-cyan-200">Business goals</p>
                {renderListItems((result.strategy?.business_goals || []).slice(0, 3))}
              </div>
              <div>
                <p className="mb-2 font-medium text-cyan-200">Short-term actions</p>
                {renderListItems((result.strategy?.short_term_actions || []).slice(0, 3))}
              </div>
              <div>
                <p className="mb-2 font-medium text-cyan-200">Long-term priorities</p>
                {renderListItems((result.strategy?.long_term_actions || []).slice(0, 3))}
              </div>
            </div>
          </SectionPanel>
        </section>

        <SectionPanel title="Executive Report" description="Full narrative output from the backend workflow.">
          {result.executive_report ? (
            <div className="prose prose-invert max-w-none text-sm leading-7 text-slate-300">
              <ReactMarkdown
                components={{
                  h1: ({ ...props }) => <h1 className="mb-4 text-2xl font-semibold text-white" {...props} />,
                  h2: ({ ...props }) => <h2 className="mt-6 mb-3 text-xl font-semibold text-cyan-200" {...props} />,
                  h3: ({ ...props }) => <h3 className="mt-5 mb-2 text-lg font-semibold text-slate-100" {...props} />,
                  p: ({ ...props }) => <p className="mb-4 text-slate-300" {...props} />,
                  ul: ({ ...props }) => <ul className="mb-4 list-disc space-y-2 pl-6 text-slate-300" {...props} />,
                  ol: ({ ...props }) => <ol className="mb-4 list-decimal space-y-2 pl-6 text-slate-300" {...props} />,
                  li: ({ ...props }) => <li className="leading-7" {...props} />,
                  strong: ({ ...props }) => <strong className="font-semibold text-white" {...props} />,
                  hr: ({ ...props }) => <hr className="my-6 border-white/10" {...props} />,
                }}
              >
                {result.executive_report}
              </ReactMarkdown>
            </div>
          ) : (
            <div className="text-sm leading-7 text-slate-300">
              The workflow report will appear here once the backend completes its analysis.
            </div>
          )}
        </SectionPanel>
      </div>
    </Layout>
  )
}
