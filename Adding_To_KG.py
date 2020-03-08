from rdflib import Graph, Literal, Namespace, RDF, RDFS, BNode, URIRef
from rdflib.namespace import FOAF, RDFS, OWL
import csv
import spotlight

graph = Graph()
graph.parse("output.ttl", format="n3")
UNIV = Namespace("http://example.org/schema#")
g = Graph()
Concordia = BNode()
Joe = BNode()

g.add((Concordia, RDF.type, UNIV.University))
g.add((Concordia, UNIV.hasName, Literal("Concordia University")))
g.add((Concordia, UNIV.hasDBPediaLink, URIRef("http://dbpedia.org/page/Concordia_University")))
g.add((Joe, RDF.type, UNIV.Student))
g.add((Joe, FOAF.givenName, Literal("Joe")))
g.add((Joe, FOAF.familyName, Literal("Black")))
g.add((Joe, UNIV.hasID, Literal("40085534")))
g.add((Joe, FOAF.mbox, Literal("joeblack@gmail.com")))



with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row:
            x=URIRef(f"http://example.org/course/{row[0].split()[0]}+{row[0].split()[1]}")
            g.add((x, RDF.type, UNIV.Course))
            g.add((x, UNIV.courseName, Literal(row[1])))
            g.add((x, UNIV.courseSubject, Literal(row[0].split()[0])))
            g.add((x, UNIV.courseNo, Literal(row[0].split()[1])))
            if "prerequisite" in row[2].lower():
                desc = row[2][row[2].index(".")+1:]
                g.add((x, UNIV.courseDescription, Literal(desc)))
            else:
                g.add((x, UNIV.courseDescription, Literal(row[2])))

for s, p, o in g.triples((None, RDF.type, UNIV.Course)):
    Name = g.objects(s,UNIV.courseName)
    Description = g.objects(s, UNIV.courseDescription)
    to_search = f"{Name}. {Description}"
    try:
        annotations = spotlight.annotate('https://api.dbpedia-spotlight.org/en/annotate', to_search, confidence=0.8,
                                         support=20)
    except spotlight.SpotlightException:
        continue
    for i in annotations:
        if (None, OWL.sameAs, URIRef(i["URI"])) not in graph:
            x=URIRef(f"http://example.org/topic/{i['surfaceForm'].replace(' ','_')}")
            g.add((x, RDF.type, UNIV.topic))
            g.add((x, UNIV.TopicName, Literal(i['surfaceForm'].replace(' ','_'))))
            g.add((x, OWL.sameAs, URIRef(i['URI'])))
            g.add((s, UNIV.hasTopic, x))
        else:
            topic = g.subjects(OWL.sameAs,URIRef(i['URI']))
            g.add(s, UNIV.hasTopic, topic)

    print(g.objects(s, UNIV.hasTopic))
    break





a="COMP"
qres = g.query(
    """SELECT (COUNT (?s) AS ?count) 
       WHERE {
             ?s rdf:type univ:Course ;
             univ:courseSubject "COMP" ;
             univ:courseName ?name ;
             univ:courseDescription ?desc ;
             univ:courseNo ?no .
       }""", initNs={'foaf': FOAF, 'univ': UNIV, 'rdfs': RDFS, 'rdf': RDF})

for row in qres:
    print(row)