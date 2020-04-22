from rdflib import Graph, Literal, Namespace, RDF, RDFS, BNode, URIRef
from rdflib.namespace import FOAF, RDFS, OWL, XSD

import csv
import spotlight
import time
g = Graph()
g.parse("knowledgeBase.nt", format="nt")
UNIV = Namespace("http://example.org/schema#")
u = Namespace("http://example.org/university/")
s = Namespace("http://example.org/student/")

q1 = open("q1-out.ttl", "a")
q2 = open("q2-out.ttl", "a")
q3 = open("q3-out.ttl", "a")
q4 = open("q4-out.ttl", "a")
q5 = open("q5-out.ttl", "a")
q6 = open("q6-out.ttl", "a")



qres1 = g.query("""Select ?c
    Where{
        ?c rdf:type univ:Course.
        ?c univ:courseSubject 'FMST'.
    }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD})



# qres1 = g.query("""Select (Count (?s) as ?Count)
#     Where{
#         ?s ?p ?o
#
#     }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD})

# print("******Query***********")
# for row in qres1:
#     print(row)
#
# for row in qres1:
#     q1.write(f'{row["Count"]} .')
#
# qres3 = g.query("""Select ?c ?n ?l
#     Where{
#         ?c rdf:type univ:Course.
#         ?c univ:hasTopic ?t.
#         ?t univ:topicName ?n.
#         ?t owl:sameAs ?l.
#     }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD, 'owl':OWL})
#
# print("******Query***********")
# for row in qres3:
#     print(row)
# for row in qres3:
#     q3.write(f'<{row["c"]}> {row["n"]} <{row["l"]}>.\n')
#
#
#
#
# qres4 = g.query("""Select ?c ?v
#     Where{
#         stu:Aman univ:hasGrade ?g.
#         ?g univ:inCourse ?c.
#         ?g univ:hasGradeValue ?v.
#         Filter(?v != 'F').
#     }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD,'stu':s})
#
# print("******Query***********")
# for row in qres4:
#     print(row)
#
# for row in qres4:
#     q4.write(f'<{row["c"]}>  {row["v"]}.\n')
#
#
#
# qres5 = g.query("""Select ?g ?s ?v
#     Where {
#         ?p univ:topicName 'biopsychosocial'.
#         ?c univ:hasTopic ?p.
#         ?g univ:inCourse ?c.
#         ?s univ:hasGrade ?g.
#         ?g univ:hasGradeValue ?v.
#         Filter(?v != 'F')
#     }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD})
#
# print("******Query***********")
# for row in qres5:
#     print(row)
#
# for row in qres5:
#     q5.write(f'<{row["g"]}> <{row["s"]}> {row["v"]}.\n')
#
#
# qres6 = g.query("""Select DISTINCT ?n
#     Where {
#         stu:Joe univ:hasGrade ?g.
#         ?g univ:inCourse ?c.
#         ?g univ:hasGradeValue ?v.
#         ?c univ:hasTopic ?t.
#         ?t univ:topicName ?n.
#         Filter(?v != 'F')
#     }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD,'stu':s})
#
# print("******Query***********")
# for row in qres6:
#     print(row)
#
# for row in qres6:
#     q6.write(f'{row["n"]}.\n')



# qres2 = g.query(""" Select (Count (DISTINCT ?s) as ?s) (Count (DISTINCT ?c) as ?c) (Count (DISTINCT ?t) as ?t)
#     Where {
#         {?s rdf:type univ:Student.}
#         {?c rdf:type univ:Course.}
#         {?t rdf:type univ:Topic.}
#     }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD})
#
# print("******Query***********")
# print("1st query done")
# print(type(qres2))
# for row in qres2:
#     print("hi")
#     print(row["s"], row['c'], row['t'])
#
# for row in qres2:
#     q2.write(f'{row["s"]}  {row["c"]}  {row["t"]}.\n')









# qres2=g.query(""" Select (Count (DISTINCT ?s) as ?s)
#     Where {
#         ?s rdf:type univ:Student.
#     }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD})
#
# print("******Query***********")
# for row in qres2:
#     print(row)
#
#
qres7 = g.query(""" SELECT (COUNT (DISTINCT ?c) as ?c)
    WHERE {
        ?c rdf:type univ:Course.
    }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD})

print("******Query***********")
for row in qres7:
    print(row)
print(type(qres7))
print(qres7.serialize(format='nt'))
#
# qres8 = g.query(""" Select (Count (DISTINCT ?t) as ?t)
#     Where {
#         ?t rdf:type univ:Topic.
#     }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF, 'xsd': XSD})
#
# print("******Query***********")
# for row in qres8:
#     print(row)














