'use client'

import { useState, useEffect } from 'react'
import { MK_TOWNS, getSchools, SCHOOL_OTHER } from '@/lib/schools'

const selectStyle = {
  width: '100%', padding: '12px 16px', borderRadius: '1rem',
  border: '2px solid #E5E7EB', background: '#FAFAFA',
  color: '#1A1A2E', fontWeight: 600, fontSize: '1rem',
  outline: 'none', appearance: 'none' as const,
  backgroundImage: `url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%236B6B8A' stroke-width='2' fill='none' stroke-linecap='round'/%3E%3C/svg%3E")`,
  backgroundRepeat: 'no-repeat' as const,
  backgroundPosition: 'right 14px center',
}

interface Props {
  town: string
  school: string
  onTownChange: (t: string) => void
  onSchoolChange: (s: string) => void
}

export default function TownSchoolPicker({ town, school, onTownChange, onSchoolChange }: Props) {
  const schools = town ? getSchools(town) : []

  // A school value is "custom" if it's non-empty and not one of the dropdown options
  const isCustom = school !== '' && school !== SCHOOL_OTHER && !schools.includes(school)
  const [showCustom, setShowCustom] = useState(isCustom)
  const [customVal, setCustomVal] = useState(isCustom ? school : '')

  // Reset when town changes
  useEffect(() => {
    setShowCustom(false)
    setCustomVal('')
  }, [town])

  const handleSchoolSelect = (val: string) => {
    if (val === SCHOOL_OTHER) {
      setShowCustom(true)
      setCustomVal('')
      onSchoolChange('')
    } else {
      setShowCustom(false)
      setCustomVal('')
      onSchoolChange(val)
    }
  }

  const handleCustomInput = (val: string) => {
    setCustomVal(val)
    onSchoolChange(val)
  }

  return (
    <div className="space-y-3">
      <div className="flex items-center gap-2">
        <div className="flex-1 h-px" style={{ background: '#E5E7EB' }} />
        <span className="text-xs font-black px-2 py-1 rounded-full"
          style={{ background: '#FFF8E1', color: '#B8860B' }}>
          🏆 Препорачано за натпревари
        </span>
        <div className="flex-1 h-px" style={{ background: '#E5E7EB' }} />
      </div>

      {/* Town */}
      <div>
        <label className="block text-xs font-black mb-1 tracking-widest" style={{ color: '#6B6B8A' }}>
          ГРАД / ОПШТИНА{' '}
          <span className="font-semibold normal-case tracking-normal" style={{ color: '#C0C0C0' }}>
            (необврзно)
          </span>
        </label>
        <select
          value={town}
          onChange={(e) => { onTownChange(e.target.value); onSchoolChange('') }}
          style={{ ...selectStyle, borderColor: town ? '#5C35D4' : '#E5E7EB' }}>
          <option value="">— Одбери град —</option>
          {MK_TOWNS.map((t) => <option key={t} value={t}>{t}</option>)}
        </select>
      </div>

      {/* School — only shown once a town is selected */}
      {town && (
        <div>
          <label className="block text-xs font-black mb-1 tracking-widest" style={{ color: '#6B6B8A' }}>
            УЧИЛИШТЕ{' '}
            <span className="font-semibold normal-case tracking-normal" style={{ color: '#C0C0C0' }}>
              (необврзно)
            </span>
          </label>
          <select
            value={showCustom ? SCHOOL_OTHER : school}
            onChange={(e) => handleSchoolSelect(e.target.value)}
            style={{ ...selectStyle, borderColor: (school && !showCustom) ? '#5C35D4' : '#E5E7EB' }}>
            <option value="">— Одбери училиште —</option>
            {schools.map((s) => <option key={s} value={s}>{s}</option>)}
          </select>

          {/* Free-text input shown when "Друго" is selected */}
          {showCustom && (
            <div className="mt-2">
              <input
                type="text"
                value={customVal}
                onChange={(e) => handleCustomInput(e.target.value)}
                placeholder="Внеси го името на училиштето..."
                className="w-full px-4 py-3 rounded-2xl border-2 font-semibold text-base outline-none"
                style={{
                  borderColor: customVal ? '#5C35D4' : '#FFD93D',
                  color: '#1A1A2E',
                  background: '#FAFAFA',
                }}
              />
            </div>
          )}
        </div>
      )}
    </div>
  )
}
