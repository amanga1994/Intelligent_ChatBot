from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, RDFS, XSD
from rdflib.namespace import DC, FOAF



UNIV = Namespace("http://example.org/schema#")
# FOCU=Namespace("http://focu.io/schema#")
# FOCUDATA=Namespace("http://focu.io/data#")
g = Graph()
g.add((UNIV.University, RDF.type, RDFS.Class))
g.add((UNIV.University, RDFS.subClassOf, FOAF.Organization))
g.add((UNIV.University, RDFS.label, Literal("Class defined for university", lang="en")))
g.add((UNIV.University, RDFS.comment, Literal("This class is used to take information about the university", lang="en")))
g.add((UNIV.hasName, RDF.type, RDF.Property))
g.add((UNIV.hasName, RDFS.subPropertyOf, FOAF.name))
g.add((UNIV.hasName, RDFS.domain, UNIV.University))
g.add((UNIV.hasName, RDFS.range, RDFS.Literal))
g.add((UNIV.hasName, RDFS.label, Literal("Property for University Name", lang="en")))
g.add((UNIV.hasName, RDFS.comment, Literal("Property defined for inputing University Name", lang="en")))
g.add((UNIV.hasDBPediaLink, RDF.type, RDF.Property))
g.add((UNIV.hasDBPediaLink, RDFS.subPropertyOf, FOAF.homepage))
g.add((UNIV.hasDBPediaLink, RDFS.domain, UNIV.University))
g.add((UNIV.hasDBPediaLink, RDFS.label, Literal("Property for DBPedia Link", lang="en")))
g.add((UNIV.hasDBPediaLink, RDFS.comment, Literal("Property defined for linking University with its dbpedia link.", lang="en")))

g.add((UNIV.Course, RDF.type, RDFS.Class))
g.add((UNIV.Course, RDFS.label, Literal("Class for University courses.", lang="en")))
g.add((UNIV.Course, RDFS.comment, Literal("Classes created for defining courses offered by the university.", lang="en")))
g.add((UNIV.CourseName, RDF.type, RDF.Property))
g.add((UNIV.CourseName, RDFS.subPropertyOf, FOAF.name))
g.add((UNIV.CourseName, RDFS.domain, UNIV.Course))
g.add((UNIV.CourseName, RDFS.range, RDFS.Literal))
g.add((UNIV.CourseName, RDFS.label, Literal("Property for Course name", lang="en")))
g.add((UNIV.CourseName, RDFS.comment, Literal("Property defined for storing name of courses offered by the university.", lang="en")))
g.add((UNIV.CourseSubject, RDF.type, RDF.Property))
g.add((UNIV.CourseSubject, RDFS.subPropertyOf, FOAF.name))
g.add((UNIV.CourseSubject, RDFS.domain, UNIV.Course))
g.add((UNIV.CourseSubject, RDFS.range, RDFS.Literal))
g.add((UNIV.CourseSubject, RDFS.label, Literal("Property for Course subject", lang="en")))
g.add((UNIV.CourseSubject, RDFS.comment, Literal("Property defined for storing subject of the corresponding course.", lang="en")))
g.add((UNIV.CourseNumber, RDF.type, RDF.Property))
g.add((UNIV.CourseNumber, RDFS.domain, UNIV.Course))
g.add((UNIV.CourseNumber, RDFS.range, RDFS.Literal))
g.add((UNIV.CourseNumber, RDFS.label, Literal("Property for Course number", lang="en")))
g.add((UNIV.CourseNumber, RDFS.comment, Literal("Property defined for storing number of the corresponding course.", lang="en")))
g.add((UNIV.CourseDescription, RDF.type, RDF.Property))
g.add((UNIV.CourseDescription, RDFS.domain, UNIV.Course))
g.add((UNIV.CourseDescription, RDFS.range, RDFS.Literal))
g.add((UNIV.CourseDescription, RDFS.label, Literal("Property for Course description", lang="en")))
g.add((UNIV.CourseDescription, RDFS.comment, Literal("Property defined for storing description of the corresponding course.", lang="en")))
g.add((UNIV.topic, RDF.type, RDFS.Class))
g.add((UNIV.topic, RDFS.subClassOf, FOAF.Document))
g.add((UNIV.topic, RDFS.label, Literal("Class for topics of a Course", lang="en")))
g.add((UNIV.topic, RDFS.comment, Literal("Class defined for depicting topics of the corresponding course.", lang="en")))
g.add((UNIV.TopicName, RDF.type, RDF.Property))
g.add((UNIV.TopicName, RDFS.subPropertyOf, FOAF.topic))
g.add((UNIV.TopicName, RDFS.domain, UNIV.topic))

