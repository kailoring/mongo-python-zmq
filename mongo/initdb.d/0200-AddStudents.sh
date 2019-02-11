# Create some students

mongo GradeBook <<EOF 

db.students.insert({name: "Frodo", grades: [20,23,15]})
db.students.insert({name: "Bilbo", grades: [22,18,24]})

EOF

