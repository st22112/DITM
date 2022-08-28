import easygui
message = easygui.enterbox("What is your name?")
easygui.msgbox("Hello {}".format(message), 'ok')
