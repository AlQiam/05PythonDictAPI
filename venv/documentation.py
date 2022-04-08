import justpy as jp


class Doc:

    def serve(self):
        wp = jp.WebPage()
        div = jp.Div(a=wp, classes='bg-gray-200 h-screen')

        jp.Div(a=div, text='Instant Dictionary API',
               classes='text-4xl m-2')
        jp.Div(a=div, text='Get Definitions of a word',
               classes='text-lg')

        jp.Hr(a=div)
        jp.Div(a=div, text='www.example.com/api?w=cat')
        jp.Hr(a=div)
        jp.Div(a=div, text="""
        {"word": "cat",
        "definition": ["A common four-legged animal (Felis silvestris) that is often kept as a household pet."]}
        """)
        return wp
