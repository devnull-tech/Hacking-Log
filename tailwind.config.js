/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './tools/templates/**/*.html',
    './hacklog/templates/**/*.html',
    './home/templates/**/*.html',
  ],
  theme: {
    extend: {
      typography: (theme) => ({
        dark: {
          css: {
            color: theme('colors.gray.300'),
            '[class~="lead"]': { 
              color: theme('colors.gray.400') 
            },
            a: { 
              color: theme('colors.blue.400') 
            },
            strong: { 
              color: theme('colors.gray.200') 
            },
            'ol > li::before': { 
              color: theme('colors.gray.400') 
            },
            'ul > li::before': { 
              backgroundColor: theme('colors.gray.600') 
            },
            hr: { 
              borderColor: theme('colors.gray.700') 
            },
            blockquote: { 
              color: theme('colors.gray.200') 
            },
            h1: { 
              color: theme('colors.gray.100') 
            },
            h2: { 
              color: theme('colors.gray.100') 
            },
            h3: { 
              color: theme('colors.gray.100') 
            },
            h4: { 
              color: theme('colors.gray.100') 
            },
            code: { 
              color: theme('colors.gray.200') 
            },
            'a code': { 
              color: theme('colors.gray.200') 
            },
            pre: { 
              color: theme('colors.gray.200'), 
              backgroundColor: theme('colors.gray.800') 
            },
            thead: { 
              color: theme('colors.gray.100'), 
              borderBottomColor: theme('colors.gray.700') 
            },
            'tbody tr': { 
              borderBottomColor: theme('colors.gray.800') 
            },
          },
        },
      }),
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
