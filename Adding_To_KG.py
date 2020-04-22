from rdflib import Graph, Literal, Namespace, RDF, RDFS, BNode, URIRef
from rdflib.namespace import FOAF, RDFS, OWL, XSD
import csv
import spotlight
import time
import re
graph = Graph()
graph.parse("rdfSchema.ttl", format="n3")
UNIV = Namespace("http://example.org/schema#")
g = Graph()
u = Namespace("http://example.org/university/")
g.add((u.Concordia, RDF.type, UNIV.University))
g.add((u.Concordia, UNIV.hasName, Literal("Concordia University")))
g.add((u.Concordia, UNIV.hasDBPediaLink, URIRef("http://dbpedia.org/page/Concordia_University")))

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row and len(row[0])>0:
            try:
                subject = " ".join(row[0].split()[0].split())
                no =" ".join(row[0].split()[1].split())
                # no= re.sub("\s\s+", " ", row[0].split()[1])
                name = " ".join(row[1].split())
                description = " ".join(row[2].split())
            except:
                no=subject[4:]
                subject=subject[0:4]
            x=URIRef(f"http://example.org/course/{subject}+{no}")
            print(row)
            g.add((x, RDF.type, UNIV.Course))
            g.add((x, UNIV.courseName, Literal(name)))
            g.add((x, UNIV.courseSubject, Literal(subject)))
            g.add((x, UNIV.courseNo, Literal(no)))
            if "Prerequisite:" in description:
                try:
                    desc = ' '.join(description[description.index(".") + 1:].split())
                    print(desc)
                    g.add((x, UNIV.courseDescription, Literal(desc)))
                except:
                    print(f"Exception{description}")
                    g.add((x, UNIV.courseDescription, Literal(description)))
            else:
                g.add((x, UNIV.courseDescription, Literal(description)))
            g.add((x, RDFS.seeAlso, URIRef(" ".join(row[3].split()))))


count=0
for s, p, o in g.triples((None, RDF.type, UNIV.Course)):
    occurred=False
    Name = [i for i in g.objects(s, UNIV.courseName)][0]
    Description = [i for i in g.objects(s, UNIV.courseDescription)][0]
    to_search = f"{Name}. {Description}"
    timer = 5
    count += 1
    print(f"count:{count}")
    try:
        annotations = spotlight.annotate('https://api.dbpedia-spotlight.org/en/annotate', to_search, confidence=0.5,
                                         support=20)
    except Exception as e:
        print(str(e))
        if("No Resources" not in str(e)):
            occurred = True
            time.sleep(120)
        continue
    print(f"{[i for i in g.objects(s, UNIV.courseSubject)][0]} {[i for i in g.objects(s, UNIV.courseNo)][0]}")
    for i in annotations:
        if (None, OWL.sameAs, URIRef(i["URI"])) not in graph:
            x = URIRef(f"http://example.org/topic/{i['surfaceForm'].replace(' ', '_')}")
            g.add((x, RDF.type, UNIV.Topic))
            g.add((x, UNIV.topicName, Literal(i['surfaceForm'].replace(' ', '_').lower())))
            g.add((x, OWL.sameAs, URIRef(i['URI'])))
            g.add((s, UNIV.hasTopic, x))
        else:
            topic = g.subjects(OWL.sameAs, URIRef(i['URI']))
            g.add(s, UNIV.hasTopic, topic)

    for i in g.objects(s, UNIV.hasTopic):
        print(i)
    # time.sleep(0.5)




s = Namespace("http://example.org/student/")

g.add((s.Joe, RDF.type, UNIV.Student))
g.add((s.Joe, FOAF.givenName, Literal("Joe")))
g.add((s.Joe, FOAF.familyName, Literal("Black")))
g.add((s.Joe, UNIV.hasID, Literal("40085530")))
g.add((s.Joe, FOAF.mbox, Literal("joeblack@gmail.com")))
g.add((s.Joe, UNIV.enrolledAt, u.Concordia))
Grade = BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Joe, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("A")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+220")))
g.add((Grade, UNIV.inTerm, Literal("Fall 2020")))
Grade = BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Joe, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("B")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+223")))
g.add((Grade, UNIV.inTerm, Literal("Summer 2020")))


