# import collections
# import sys
# import urllib
# import urllib.request
from urllib.parse import urlencode


# """Parse (absolute and relative) URLs.
#
# urlparse module is based upon the following RFC specifications.
#
# RFC 3986 (STD66): "Uniform Resource Identifiers" by T. Berners-Lee, R. Fielding
# and L.  Masinter, January 2005.
#
# RFC 2732 : "Format for Literal IPv6 Addresses in URL's by R.Hinden, B.Carpenter
# and L.Masinter, December 1999.
#
# RFC 2396:  "Uniform Resource Identifiers (URI)": Generic Syntax by T.
# Berners-Lee, R. Fielding, and L. Masinter, August 1998.
#
# RFC 2368: "The mailto URL scheme", by P.Hoffman , L Masinter, J. Zawinski, July 1998.
#
# RFC 1808: "Relative Uniform Resource Locators", by R. Fielding, UC Irvine, June
# 1995.
#
# RFC 1738: "Uniform Resource Locators (URL)" by T. Berners-Lee, L. Masinter, M.
# McCahill, December 1994
#
# RFC 3986 is considered the current standard and any future changes to
# urlparse module should conform with it.  The urlparse module is
# currently not entirely compliant with this RFC due to defacto
# scenarios for parsing, and for backward compatibility purposes, some
# parsing quirks from older RFCs are retained. The test cases in
# test_urlparse.py provides a good indicator of parsing behavior.
# """
#
# _ALWAYS_SAFE = frozenset(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#                          b'abcdefghijklmnopqrstuvwxyz'
#                          b'0123456789'
#                          b'_.-')
# _ALWAYS_SAFE_BYTES = bytes(_ALWAYS_SAFE)
# _safe_quoters = {}
#
#
# class Quoter(collections.defaultdict):
#     """A mapping from bytes (in range(0,256)) to strings.
#
#     String values are percent-encoded byte values, unless the key < 128, and
#     in the "safe" set (either the specified safe set, or default set).
#     """
#     # Keeps a cache internally, using defaultdict, for efficiency (lookups
#     # of cached keys don't call Python code at all).
#     def __init__(self, safe):
#         """safe: bytes object."""
#         self.safe = _ALWAYS_SAFE.union(safe)
#
#     def __repr__(self):
#         # Without this, will just display as a defaultdict
#         return "<%s %r>" % (self.__class__.__name__, dict(self))
#
#     def __missing__(self, b):
#         # Handle a cache miss. Store quoted string in cache and return.
#         res = chr(b) if b in self.safe else '%{:02X}'.format(b)
#         self[b] = res
#         return res
#
#
# def quote(string, safe='/', encoding=None, errors=None):
#     # urllib.parse.urlencode AKA urllib/parse.py
#     """quote('abc def') -> 'abc%20def'
#
#     Each part of a URL, e.g. the path info, the query, etc., has a
#     different set of reserved characters that must be quoted.
#
#     RFC 2396 Uniform Resource Identifiers (URI): Generic Syntax lists
#     the following reserved characters.
#
#     reserved    = ";" | "/" | "?" | ":" | "@" | "&" | "=" | "+" |
#                   "$" | ","
#
#     Each of these characters is reserved in some component of a URL,
#     but not necessarily in all of them.
#
#     By default, the quote function is intended for quoting the path
#     section of a URL.  Thus, it will not encode '/'.  This character
#     is reserved, but in typical usage the quote function is being
#     called on a path where the existing slash characters are used as
#     reserved characters.
#
#     string and safe may be either str or bytes objects. encoding and errors
#     must not be specified if string is a bytes object.
#
#     The optional encoding and errors parameters specify how to deal with
#     non-ASCII characters, as accepted by the str.encode method.
#     By default, encoding='utf-8' (characters are encoded with UTF-8), and
#     errors='strict' (unsupported characters raise a UnicodeEncodeError).
#     """
#     if isinstance(string, str):
#         if not string:
#             return string
#         if encoding is None:
#             encoding = 'utf-8'
#         if errors is None:
#             errors = 'strict'
#         string = string.encode(encoding, errors)
#     else:
#         if encoding is not None:
#             raise TypeError("quote() doesn't support 'encoding' for bytes")
#         if errors is not None:
#             raise TypeError("quote() doesn't support 'errors' for bytes")
#     return quote_from_bytes(string, safe)
#
#
# def quote_plus(string, safe='', encoding=None, errors=None):
#     # urllib.parse.urlencode AKA urllib/parse.py
#     """Like quote(), but also replace ' ' with '+', as required for quoting
#     HTML form values. Plus signs in the original string are escaped unless
#     they are included in safe. It also does not have safe default to '/'.
#     """
#     # Check if ' ' in string, where string may either be a str or bytes.  If
#     # there are no spaces, the regular quote will produce the right answer.
#     if ((isinstance(string, str) and ' ' not in string) or
#             (isinstance(string, bytes) and b' ' not in string)):
#         return quote(string, safe, encoding, errors)
#     if isinstance(safe, str):
#         space = ' '
#     else:
#         space = b' '
#     string = quote(string, safe + space, encoding, errors)
#     return string.replace(' ', '+')
#
#
# def quote_from_bytes(bs, safe='/'):
#     # urllib.parse.urlencode AKA urllib/parse.py
#     """Like quote(), but accepts a bytes object rather than a str, and does
#     not perform string-to-bytes encoding.  It always returns an ASCII string.
#     quote_from_bytes(b'abc def\x3f') -> 'abc%20def%3f'
#     """
#     if not isinstance(bs, (bytes, bytearray)):
#         raise TypeError("quote_from_bytes() expected bytes")
#     if not bs:
#         return ''
#     if isinstance(safe, str):
#         # Normalize 'safe' by converting to bytes and removing non-ASCII chars
#         safe = safe.encode('ascii', 'ignore')
#     else:
#         safe = bytes([c for c in safe if c < 128])
#     if not bs.rstrip(_ALWAYS_SAFE_BYTES + safe):
#         return bs.decode()
#     try:
#         quoter = _safe_quoters[safe]
#     except KeyError:
#         _safe_quoters[safe] = quoter = Quoter(safe).__getitem__
#     return ''.join([quoter(char) for char in bs])
#
#
# def urlencode(query,
#               do_sequences=False,
#               safe='',
#               encoding=None,
#               errors=None,
#               quote_via=quote_plus):
#     """Encode a dict or sequence of two-element tuples into a URL query string.
#
#     If any values in the query arg are sequences and do_sequences is true, each
#     sequence element is converted to a separate parameter.
#
#     If the query arg is a sequence of two-element tuples, the order of the
#     parameters in the output will match the order of parameters in the
#     input.
#
#     The components of a query arg may each be either a string or a bytes type.
#
#     The safe, encoding, and errors parameters are passed down to the function
#     specified by quote_via (encoding and errors only if a component is a str).
#     """
#
#     if hasattr(query, "items"):
#         query = query.items()
#     else:
#         # It's a bother at times that strings and string-like objects are
#         # sequences.
#         try:
#             # non-sequence items should not work with len()
#             # non-empty strings will fail this
#             if len(query) and not isinstance(query[0], tuple):
#                 raise TypeError
#             # Zero-length sequences of all types will get here and succeed,
#             # but that's a minor nit.  Since the original implementation
#             # allowed empty dicts that type of behavior probably should be
#             # preserved for consistency
#         except TypeError:
#             ty, va, tb = sys.exc_info()
#             raise TypeError("not a valid non-string sequence "
#                             "or mapping object").with_traceback(tb)
#
#     the_list = []
#     if not do_sequences:
#         for the_key, the_value in query:
#             if isinstance(the_key, bytes):
#                 the_key = quote_via(the_key, safe)
#             else:
#                 the_key = quote_via(str(the_key), safe, encoding, errors)
#
#             if isinstance(the_value, bytes):
#                 the_value = quote_via(the_value, safe)
#             else:
#                 the_value = quote_via(str(the_value), safe, encoding, errors)
#             the_list.append(the_key + '=' + the_value)
#     else:
#         for the_key, the_value in query:
#             if isinstance(the_key, bytes):
#                 the_key = quote_via(the_key, safe)
#             else:
#                 the_key = quote_via(str(the_key), safe, encoding, errors)
#
#             if isinstance(the_value, bytes):
#                 the_value = quote_via(the_value, safe)
#                 the_list.append(the_key + '=' + the_value)
#             elif isinstance(the_value, str):
#                 the_value = quote_via(the_value, safe, encoding, errors)
#                 the_list.append(the_key + '=' + the_value)
#             else:
#                 try:
#                     # Is this a sufficient test for sequence-ness?
#                     x = len(the_value)
#                 except TypeError:
#                     # not a sequence
#                     the_value = quote_via(str(the_value), safe, encoding, errors)
#                     the_list.append(the_key + '=' + the_value)
#                 else:
#                     # loop over the sequence
#                     for elt in the_value:
#                         if isinstance(elt, bytes):
#                             elt = quote_via(elt, safe)
#                         else:
#                             elt = quote_via(str(elt), safe, encoding, errors)
#                         the_list.append(the_key + '=' + elt)
#     return '&'.join(the_list)


