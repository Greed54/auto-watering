# language=css
ENABLED_CHANNEL_STYLE = '''
#channel_tile_{channel_id} {{
    border: 2px solid rgb(235, 239, 239);
    border-radius: 10px;
    padding: 8px;
    background-color: #5AFF00;
}}
'''

# language=css
DISABLED_CHANNEL_STYLE = '''
#channel_tile_{channel_id} {{
    border: 2px solid rgb(235, 239, 239);
    border-radius: 10px;
    padding: 8px;
    background-color: #DFFF00;
}}          
'''

# language=css
INACTIVE_CHANNEL_STYLE = '''
#channel_tile_{channel_id} {{
    border: 2px solid rgb(235, 239, 239);
    border-radius: 10px;
    padding: 8px;
    background-color: lightgray;
}}   
'''

# language=css
ENABLED_PUMP_TILE_STYLE = '''
#pump_channel_tile {
    border: 2px solid rgb(235, 239, 239);
    border-radius: 10px;
    padding: 8px;
    background-color: #5AFF00;
}
'''

# language=css
DISABLED_PUMP_TILE_STYLE = '''
#pump_channel_tile {
    border: 2px solid rgb(235, 239, 239);
    border-radius: 10px;
    padding: 8px;
    background-color: #DFFF00;
}         
'''

# language=css
AUTO_WATERING_ENABLED_BUTTON_STYLE = '''
.startStopButton {
    background-color: #E83F25;
    color: white;
    border: none;
    border-radius: 15px;
    font-size: 30pt;
}

.startStopButton:pressed {
    background-color: #A62C2C;
}
'''

# language=css
AUTO_WATERING_DISABLED_BUTTON_STYLE = '''
.startStopButton {
    background-color: #1e88e5;
    color: white;
    border: none;
    border-radius: 15px;
    font-size: 30pt;
}

.startStopButton:pressed {
    background-color: #0d47a1;
}
'''
