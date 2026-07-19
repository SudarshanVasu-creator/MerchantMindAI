export default function StatusCard({ title, value, subtitle, accent = 'cyan' }) {
  const accentClasses = {
    cyan: 'border-cyan-500/20 bg-cyan-500/10 text-cyan-200',
    emerald: 'border-emerald-500/20 bg-emerald-500/10 text-emerald-200',
    violet: 'border-violet-500/20 bg-violet-500/10 text-violet-200',
    amber: 'border-amber-500/20 bg-amber-500/10 text-amber-200',
  }

  return (
    <div className={`rounded-2xl border p-4 ${accentClasses[accent]}`}>
      <p className="text-sm font-medium">{title}</p>
      <div className="mt-2 text-2xl font-semibold">{value}</div>
      {subtitle ? <p className="mt-1 text-sm opacity-80">{subtitle}</p> : null}
    </div>
  )
}
