from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, RDFS, XSD
from rdflib.namespace import DC, FOAF





UNIV = Namespace("http://example.org/schema/")
# FOCU=Namespace("http://focu.io/schema#")
# FOCUDATA=Namespace("http://focu.io/data#")a
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
g.add((UNIV.courseName, RDF.type, RDF.Property))
g.add((UNIV.courseName, RDFS.subPropertyOf, FOAF.name))
g.add((UNIV.courseName, RDFS.domain, UNIV.Course))
g.add((UNIV.courseName, RDFS.range, RDFS.Literal))
g.add((UNIV.courseName, RDFS.label, Literal("Property for Course name", lang="en")))
g.add((UNIV.courseName, RDFS.comment, Literal("Property defined for storing name of courses offered by the university.", lang="en")))
g.add((UNIV.courseSubject, RDF.type, RDF.Property))
g.add((UNIV.courseSubject, RDFS.subPropertyOf, FOAF.name))
g.add((UNIV.courseSubject, RDFS.domain, UNIV.Course))
g.add((UNIV.courseSubject, RDFS.range, RDFS.Literal))
g.add((UNIV.courseSubject, RDFS.label, Literal("Property for Course subject", lang="en")))
g.add((UNIV.courseSubject, RDFS.comment, Literal("Property defined for storing subject of the corresponding course.", lang="en")))
g.add((UNIV.courseNo, RDF.type, RDF.Property))
g.add((UNIV.courseNo, RDFS.domain, UNIV.Course))
g.add((UNIV.courseNo, RDFS.range, RDFS.Literal))
g.add((UNIV.courseNo, RDFS.label, Literal("Property for Course number", lang="en")))
g.add((UNIV.courseNo, RDFS.comment, Literal("Property defined for storing number of the corresponding course.", lang="en")))
g.add((UNIV.courseDescription, RDF.type, RDF.Property))
g.add((UNIV.courseDescription, RDFS.domain, UNIV.Course))
g.add((UNIV.courseDescription, RDFS.range, RDFS.Literal))
g.add((UNIV.courseDescription, RDFS.label, Literal("Property for Course description", lang="en")))
g.add((UNIV.courseDescription, RDFS.comment, Literal("Property defined for storing description of the corresponding course.", lang="en")))
g.add((UNIV.Topic, RDF.type, RDFS.Class))
g.add((UNIV.Topic, RDFS.subClassOf, FOAF.Document))
g.add((UNIV.Topic, RDFS.label, Literal("Class for topics of a Course", lang="en")))
g.add((UNIV.Topic, RDFS.comment, Literal("Class defined for depicting topics of the corresponding course.", lang="en")))
g.add((UNIV.topicName, RDF.type, RDF.Property))
g.add((UNIV.topicName, RDFS.subPropertyOf, FOAF.topic))
g.add((UNIV.topicName, RDFS.domain, UNIV.Topic))
g.add((UNIV.courseDescription, RDFS.comment, Literal("Property defined for storing description of the corresponding course.", lang="en")))
g.add((UNIV.hasTopic, RDF.type, RDF.Property))
g.add((UNIV.hasTopic, RDFS.domain, UNIV.Course))
g.add((UNIV.hasTopic, RDFS.range, UNIV.Topic))
g.add((UNIV.hasTopic, RDFS.label, Literal("Property for linking course and its topics.", lang="en")))
g.add((UNIV.hasTopic, RDFS.comment, Literal("Property for linking course and its corresponding topics.", lang="en")))


g.add((UNIV.Student, RDF.type, RDFS.Class))
g.add((UNIV.Student, RDFS.subClassOf, FOAF.Person))
g.add((UNIV.Student, RDFS.label, Literal("Class for Student is a University", lang="en")))
g.add((UNIV.Student, RDFS.comment, Literal("Class defined for Students of a corresponding university.", lang="en")))
g.add((UNIV.enrolledAt, RDF.type, RDF.Property))
g.add((UNIV.enrolledAt, RDFS.domain, UNIV.Student))
g.add((UNIV.enrolledAt, RDFS.range, UNIV.University))
g.add((UNIV.enrolledAt, RDFS.label, Literal("Property to define link between student and university.", lang="en")))
g.add((UNIV.enrolledAt, RDFS.comment, Literal("Property to define link between student and university.", lang="en")))
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
g.add((UNIV.inTerm, RDF.type, RDF.Property))
g.add((UNIV.inTerm, RDFS.domain, UNIV.Grade))
g.add((UNIV.inTerm, RDFS.range, RDFS.Literal))
g.add((UNIV.inTerm, RDFS.label, Literal("Associating Grade and Term", lang="en")))
g.add((UNIV.inTerm, RDFS.comment, Literal("Associating Grade and Term", lang="en")))
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
g.serialize(destination='rdfSchema.ttl', format='turtle')
print(g.serialize(format="turtle"))