g.add((s.Aman, RDF.type, UNIV.Student))
g.add((s.Aman, FOAF.givenName, Literal("Aman")))
g.add((s.Aman, FOAF.familyName, Literal("Garg")))
g.add((s.Aman, UNIV.hasID, Literal("40085531")))
g.add((s.Aman, FOAF.mbox, Literal("amangarg@gmail.com")))
g.add((s.Aman, UNIV.enrolledAt, u.Concordia))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Aman, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("B")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+220")))
g.add((Grade, UNIV.inTerm, Literal("Fall 2020")))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Aman, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("F")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+223")))
g.add((Grade, UNIV.inTerm, Literal("Summer 2020")))

g.add((s.Basant, RDF.type, UNIV.Student))
g.add((s.Basant, FOAF.givenName, Literal("Basant")))
g.add((s.Basant, FOAF.familyName, Literal("Gera")))
g.add((s.Basant, UNIV.hasID, Literal("40085532")))
g.add((s.Basant, FOAF.mbox, Literal("basantgera@gmail.com")))
g.add((s.Basant, UNIV.enrolledAt, u.Concordia))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Basant, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("A")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+220")))
g.add((Grade, UNIV.inTerm, Literal("Fall 2020")))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Basant, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("A")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+223")))
g.add((Grade, UNIV.inTerm, Literal("Summer 2020")))

g.add((s.Arpit, RDF.type, UNIV.Student))
g.add((s.Arpit, FOAF.givenName, Literal("Arpit")))
g.add((s.Arpit, FOAF.familyName, Literal("Malhotra")))
g.add((s.Arpit, UNIV.hasID, Literal("40085533")))
g.add((s.Arpit, FOAF.mbox, Literal("arpitmalhotra@gmail.com")))
g.add((s.Arpit, UNIV.enrolledAt, u.Concordia))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Arpit, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("A")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+220")))
g.add((Grade, UNIV.inTerm, Literal("Fall 2020")))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Arpit, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("B")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+223")))
g.add((Grade, UNIV.inTerm, Literal("Summer 2020")))

g.add((s.Rohit, RDF.type, UNIV.Student))
g.add((s.Rohit, FOAF.givenName, Literal("Rohit")))
g.add((s.Rohit, FOAF.familyName, Literal("Gupta")))
g.add((s.Rohit, UNIV.hasID, Literal("40085534")))
g.add((s.Rohit, FOAF.mbox, Literal("rohitgupta@gmail.com")))
g.add((s.Rohit, UNIV.enrolledAt, u.Concordia))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Rohit, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("A")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+220")))
g.add((Grade, UNIV.inTerm, Literal("Fall 2020")))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Rohit, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("B")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+223")))
g.add((Grade, UNIV.inTerm, Literal("Summer 2020")))

g.add((s.Shubham, RDF.type, UNIV.Student))
g.add((s.Shubham, FOAF.givenName, Literal("Shubham")))
g.add((s.Shubham, FOAF.familyName, Literal("Kumar")))
g.add((s.Shubham, UNIV.hasID, Literal("40085535")))
g.add((s.Shubham, FOAF.mbox, Literal("shubhamkumar@gmail.com")))
g.add((s.Shubham, UNIV.enrolledAt, u.Concordia))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Shubham, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("A")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+220")))
g.add((Grade, UNIV.inTerm, Literal("Fall 2020")))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Shubham, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("B")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+223")))
g.add((Grade, UNIV.inTerm, Literal("Summer 2020")))

g.add((s.Sunchit, RDF.type, UNIV.Student))
g.add((s.Sunchit, FOAF.givenName, Literal("Sunchit")))
g.add((s.Sunchit, FOAF.familyName, Literal("Sehgal")))
g.add((s.Sunchit, UNIV.hasID, Literal("40085536")))
g.add((s.Sunchit, FOAF.mbox, Literal("sunchitsehgal@gmail.com")))
g.add((s.Sunchit, UNIV.enrolledAt, u.Concordia))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Sunchit, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("A")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+220")))
g.add((Grade, UNIV.inTerm, Literal("Fall 2020")))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Sunchit, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("B")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+223")))
g.add((Grade, UNIV.inTerm, Literal("Summer 2020")))

g.add((s.Badal, RDF.type, UNIV.Student))
g.add((s.Badal, FOAF.givenName, Literal("Badal")))
g.add((s.Badal, FOAF.familyName, Literal("Kumar")))
g.add((s.Badal, UNIV.hasID, Literal("40085537")))
g.add((s.Badal, FOAF.mbox, Literal("badalkumar@gmail.com")))
g.add((s.Badal, UNIV.enrolledAt, u.Concordia))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Badal, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("A")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+220")))
g.add((Grade, UNIV.inTerm, Literal("Fall 2020")))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Badal, UNIV.hasGrade, Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("B")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+223")))
g.add((Grade, UNIV.inTerm, Literal("Summer 2020")))

