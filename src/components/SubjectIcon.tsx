import type { Subject } from '@/types'

interface Props {
  subject: Subject
  size?: 'sm' | 'md' | 'lg'
  className?: string
}

const flagSizes = { sm: 'w-7 h-5', md: 'w-10 h-7', lg: 'w-14 h-10' }
const emojiSizes = { sm: 'text-xl', md: 'text-3xl', lg: 'text-5xl' }

export default function SubjectIcon({ subject, size = 'md', className = '' }: Props) {
  if (subject.flagCode) {
    return (
      <img
        src={`/flags/${subject.flagCode}.svg`}
        alt={subject.name}
        className={`${flagSizes[size]} object-cover rounded shadow-sm ${className}`}
      />
    )
  }
  return <span className={`${emojiSizes[size]} ${className}`}>{subject.emoji}</span>
}
