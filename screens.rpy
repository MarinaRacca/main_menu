screen main_menu():

    ## Every menu screens are replaced.
    tag menu
    ## add the backgorund image
    add gui.main_menu_background

    ## If you want to take in another screen: use statemant + the name of the screen
    use navigation
    
    ##Add some button to your menu
    
    imagebutton idle "start.png" hover "start_hover.png" xpos 1000 ypos 570 focus_mask None action Start() mouse "hand" 
    imagebutton idle "end.png" hover "end_hover.png" xpos 1000 ypos 730 focus_mask None action Quit() mouse "hand"
    
    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text