g.add((UNIV.Student, RDF.type, RDFS.Class))
g.add((UNIV.Student, RDFS.subClassOf, FOAF.Person))
g.add((UNIV.Student, RDFS.label, Literal("Class for Student is a University", lang="en")))
g.add((UNIV.Student, RDFS.comment, Literal("Class defined for Students of a corresponding university.", lang="en")))
g.add((UNIV.hasID, RDF.type, RDF.Property))
g.add((UNIV.hasID, RDFS.domain, UNIV.Student))
g.add((UNIV.hasID, RDFS.range, RDFS.Literal))
g.add((UNIV.hasID, RDFS.label, Literal("Property to link Student IDs", lang="en")))
g.add((UNIV.hasID, RDFS.comment, Literal("Property to link Student IDs", lang="en")))
g.add((UNIV.Grade, RDF.type, RDFS.Class))
g.add((UNIV.Grade, RDFS.label, Literal("Represents Grade of a student.", lang="en")))
g.add((UNIV.Grade, RDFS.comment, Literal("Represents Grade of a student in a particular course", lang="en")))
g.add((UNIV.hasGradeValue, RDF.type, RDF.Property))
g.add((UNIV.hasGradeValue, RDFS.domain, UNIV.Grade))
g.add((UNIV.hasGradeValue, RDFS.range, RDFS.Literal))
g.add((UNIV.hasGradeValue, RDFS.label, Literal("Represents value of a grade.", lang="en")))
g.add((UNIV.hasGradeValue, RDFS.comment, Literal("Represents alphabetical grade of a student in a particular course", lang="en")))
g.add((UNIV.inCourse, RDF.type, RDF.Property))
g.add((UNIV.inCourse, RDFS.domain, UNIV.Grade))
g.add((UNIV.inCourse, RDFS.range, UNIV.Course))
g.add((UNIV.inCourse, RDFS.label, Literal("Associating Grade and Course", lang="en")))
g.add((UNIV.inCourse, RDFS.comment, Literal("Associating Grade and Course", lang="en")))
g.add((UNIV.hasGrade, RDF.type, RDF.Property))
g.add((UNIV.hasGrade, RDFS.domain, UNIV.Student))
g.add((UNIV.hasGrade, RDFS.range, UNIV.Grade))
g.add((UNIV.hasGrade, RDFS.label, Literal("Associating Student and Grade.", lang="en")))
g.add((UNIV.hasGrade, RDFS.comment, Literal("Associating Student and Grade.", lang="en")))






# @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
# @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
# @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
# @prefix foaf: <http://xmlns.com/foaf/0.1/> .
# @prefix focu: <http://focu.io/schema#> .
# @prefix focudata: <http://focu.io/data#> .
# g.add((FOCU.University, RDF.type, RDFS.Class))
# g.add((FOCU.University, RDFS.subClassOf, FOAF.Organization))\

# g.add((FOCU.Student, RDFS.subClassOf, FOAF.person))
# g.add((FOCU.Professor, RDFS.subClassOf, FOAF.person))
# g.add((FOCU.isEnrolledAt, RDF.type, RDF.Property))
# g.add((FOCU.teaches, RDF.type, RDF.Property))
# g.add((FOCU.isEnrolledAt, RDFS.domain, FOCU.Student))
# g.add((FOCU.isEnrolledAt, RDFS.range, FOCU.University))
# g.add((FOCU.teaches, RDFS.domain, FOCU.Professor))
# g.add((FOCU.teaches, RDFS.range, FOCU.Student))
# g.add((FOCUDATA.Concordia, RDF.type, FOCU.University))
# g.add((FOCUDATA.Aman, RDF.type, FOCU.Student))
# g.add((FOCUDATA.Aman, FOAF.firstName, Literal("Aman")))
# g.add((FOCUDATA.Aman, FOAF.lastName, Literal("Garg")))
# g.add((FOCUDATA.Aman, FOAF.mbox, Literal("amangarg@gmail.com", datatype=XSD.anyURI)))
# g.add((FOCUDATA.Aman, FOCU.isenrolledAt, FOCUDATA.Concordia))
g.serialize(destination='output.txt', format='turtle')
print(g.serialize(format="turtle"))




