import sys
from rdflib import Graph
from pyshacl import validate
import os

def run_validation(data_path):
    shapes_path = os.path.expanduser('~/the-library/peculiar-shelf/shapes/library_shapes.shacl')
    
    data_graph = Graph()
    shapes_graph = Graph()
    
    try:
        data_graph.parse(os.path.expanduser(data_path), format='turtle')
        shapes_graph.parse(shapes_path, format='turtle')
    except Exception as e:
        print(f"❌ PARSE ERROR: {e}")
        sys.exit(1)

    # THE CORE ENGINE: This is where we check the logic
    conforms, results_graph, results_text = validate(
        data_graph,
        shacl_graph=shapes_graph,
        inference='rdfs',
        abort_on_first=False,
        serialize_report_graph=True
    )

    if conforms:
        print("\n🏆 DETERMINISTIC VALIDITY CONFIRMED: The shelf meets Library standards.")
    else:
        print("\n🚨 VALIDATION BREACH DETECTED 🚨")
        print(results_text)
        sys.exit(1) # Force the script to fail

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else '~/the-peculiar-library/ontology/padi-v3.ttl'
    run_validation(target)
