import os
class Settings:
    def __init__(self):
        # define the settings
        self.ini = {
            'Aircraft': {
                'blue': '1',
                'red': '1',
                'blue_strategy': 'Random',
                'red_strategy': 'Random'
            }
        }
        # load the settings
        if os.path.exists('2DAircraftPlat\settings.ini'):
            with open('2DAircraftPlat\settings.ini', 'r') as f:
                for line in f:
                    if line.startswith('['):
                        section = line[1:-2]
                    elif line.strip() != '':
                        key, value = line.split('=')
                        self.ini[section][key] = value[:-1]
        else :
            self.save()

    def save(self):
        # save the settings
        with open('2DAircraftPlat\settings.ini', 'w') as f:
            for section in self.ini:
                f.write('[{}]\n'.format(section))
                for key in self.ini[section]:
                    f.write('{}={}\n'.format(key, self.ini[section][key]))
                f.write('\n')

    def get(self, section, key):
        return self.ini[section][key]


