from xml.dom import minidom
from xml.sax import make_parser, ContentHandler
import datetime

def parse_with_dom(file_path):
    # 记录开始时间
    start_time = datetime.datetime.now()
    
    # 加载 XML 文件
    doc = minidom.parse(file_path)
    
    # 获取所有的 <term> 节点
    terms = doc.getElementsByTagName("term")
    
    # 初始化存储结构
    ontology_depth = {
        "molecular_function": {"term": None, "max_is_a": 0},
        "biological_process": {"term": None, "max_is_a": 0},
        "cellular_component": {"term": None, "max_is_a": 0}
    }
    
    # 遍历每个 <term> 节点
    for term in terms:
        # 获取 <namespace> 的值
        namespace = term.getElementsByTagName("namespace")[0].firstChild.data
        
        # 获取所有的 <is_a> 元素
        is_a_elements = term.getElementsByTagName("is_a")
        
        # 统计 <is_a> 元素的数量
        num_is_a = len(is_a_elements)
        
        # 如果当前术语属于某个本体，并且它的 <is_a> 数量大于之前记录的最大值，则更新记录
        if namespace in ontology_depth:
            if num_is_a > ontology_depth[namespace]["max_is_a"]:
                ontology_depth[namespace]["term"] = term.getElementsByTagName("id")[0].firstChild.data
                ontology_depth[namespace]["max_is_a"] = num_is_a
    
    # 记录结束时间
    end_time = datetime.datetime.now()
    
    # 返回结果和执行时间
    return ontology_depth, (end_time - start_time).total_seconds()

if __name__ == "__main__":
    file_path = r"C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical14\go_obo.xml"
    results, time_taken = parse_with_dom(file_path)
    print("DOM Parsing Results:")
    for ontology, data in results.items():
        print(f"{ontology}: {data['term']} with {data['max_is_a']} <is_a> elements")
    print(f"Time taken: {time_taken} seconds")

class GOHandler(ContentHandler):
    def __init__(self):
        self.current_tag = ""  # 当前正在处理的标签
        self.current_term = {}  # 当前正在处理的术语
        self.ontology_depth = {
            "molecular_function": {"term": None, "max_is_a": 0},
            "biological_process": {"term": None, "max_is_a": 0},
            "cellular_component": {"term": None, "max_is_a": 0}
        }
    
    def startElement(self, tag, attributes):
        # 当遇到一个新标签时，记录当前标签
        self.current_tag = tag
        
        # 如果遇到 <term> 标签，初始化当前术语
        if tag == "term":
            self.current_term = {"is_a_count": 0}
    
    def endElement(self, tag):
        # 当结束一个标签时，检查是否是 <term> 标签
        if tag == "term":
            # 获取当前术语的 <namespace> 和 <is_a> 数量
            namespace = self.current_term.get("namespace")
            num_is_a = self.current_term["is_a_count"]
            
            # 如果当前术语属于某个本体，并且它的 <is_a> 数量大于之前记录的最大值，则更新记录
            if namespace in self.ontology_depth:
                if num_is_a > self.ontology_depth[namespace]["max_is_a"]:
                    self.ontology_depth[namespace]["term"] = self.current_term["id"]
                    self.ontology_depth[namespace]["max_is_a"] = num_is_a
    
    def characters(self, content):
        # 当遇到文本内容时，根据当前标签进行处理
        if self.current_tag == "id":
            self.current_term["id"] = content
        elif self.current_tag == "namespace":
            self.current_term["namespace"] = content
        elif self.current_tag == "is_a":
            self.current_term["is_a_count"] += 1
    
    def get_results(self):
        # 返回最终结果
        return self.ontology_depth

def parse_with_sax(file_path):
    # 记录开始时间
    start_time = datetime.datetime.now()
    
    # 创建解析器
    parser = make_parser()
    
    # 创建处理器
    handler = GOHandler()
    
    # 将处理器绑定到解析器
    parser.setContentHandler(handler)
    
    # 解析文件
    parser.parse(file_path)
    
    # 记录结束时间
    end_time = datetime.datetime.now()
    
    # 返回结果和执行时间
    return handler.get_results(), (end_time - start_time).total_seconds()

if __name__ == "__main__":
    file_path = r"C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical14\go_obo.xml"
    results, time_taken = parse_with_sax(file_path)
    print("SAX Parsing Results:")
    for ontology, data in results.items():
        print(f"{ontology}: {data['term']} with {data['max_is_a']} <is_a> elements")
    print(f"Time taken: {time_taken} seconds")

if __name__ == "__main__":
    file_path = r"C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical14\go_obo.xml"
    
    # DOM 解析
    dom_results, dom_time = parse_with_dom(file_path)
    print("DOM Parsing Results:")
    for ontology, data in dom_results.items():
        print(f"{ontology}: {data['term']} with {data['max_is_a']} <is_a> elements")
    print(f"Time taken: {dom_time} seconds")
    
    # SAX 解析
    sax_results, sax_time = parse_with_sax(file_path)
    print("SAX Parsing Results:")
    for ontology, data in sax_results.items():
        print(f"{ontology}: {data['term']} with {data['max_is_a']} <is_a> elements")
    print(f"Time taken: {sax_time} seconds")
    
    # 比较两种方法的执行时间
    if dom_time < sax_time:
        print("DOM was faster.")
    else:
        print("SAX was faster.")