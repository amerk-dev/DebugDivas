import { Oswald, Raleway } from 'next/font/google'

const raleway = Raleway({
  weight: ['100', '200', '300', '400', '500', '600', '700', '800', '900'],
  variable: '--font-raleway',
  subsets: ['cyrillic', 'latin'],
})

const oswald = Oswald({
  weight: ['200', '300', '400', '500', '600', '700'],
  variable: '--font-oswald',
  subsets: ['cyrillic', 'latin'],
})

const fonts = { oswald, raleway }

export default fonts
