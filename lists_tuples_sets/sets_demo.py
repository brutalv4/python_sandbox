cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(f'''{cs_courses}
{art_courses}

intersection() - {cs_courses.intersection(art_courses)}
difference() - {cs_courses.difference(art_courses)}
union() - {cs_courses.union(art_courses)}
''')
