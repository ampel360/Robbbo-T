import xml.etree.ElementTree as ET
import sys
import coverage

def parse_xml(file_path):
    try:
        tree = ET.parse(file_path)
        return tree.getroot()
    except ET.ParseError as e:
        print(f"Error parsing XML file {file_path}: {e}")
        sys.exit(1)

def check_brex_compliance(brex_rules, data_module):
    violations = []
    for rule in brex_rules.findall('rule'):
        rule_id = rule.get('id')
        rule_description = rule.find('description').text
        rule_xpath = rule.find('xpath').text
        if not data_module.findall(rule_xpath):
            violations.append((rule_id, rule_description))
    return violations

def main(brex_file, data_module_file):
    brex_rules = parse_xml(brex_file)
    data_module = parse_xml(data_module_file)
    violations = check_brex_compliance(brex_rules, data_module)
    if violations:
        for violation in violations:
            print(f"BREX Violation: {violation[0]} - {violation[1]}")
        sys.exit(1)
    else:
        print("No BREX violations found.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python brex_check.py <brex_file> <data_module_file>")
        sys.exit(1)
    brex_file = sys.argv[1]
    data_module_file = sys.argv[2]
    main(brex_file, data_module_file)

# Unit tests
def test_parse_xml():
    root = parse_xml('test_data/test_brex.xml')
    assert root.tag == 'brex'

def test_check_brex_compliance():
    brex_rules = parse_xml('test_data/test_brex.xml')
    data_module = parse_xml('test_data/test_data_module.xml')
    violations = check_brex_compliance(brex_rules, data_module)
    assert len(violations) == 1
    assert violations[0][0] == 'RULE001'

# Code coverage analysis
if __name__ == "__main__":
    cov = coverage.Coverage()
    cov.start()

    # Run the main function with test data
    main('test_data/test_brex.xml', 'test_data/test_data_module.xml')

    cov.stop()
    cov.save()
    cov.report()
    cov.html_report(directory='coverage_report')
