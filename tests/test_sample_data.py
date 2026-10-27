import os
import json
import pytest


def test_sample_document_exists():
    """Test that the sample document exists."""
    doc_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_documents', 'library_policy.txt')
    assert os.path.exists(doc_path), "Sample document library_policy.txt does not exist"


def test_sample_document_contains_expected_facts():
    """Test that the sample document contains the expected facts."""
    doc_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_documents', 'library_policy.txt')
    with open(doc_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for the 6 expected facts
    assert "9 AM to 5 PM" in content, "Missing operating hours"
    assert "Monday through Friday" in content, "Missing operating days"
    assert "four books" in content, "Missing book borrowing limit"
    assert "14 days" in content, "Missing loan period"
    assert "closed on Sundays" in content, "Missing Sunday closure"
    assert "college ID" in content, "Missing ID requirement"
    assert "20 computers" in content, "Missing computer count"


def test_test_cases_json_exists():
    """Test that the test cases JSON file exists."""
    json_path = os.path.join(os.path.dirname(__file__), '..', 'evaluation', 'test_cases.json')
    assert os.path.exists(json_path), "Test cases JSON file does not exist"


def test_test_cases_json_structure():
    """Test that the test cases JSON has the correct structure and all three verdict categories."""
    json_path = os.path.join(os.path.dirname(__file__), '..', 'evaluation', 'test_cases.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    assert 'test_cases' in data, "Missing 'test_cases' key in JSON"
    assert len(data['test_cases']) == 9, f"Expected 9 test cases, found {len(data['test_cases'])}"
    
    # Check that all three verdict categories are present
    verdicts = {case['expected_verdict'] for case in data['test_cases']}
    assert 'Supported' in verdicts, "Missing 'Supported' verdict category"
    assert 'Contradicted' in verdicts, "Missing 'Contradicted' verdict category"
    assert 'Insufficient Evidence' in verdicts, "Missing 'Insufficient Evidence' verdict category"
    
    # Verify each test case has required fields
    for case in data['test_cases']:
        assert 'claim_id' in case, f"Missing 'claim_id' in test case {case.get('claim_id', 'unknown')}"
        assert 'claim' in case, f"Missing 'claim' in test case {case.get('claim_id', 'unknown')}"
        assert 'expected_verdict' in case, f"Missing 'expected_verdict' in test case {case.get('claim_id', 'unknown')}"
        assert 'explanation' in case, f"Missing 'explanation' in test case {case.get('claim_id', 'unknown')}"
