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
li=g.subjects(RDF.type, UNIV.Course)

with open("link.csv", "w") as csv_file:
    for i in li:
        t = g.objects(i, UNIV.hasTopic)
        for j in t:
            g.objects(j, UNIV.hasName)
            g.objects(j, OWL.sameAs)
            name = [x for x in g.objects(j, UNIV.topicName)][0]
            url = [y for y in g.objects(j, OWL.sameAs)][0]

            writer = csv.writer(csv_file, delimiter=",")
            writer.writerow((i, name, url))













