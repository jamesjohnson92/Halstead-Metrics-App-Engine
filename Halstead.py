import sys
import webapp2
import re
import math
RESERVED_WORDS = [
    "alignas", "alignof", "and", "and_eq", "asm", "auto", "bitand", "bitor",
    "bool", "break", "case", "catch", "char", "char16_t", "char32_t", "class",
    "compl", "const", "constexpr", "const_cast", "continue", "decltype",
    "default", "delete", "do", "double", "dynamic_cast", "else", "enum",
    "explicit", "export", "extern", "false", "float", "for", "friend", "goto",
    "if", "inline", "int", "long", "mutable", "namespace", "new", "noexcept",
    "not", "not_eq", "nullptr", "operator", "or", "or_eq", "private",
    "protected", "public", "register", "reinterpret_cast", "return", "short",
    "signed", "sizeof", "static", "static_assert", "static_cast", "struct",
    "switch", "template", "this", "thread_local", "throw", "true", "try",
    "typedef", "typeid", "typename", "union", "unsigned", "using", "virtual",
    "void", "volatile", "wchar_t", "while", "xor", "xor_eq"
    ]

PURE_OPERATORS = [
    "::", "++", "--", "(", ")", "[", "]", ".", "->", "++", "--", "+", "-",
    "!", "~", "*", "&", ".*", "->*", "*", "/", "%", "+", "-", "<<", ">>",
    "<", "<=", ">", ">=", "==", "!=", "&", "^", "|", "&&", "||", "?:", "=",
    "+=", "-=", "*=", "/=", "%=", "<<=", ">>=", "&=", "^=", "|=", ",", "\"",
    "\'", "\\", ";", "{", "}"
    ]


class Halstead:

	def __init__(self,content):
	  self.operands = []
	  self.operators = []
	  self.content = content
	  self.operatorsCount = 0
	  self.operandsCount = 0

	  for line in self.content:
	    self.analyzeLine(line)
          self.filterFunctionNames()

	def analyzeLine(self,line):
	  for token in line.split():
	    self.splitEachToken(token)


	def splitEachToken(self,token):
	  filter = token
	  while filter:
	    filter = self.analyzeToken(filter)


	def analyzeToken(self,token):
	  lenOfToken = len(token)
	  for operator in PURE_OPERATORS:
	    if token.startswith(operator):
	      self.operatorsCount += 1
	      self.operators.append(operator)
	      return token[len(operator):]

	    if operator in token:
	      lenOfToken = min(lenOfToken,token.find(operator))

	  identifier = token[:lenOfToken]

	  for keyword in RESERVED_WORDS:
	    if identifier == keyword:
	      self.operators.append(keyword)
	      self.operatorsCount += 1
	      return token[lenOfToken:]

	  self.operandsCount += 1
	  self.operands.append(identifier)
	  return token[lenOfToken:]


	def getUniqueOperators(self):
	   return set(self.operators)

	def getUniqueOperands(self):
	   return set(self.operands)

	def getNoUniqueOperators(self):
	  return len(set(self.operators))

	def getNoUniqueOperands(self):
	  return len(set(self.operands))

	def getAllOperators(self):
	 return self.operators

	def getAllOperands(self):
	 return self.operands

	def getNoAllOperators(self):
	 return len(self.operators)

	def getNoAllOperands(self):
	 return len(self.operands)

	def getVocabularySize(self):
	  return self.getNoUniqueOperators()+self.getNoUniqueOperands()

	def getProgramLength(self):
	  return self.getNoAllOperands()+self.getNoAllOperators()

        def filterFunctionNames(self):
            content = ''.join(self.content)
            rproc = r"((?<=[\s:~])(\w+)\s*\(([\w\s,<>\[\].=&':/*]*?)\)\s*(const)?\s*(?={))"
	    cppwords = ['if', 'while', 'do', 'for', 'switch']
	    procs = [(i.group(2), i.group(3)) for i in re.finditer(rproc, content) \
	     if i.group(2) not in cppwords]
            for element in self.operands:
                for name in procs:
                    if element in name:
                        self.operands.remove(element)

        def getVolume(self):
            return self.getNoAllOperands()*math.log(self.getProgramLength(),2)

        def getDifficulty(self):
            return (self.getNoUniqueOperators() / 2) * (self.getNoAllOperands() / self.getNoUniqueOperands())


        def getEffort(self):
            return self.getVolume() * self.getDifficulty()









