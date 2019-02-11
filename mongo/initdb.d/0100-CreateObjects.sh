# Create a database and collection for student information

mongo <<EOF 

use GradeBook

db.createCollection("students")

EOF
