import json
import re
import unittest

###############################################################
# PROGRAM
###############################################################

try:
    file_path = 'amazon.json'
    with open(file_path, 'r') as file:
        data = json.load(file)

    policy_name = data["PolicyName"]
    policy_document = data["PolicyDocument"]

    validation_flag = True
except:
    policy_name=""
    policy_document=""
    validation_flag = False


def validation_policy_name(policy_n):
    global validation_flag
    try:
        pattern = r"[\w+=,.@-]+"
        if not policy_n or len(policy_n) > 128 or policy_n.isspace() or not re.match(pattern, policy_n):
            validation_flag = False
    except:
        validation_flag = False


def validate_policy_document(policy_d):
    try:
        global validation_flag
        version = policy_d["Version"]

        if version is None or version.isspace():
            validation_flag = False

        statements = policy_d["Statement"]

        if statements is None:
            validation_flag = False

        for statement in statements:
            if all(key in statement and statement[key] and statement["Resource"] == "*" and (
                    isinstance(statement[key], list) or statement[key].strip() != "") for key in
                   ["Sid", "Effect", "Action", "Resource"]):
                pass
            else:
                validation_flag = False
    except:
        validation_flag = False


def solution(policy_n, policy_d):
    validation_policy_name(policy_n)
    validate_policy_document(policy_d)
    if (validation_flag == True):
        return False
    else:
        return True  # Method returns true when in resoursce lacks * or is wrongly formatted


def setValidationFlag():  # For test purpose
    global validation_flag
    validation_flag = True


try:
    print(solution(policy_name, policy_document))
except:
    print("Something is wrong...")


###############################################################
# TESTS
###############################################################


class TestSolution(unittest.TestCase):
    def setUp(self):
        # Data for testing
        self.valid_policy_name = "lala"
        self.invalid_policy_name = "$%^&*()"
        self.policy_document = {
            "Version": "2012-10-17",
            "Statement": [
                {"Sid": "1", "Effect": "Allow", "Action": ["iam:ListRoles", "iam:ListUsers"], "Resource": "*"}
            ]
        }


    def test_valid_solution(self):
        # Test for valid policy name and document
        setValidationFlag()
        self.assertFalse(solution(self.valid_policy_name, self.policy_document))

    ####Tests for policy_name
    def test_invalid_policy_name(self):
        # Test for invalid policy name
        setValidationFlag()
        self.assertTrue(solution(self.invalid_policy_name, self.policy_document))

    def test_policy_name_too_long(self):
        setValidationFlag()
        self.invalid_policy_name = "a" * 129
        self.assertTrue(solution(self.invalid_policy_name, policy_document))

    def test_policy_name_128(self):
        setValidationFlag()
        self.policy_name = "a" * 128
        self.assertFalse(solution(self.policy_name, self.policy_document))

    def test_policy_name_0(self):
        setValidationFlag()
        self.invalid_policy_name = ""
        self.assertTrue(solution(self.invalid_policy_name, policy_document))

    ####Tests for policy documents
    def test_invalid_policy_document(self):
        # Test for invalid policy document (missing version)
        setValidationFlag()
        policy_document = {"Statement": [
            {"Sid": "1", "Effect": "Allow", "Action": ["iam:ListRoles", "iam:ListUsers"], "Resource": "*"}]}
        self.assertTrue(solution(self.valid_policy_name, policy_document))

    def test_invalid_resource(self):
        # Test for invalid resource (missing *)
        setValidationFlag()
        policy_document = {"Version": "2012-10-17", "Statement": [
            {"Sid": "1", "Effect": "Allow", "Action": ["iam:ListRoles", "iam:ListUsers"], "Resource": "xd"}]}
        self.assertTrue(solution(self.valid_policy_name, policy_document))

    def test_empty_Action(self):
        # Test for invalid Action
        setValidationFlag()
        policy_document = {"Version": "2012-10-17",
                           "Statement": [{"Sid": "1", "Effect": "Allow", "Action": [], "Resource": "*"}]}
        self.assertTrue(solution(self.valid_policy_name, policy_document))

    def test_no_effect(self):
        # Test for lack of effect
        setValidationFlag()
        policy_document = {"Version": "2012-10-17", "Statement": [{"Sid": "1", "Action": [], "Resource": "*"}]}
        self.assertTrue(solution(self.valid_policy_name, policy_document))

    def test_invalid_resource_and_name(self):
        # invalid resource and name
        setValidationFlag()
        policy_document = {"Version": "2012-10-17", "Statement": [{"Sid": "1"}]}
        self.assertTrue(solution(self.invalid_policy_name, policy_document))

    def test_invalid_resource_and_name2(self):
        setValidationFlag()
        self.assertTrue(solution(None, None))

    def test_double_asteriks(self):
        setValidationFlag()
        policy_document = {"Version": "2012-10-17", "Statement": [
            {"Sid": "1", "Effect": "Allow", "Action": ["iam:ListRoles", "iam:ListUsers"], "Resource": "**"}]}
        self.assertTrue(solution(self.invalid_policy_name, policy_document))


if __name__ == '__main__':
    unittest.main()
