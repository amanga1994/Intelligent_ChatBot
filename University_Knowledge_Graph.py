from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef, RDFS, XSD
from rdflib.namespace import DC, FOAF

UNIV = Namespace("http://example.org/schema#")
# FOCU=Namespace("http://focu.io/schema#")
# FOCUDATA=Namespace("http://focu.io/data#")
g = Graph()
g.add((UNIV.University, RDF.type, RDFS.Class))
g.add((UNIV.University, RDFS.subClassOf, FOAF.Organization))
g.add((UNIV.Name, RDF.type, RDF.Property))
g.add((UNIV.Name, RDFS.subPropertyOf, FOAF.name))
g.add((UNIV.Name, RDFS.domain, UNIV.University))
g.add((UNIV.Name, RDFS.range, Literal("", datatype=XSD.string)))
g.add((UNIV.DBPediaLink, RDF.type, RDF.Property))
g.add((UNIV.DBPediaLink, RDFS.subPropertyOf, FOAF.homepage))
g.add((UNIV.DBPediaLink, RDFS.domain, UNIV.University))

g.add((UNIV.Course, RDF.type, RDF.Class))
g.add((UNIV.CourseName, RDF.type, RDF.Property))
g.add((UNIV.CourseName, RDFS.subPropertyOf, FOAF.name))
g.add((UNIV.CourseName, RDFS.domain, UNIV.Course))
g.add((UNIV.CourseName, RDFS.range, Literal("", datatype=XSD.string)))
g.add((UNIV.CourseSubject, RDF.type, RDF.Property))
g.add((UNIV.CourseSubject, RDFS.subPropertyOf, FOAF.name))
g.add((UNIV.CourseSubject, RDFS.domain, UNIV.Course))
g.add((UNIV.CourseSubject, RDFS.range, Literal("", datatype=XSD.string)))
g.add((UNIV.CourseNumber, RDF.type, RDF.Property))
g.add((UNIV.CourseNumber, RDFS.domain, UNIV.Course))
g.add((UNIV.CourseNumber, RDFS.range, Literal("", datatype=XSD.int)))
g.add((UNIV.CourseDescription, RDF.type, RDF.Property))
g.add((UNIV.CourseDescription, RDFS.domain, UNIV.Course))
g.add((UNIV.CourseDescription, RDFS.range, Literal("", datatype=XSD.String)))

g.add((UNIV.topic, RDF.type, RDFS.Class))
g.add((UNIV.topic, RDFS.subClassOf, FOAF.Document))
g.add((UNIV.TopicName, RDF.type, RDFS.Property))
g.add((UNIV.TopicName, RDFS.subPropertyOf, FOAF.topic))
g.add((UNIV.TopicName, RDFS.domain, UNIV.topic))
g.add((UNIV.topicName, RDFS.))






# @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
# @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
# @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
# @prefix foaf: <http://xmlns.com/foaf/0.1/> .
# @prefix focu: <http://focu.io/schema#> .
# @prefix focudata: <http://focu.io/data#> .
# g.add((FOCU.University, RDF.type, RDFS.Class))
# g.add((FOCU.University, RDFS.subClassOf, FOAF.Organization))
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
g.serialize(destination='output.txt', format='xml')
print(g.serialize(format="turtle"))

# Add yourself as a Person
# Add some properties, like first name, last name, age, mbox (email), etc.
# Validate your graph using the tools you used in the previous lab.



