def correctFormatting(termDict):
  """ Return a bool denoting whether the input dict has the necessary keys for entry into db as a term

  :param termDict: a dict to be used as a new term
  :type dbConnector: dict

  :rtype: bool
  """
  if not isinstance(termDict, dict):
    return False

  for key in ['term_string', 'definition', 'examples']:
    if not isinstance(termDict.get(key, False), basestring):
      return False

  return True