DEFAULT_URI_SCHEME = "https"


def build_url_string(uri_scheme = None,
                     uri_authority = None,
                     uri_path = None,
                     uri_query = None,
                     uri_fragment = None,
                     query_string_parameters = None):
    """
    https://tools.ietf.org/html/rfc3986#section-3
    URI Components: scheme, authority, path, query, fragment
    uri_query and query_parameter_string are mutually-exclusive.
    :param uri_scheme: [optional] (Default: "https")
    :type uri_scheme: str
    :param uri_authority: [required]
    :type uri_authority: str
    :param uri_path: [required]
    :type uri_path: str
    :param uri_query: [optional] (Default: None)
    :type uri_query: str
    :param uri_fragment: [optional] (Default: None)
    :type uri_fragment: str
    :param query_string_parameters:
    :type query_string_parameters: dict
    :return:
    """

    # TODO(JamesBalcomb): raise ValueError if missing required parameters
    if uri_scheme is None:
        # del uri_scheme
        # UnboundLocalError: local variable 'uri_scheme' referenced before assignment
        pass
    if uri_authority is None:
        raise ValueError("uri_authority? Nein danke!")
    if uri_path is None:
        raise ValueError("uri_path? Nein danke!")
    if uri_query is None:
        # del uri_query
        # UnboundLocalError: local variable 'uri_query' referenced before assignment
        pass
    if uri_fragment is None:
        # del uri_fragment
        # UnboundLocalError: local variable 'uri_fragment' referenced before assignment
        pass
    if query_string_parameters is None:
        # del query_string_parameters
        # UnboundLocalError: local variable 'query_string_parameters' referenced before assignment
        pass

    if uri_query and query_string_parameters:
        print("Are you trying to get a rise out of me, Agent Kujan")
        print("PS. What shall we do if you pass a query /and/ query_string_parameters?")

    if query_string_parameters is not None:
        # NOTE: urlencode does not provide the URI query separator "?"
        # uri_query = urllib.parse.urlencode(query_string_parameters)
        urlencode(query_string_parameters)

    # DEFAULT_URI_SCHEME = "https"
    # DEFAULT_URI_AUTHORITY = "maps.googleapis.com"
    # DEFAULT_URI_PATH_BASE = "/maps/api/place/"

    uri_scheme = DEFAULT_URI_SCHEME if uri_scheme is None else uri_scheme
    # uri_authority = DEFAULT_URI_AUTHORITY if uri_authority is None else uri_authority
    # uri_path = DEFAULT_URI_PATH_BASE if uri_path is None else uri_path

    url_string = "{uri_scheme}://{uri_authority}{uri_path}".format(uri_scheme = uri_scheme,
                                                                   uri_authority = uri_authority,
                                                                   uri_path = uri_path)

    if uri_query:
        if not uri_query.startswith("?"):
            uri_query = "?" + uri_query
        url_string = url_string + uri_query

    if uri_fragment:
        if not uri_fragment.startswith("#"):
            uri_fragment = "#" + uri_fragment
        url_string = url_string + uri_fragment

    return url_string
