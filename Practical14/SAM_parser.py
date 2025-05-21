import xml.sax
import time

class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_tag = ""
        self.namespace = ""
        self.id = ""
        self.name = ""
        self.is_a_count = 0

        self.max_is_a = {
            "molecular_function": {"max_count": 0, "terms": []},
            "biological_process": {"max_count": 0, "terms": []},
            "cellular_component": {"max_count": 0, "terms": []},
        }

        self.in_term = False
        self.buffer = ""

    def startElement(self, name, attrs):
        self.current_tag = name
        if name == "term":
            self.in_term = True
            self.namespace = ""
            self.id = ""
            self.name = ""
            self.is_a_count = 0

    def characters(self, content):
        if self.current_tag in {"id", "namespace", "name"}:
            self.buffer += content.strip()

    def endElement(self, name):
        if name == "id":
            self.id = self.buffer
        elif name == "name":
            self.name = self.buffer
        elif name == "namespace":
            self.namespace = self.buffer
        elif name == "is_a":
            self.is_a_count += 1
        elif name == "term":
            entry = self.max_is_a[self.namespace]
            if self.is_a_count > entry["max_count"]:
                entry["max_count"] = self.is_a_count
                entry["terms"] = [{"id": self.id, "name": self.name}]
            elif self.is_a_count == entry["max_count"]:
                entry["terms"].append({"id": self.id, "name": self.name})
        self.buffer = ""
start_time = time.time() #record the time

#create the parser
parser = xml.sax.make_parser()
handler = GOHandler()
parser.setContentHandler(handler)
parser.parse(r"C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical14\go_obo.xml")

#print the result
print("=== SAX Results ===")
for ns, info in handler.max_is_a.items():
    print(f"\nNamespace: {ns}")
    print(f"Max number of is_a terms: {info['max_count']}")
    for t in info["terms"]:
        print(f"GO ID: {t['id']}, Name: {t['name']}")

end_time = time.time()
sax_duration = end_time - start_time
print(f"\nSAX parsing took {sax_duration:.4f} seconds")

# SAX was faster than DOM (or vice versa), depending on results.
# SAX is more memory-efficient because it reads the XML incrementally.
# DOM is easier to implement but slower and more memory-hungry for large files.