student_data = {'id1':
    {'name': ['sara'],
     'class': ['v'],
     'subject_integragation': ['english,math,science']
    },
    'id2':
     {'name': ['David'],
     'class': ['v'],
     'subject_integragation': ['english,math,science']
    },
    "id3":
     {'name': ['sara'],
     'class': ['v'],
     'subject_integragation': ['english,math,science']
    },
    'id4':
    {'name': ['sarya'],
     'class': ['v'],
     'subject_integragation': ['english,math,science']
    },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)