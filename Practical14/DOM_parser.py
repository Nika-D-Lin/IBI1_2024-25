import xml.dom.minidom as minidom
import time

start_time = time.time()

#read the file
doc = minidom.parse(r"C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical14\go_obo.xml")

#get the terms
terms = doc.getElementsByTagName("term")

#reecord the the item is_a that has the most amount in namespace
#use the list to easily append the things in it, because there are more than one term that have the most is_a count
max_is_a = {
    "molecular_function": {"max_count": 0, "terms": []},
    "biological_process": {"max_count": 0, "terms": []},
    "cellular_component": {"max_count": 0, "terms": []},
}

#traverse term
for term in terms:
    namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue
    term_id = term.getElementsByTagName("id")[0].firstChild.nodeValue
    term_name = term.getElementsByTagName("name")[0].firstChild.nodeValue
    is_a_tags = term.getElementsByTagName("is_a")
    is_a_count = len(is_a_tags)

    if namespace in max_is_a:
        if is_a_count > max_is_a[namespace]["max_count"]:
            max_is_a[namespace]["max_count"] = is_a_count
            max_is_a[namespace]["terms"] = [{"id": term_id, "name": term_name}] #put the id and name as a group to easily append
        elif is_a_count == max_is_a[namespace]["max_count"]:
            max_is_a[namespace]["terms"].append({"id": term_id, "name": term_name})

#output
print("=== DOM Results ===")
for ns, info in max_is_a.items():
    print(f"\nNamespace: {ns}")
    print(f"Max number of is_a terms: {info['max_count']}")
    for t in info["terms"]:
        print(f"GO ID: {t['id']}, Name: {t['name']}")

end_time = time.time()
dom_duration = end_time - start_time
print(f"\nDOM parsing took {dom_duration:.4f} seconds")
