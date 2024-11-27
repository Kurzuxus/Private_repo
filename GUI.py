import flet as ft



def main(page:ft.Page):

    page.window_width=1280
    page.window_height=720
    page.window.always_on_top=True


    page.vertical_alignment=ft.MainAxisAlignment.START
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    def Animate(e):
        if e.data=='true':
            e.control.scale=1.10
        else:
            e.control.scale=1
        e.control.update()

    def Register():
        Dialog=ft.AlertDialog(title=ft.Text('User Successfuly Added!',
                            font_family='Century Gothic',
                            color='black',
                            size=25,
                            weight='bold'),
                            bgcolor='white',
                            alignment=ft.alignment.center)
        page.open(Dialog)

    Title=ft.Text('Visa Account Data Entry',
                font_family='Century Gothic',
                weight='bold',
                size=40)
    
    Main_cont=ft.Container(bgcolor='white',
                        border_radius=20,
                        width=page.window.width,
                        height=page.window.height-150,
                        margin=ft.margin.only(left=50,right=50),
                        content=ft.Column(alignment=ft.MainAxisAlignment.START,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=20),
                        padding=ft.padding.all(20))
    
    Email_heading=ft.Text('User Email',
                        color='black',
                        font_family='Century Gothic',
                        weight='bold',
                        size=18)

    Email_inpt=ft.TextField(width=300,
                        border_radius=12,
                        border_width=0,
                        bgcolor='black')
    
    Password_heading=ft.Text('User Password',
                        color='black',
                        font_family='Century Gothic',
                        weight='bold',
                        size=18)

    Password_inpt=ft.TextField(width=300,
                        border_radius=12,
                        border_width=0,
                        bgcolor='black')
    
    Submit_bu=ft.ElevatedButton('Submit Information',
                                bgcolor='black',
                                width=200,
                                height=45,
                                style=ft.ButtonStyle(text_style=ft.TextStyle(
                                    font_family='Century Gothic',
                                    weight='bold'
                                )),
                                color='white',
                                scale=ft.transform.Scale(1),
                                animate_scale=ft.animation.Animation(500,ft.AnimationCurve.FAST_OUT_SLOWIN),
                                on_hover=lambda e: Animate(e),
                                on_click=lambda e: Register())
    

    Category=ft.Dropdown(bgcolor='black',
                        hint_text='User Category',
                        width=300,
                        border_radius=12,
                        options=[ft.dropdown.Option('Express'),
                                ft.dropdown.Option('<2 Months'),
                                ft.dropdown.Option('<3 Months'),
                                ft.dropdown.Option('Any')])
    
    Main_cont.content.controls.extend([Email_heading,Email_inpt,
                                    Password_heading,Password_inpt,
                                    Category,
                                    Submit_bu])


    page.add(Title,Main_cont)


ft.app(target=main)