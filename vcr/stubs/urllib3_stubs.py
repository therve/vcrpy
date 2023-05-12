"""Stubs for urllib3"""

try:
    from urllib3.connectionpool import HTTPConnection, VerifiedHTTPSConnection
except ImportError:
    from urllib3.connection import HTTPConnection, VerifiedHTTPSConnection

from urllib3.response import HTTPResponse

from ..stubs import VCRHTTPConnection, VCRHTTPSConnection

# urllib3 defines its own HTTPConnection classes. It includes some polyfills
# for newer features missing in older pythons.


class VCRRequestsHTTPConnection(VCRHTTPConnection, HTTPConnection):
    _baseclass = HTTPConnection

    def getresponse(self, _=False, **kwargs):
        httplib_response = super().getresponse()  # VCRHTTPConnectio
        return HTTPResponse(
            body=httplib_response,
            headers=httplib_response.getheaders(),
            status=httplib_response.status,
            version=httplib_response.version,
            reason=httplib_response.reason,
            original_response=httplib_response,
            request_method=self._vcr_request.method,
            request_url=self._vcr_request.uri,
        )


class VCRRequestsHTTPSConnection(VCRHTTPSConnection, VerifiedHTTPSConnection):
    _baseclass = VerifiedHTTPSConnection

    def getresponse(self, _=False, **kwargs):
        httplib_response = super().getresponse()  # VCRHTTPConnectio
        return HTTPResponse(
            body=httplib_response,
            headers=httplib_response.getheaders(),
            status=httplib_response.status,
            version=httplib_response.version,
            reason=httplib_response.reason,
            original_response=httplib_response,
            request_method=self._vcr_request.method,
            request_url=self._vcr_request.uri,
        )
