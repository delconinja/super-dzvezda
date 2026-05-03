import type { Metadata } from 'next'
import { Nunito } from 'next/font/google'
import './globals.css'

const nunito = Nunito({
  subsets: ['latin'],
  weight: ['400', '600', '700', '800', '900'],
  variable: '--font-nunito',
})

export const metadata: Metadata = {
  title: 'Супер Ѕвезда',
  description: 'Платформа за учење за 5-9 одделение',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="mk" className={`${nunito.variable} h-full`}>
      <body className="min-h-full flex flex-col font-[family-name:var(--font-nunito)]">
        {children}
      </body>
    </html>
  )
}
