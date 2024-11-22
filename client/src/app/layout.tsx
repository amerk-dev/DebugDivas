import type { Metadata } from 'next'
import fonts from '@/fonts'
import '@/styles/main.scss'
import { Header } from '@/components/shared'

export const metadata: Metadata = {
  title: 'Create Next App',
  description: 'Generated by create next app',
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body className={`${fonts.oswald.variable} ${fonts.raleway.variable}`}>
        <Header />

        <main>{children}</main>

        <footer></footer>
      </body>
    </html>
  )
}
