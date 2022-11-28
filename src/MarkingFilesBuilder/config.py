import json, os






def load_json_config():
    if os.path.exists('template.json'):
        with open('template.json') as file_data:
            return json.load(file_data)
    else:
        with open('template.json', 'w') as json_file:
            template_data = return_template()
            json.dump(template_data, json_file, indent=4)
            return template_data


def return_template():
    json_template = {
    "templates" : {
        "Info" : {
                "FileType" : "CCL100 Marking Layout File", 
                "Version" : "1.0"
            }
        ,
        "Count" : {
                "Number" : 9
            }
        ,
        "FileParams" : {
            "rotation" : 0.00000, 
            "xoffset" : 0.00000, 
            "yoffset" : 0.00000, 
            "mirrored" : 0, 
            "flipped" : 0
            }
        ,
        "CircleL" : {
            "char" : 0, 
            "enabled" : 0, 
            "font" : 20, 
            "pen" : 1, 
            "height" : 1.500000, 
            "width" : 1.500000, 
            "x" : 17.00000, 
            "y" : 0.00000, 
            "rotation" : 0.00000, 
            "orientation" : 5, 
            "flipping" : 0, 
            "decimalsign" : 1, 
            "digits" : 2, 
            "type" : 6, 
            "name" : "CircleL"
            }
        ,
        "CircleR" : {
            "char" : 0,
            "enabled" : 0, 
            "font" : 20, 
            "pen" : 1, 
            "height" : 1.500000, 
            "width" : 1.500000, 
            "x" : 17.00000, 
            "y" : 0.00000, 
            "rotation" : 0.00000, 
            "orientation" : 5, 
            "flipping" : 0, 
            "decimalsign" : 1, 
            "digits" : 2, 
            "type" : 6, 
            "name" : "CircleR"
            }
        ,
        "Logo" : {
            "char" : 0, 
            "enabled" : 0, 
            "font" : 32, 
            "pen" : 2, 
            "height" : 2.00000, 
            "width" : 2.500000, 
            "x" : 17.00000, 
            "y" : -6.00000, 
            "rotation" : 0.00000, 
            "orientation" : 5, 
            "mirrorin" : 1, 
            "flipping" : 0, 
            "decimalsign" : 1, 
            "digits" : 2, 
            "type" : 6, 
            "name" : "Logo"
            }
        
    },
    "Text" : {
        "text" : "",
        "enabled" : 0,
        "font" : 10,
        "pen" : 3,
        "height" : 1.500000,
        "width" : 1.500000,
        "x" : 0.000000,
        "y" : 0.000000,
        "rotation" : 0.000000,
        "orientation" : 5,
        "mirroring" : 0,
        "flipping" : 0,
        "decimalsign" : 0,
        "digits" : 2,
        "type" : 6,
        "name" : ""
    }
}
    return json_template



if __name__ == '__main__':
    config = load_json_config()
    print(config)