g.add((s.Akash, RDF.type, UNIV.Student))
g.add((s.Akash, FOAF.givenName, Literal("Akash")))
g.add((s.Akash, FOAF.familyName, Literal("Singh")))
g.add((s.Akash, UNIV.hasID, Literal("40085538")))
g.add((s.Akash, FOAF.mbox, Literal("akashsingh@gmail.com")))
g.add((s.Akash, UNIV.enrolledAt, u.Concordia))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Akash, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("A")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+220")))
g.add((Grade, UNIV.inTerm, Literal("Fall 2020")))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Akash, UNIV.hasGrade, Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("B")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+223")))
g.add((Grade, UNIV.inTerm, Literal("Summer 2020")))

g.add((s.Ofreish, RDF.type, UNIV.Student))
g.add((s.Ofreish, FOAF.givenName, Literal("Ofreish")))
g.add((s.Ofreish, FOAF.familyName, Literal("Talwar")))
g.add((s.Ofreish, UNIV.hasID, Literal("40085539")))
g.add((s.Ofreish, FOAF.mbox, Literal("otalwar@gmail.com")))
g.add((s.Ofreish, UNIV.enrolledAt, u.Concordia))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Ofreish, UNIV.hasGrade,Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("A")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+220")))
g.add((Grade, UNIV.inTerm, Literal("Fall 2020")))
Grade=BNode()
g.add((Grade, RDF.type, UNIV.Grade))
g.add((s.Ofreish, UNIV.hasGrade, Grade))
g.add((Grade, UNIV.hasGradeValue, Literal("B")))
g.add((Grade, UNIV.inCourse, URIRef("http://example.org/course/AHSC+223")))
g.add((Grade, UNIV.inTerm, Literal("Summer 2020")))

# qres1 = g.query("""Select (Count (?s) as ?Count)
#     Where{
#         ?s ?p ?o
#
#     }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD})
#
#
# qres2=g.query(""" Select (Count (DISTINCT ?s) as ?s) (Count (DISTINCT ?c) as ?c) (Count (DISTINCT ?t) as ?t)
#     Where {
#         ?s rdf:type univ:Student.
#         ?c rdf:type univ:Course.
#         ?t rdf:type univ:Topic.
#     }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD})
#
# qres3 = g.query("""Select ?c ?n ?l
#     Where{
#         ?c rdf:type univ:Course.
#         ?c univ:hasTopic ?t.
#         ?t univ:topicName ?n.
#         ?t owl:sameAs ?l.
#     }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD, 'owl':OWL})
#
# qres4=g.query("""Select ?c ?v
#     Where{
#         stu:Joe univ:hasGrade ?g.
#         ?g univ:inCourse ?c.
#         ?g univ:hasGradeValue ?v.
#         Filter(?v != 'F').
#     }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD,'stu':s})
#
#
#
# qres5=g.query("""Select ?g ?s ?v
#     Where {
#         ?p univ:topicName 'library'.
#         ?c univ:hasTopic ?p.
#         ?g univ:inCourse ?c.
#         ?s univ:hasGrade ?g.
#         ?g univ:hasGradeValue ?v.
#         Filter(?v != 'F')
#     }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD})
#
#
# qres6=g.query("""Select DISTINCT ?n
#     Where {
#         stu:Joe univ:hasGrade ?g.
#         ?g univ:inCourse ?c.
#         ?g univ:hasGradeValue ?v.
#         ?c univ:hasTopic ?t.
#         ?t univ:topicName ?n.
#         Filter(?v != 'F')
#     }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD,'stu':s})
#
#
#
# print("******Query***********")
# for row in qres1:
#     print(row)
#
# print("******Query***********")
# for row in qres2:
#     print(row)
#
# print("******Query***********")
# for row in qres3:
#     print(row)
#
# print("******Query***********")
# for row in qres4:
#     print(row)
#
# print("******Query***********")
# for row in qres5:
#     print(row)
#
# print("******Query***********")
# for row in qres6:
#     print(row)

g.serialize(destination='knowledgeBase.nt', format='nt')
print(g.serialize(format="nt"))
