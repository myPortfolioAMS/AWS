# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class MediaProcessorList(ListResource):

    def __init__(self, version):
        """
        Initialize the MediaProcessorList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.media.v1.media_processor.MediaProcessorList
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorList
        """
        super(MediaProcessorList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/MediaProcessors'.format(**self._solution)

    def create(self, extension, extension_context,
               extension_environment=values.unset, status_callback=values.unset,
               status_callback_method=values.unset, max_duration=values.unset):
        """
        Create the MediaProcessorInstance

        :param unicode extension: The Media Extension name or URL
        :param unicode extension_context: The Media Extension context
        :param dict extension_environment: The Media Extension environment
        :param unicode status_callback: The URL to send MediaProcessor event updates to your application
        :param unicode status_callback_method: The HTTP method Twilio should use to call the `status_callback` URL
        :param unicode max_duration: Maximum MediaProcessor duration in minutes

        :returns: The created MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        """
        data = values.of({
            'Extension': extension,
            'ExtensionContext': extension_context,
            'ExtensionEnvironment': serialize.object(extension_environment),
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'MaxDuration': max_duration,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return MediaProcessorInstance(self._version, payload, )

    def stream(self, order=values.unset, status=values.unset, limit=None,
               page_size=None):
        """
        Streams MediaProcessorInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param MediaProcessorInstance.Order order: The sort order of the list
        :param MediaProcessorInstance.Status status: Status to filter by
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.media.v1.media_processor.MediaProcessorInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(order=order, status=status, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, order=values.unset, status=values.unset, limit=None,
             page_size=None):
        """
        Lists MediaProcessorInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param MediaProcessorInstance.Order order: The sort order of the list
        :param MediaProcessorInstance.Status status: Status to filter by
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.media.v1.media_processor.MediaProcessorInstance]
        """
        return list(self.stream(order=order, status=status, limit=limit, page_size=page_size, ))

    def page(self, order=values.unset, status=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MediaProcessorInstance records from the API.
        Request is executed immediately

        :param MediaProcessorInstance.Order order: The sort order of the list
        :param MediaProcessorInstance.Status status: Status to filter by
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorPage
        """
        data = values.of({
            'Order': order,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return MediaProcessorPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MediaProcessorInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return MediaProcessorPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a MediaProcessorContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.media.v1.media_processor.MediaProcessorContext
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorContext
        """
        return MediaProcessorContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a MediaProcessorContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.media.v1.media_processor.MediaProcessorContext
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorContext
        """
        return MediaProcessorContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Media.V1.MediaProcessorList>'


class MediaProcessorPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MediaProcessorPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.media.v1.media_processor.MediaProcessorPage
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorPage
        """
        super(MediaProcessorPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MediaProcessorInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        """
        return MediaProcessorInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Media.V1.MediaProcessorPage>'


class MediaProcessorContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the MediaProcessorContext

        :param Version version: Version that contains the resource
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.media.v1.media_processor.MediaProcessorContext
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorContext
        """
        super(MediaProcessorContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/MediaProcessors/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the MediaProcessorInstance

        :returns: The fetched MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MediaProcessorInstance(self._version, payload, sid=self._solution['sid'], )

    def update(self, status):
        """
        Update the MediaProcessorInstance

        :param MediaProcessorInstance.UpdateStatus status: The status of the MediaProcessor

        :returns: The updated MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        """
        data = values.of({'Status': status, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return MediaProcessorInstance(self._version, payload, sid=self._solution['sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Media.V1.MediaProcessorContext {}>'.format(context)


class MediaProcessorInstance(InstanceResource):

    class Status(object):
        FAILED = "failed"
        STARTED = "started"
        ENDED = "ended"

    class UpdateStatus(object):
        ENDED = "ended"

    class Order(object):
        ASC = "asc"
        DESC = "desc"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the MediaProcessorInstance

        :returns: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        """
        super(MediaProcessorInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'sid': payload.get('sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'extension': payload.get('extension'),
            'extension_context': payload.get('extension_context'),
            'status': payload.get('status'),
            'url': payload.get('url'),
            'ended_reason': payload.get('ended_reason'),
            'status_callback': payload.get('status_callback'),
            'status_callback_method': payload.get('status_callback_method'),
            'max_duration': deserialize.integer(payload.get('max_duration')),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: MediaProcessorContext for this MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorContext
        """
        if self._context is None:
            self._context = MediaProcessorContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def extension(self):
        """
        :returns: The Media Extension name or URL
        :rtype: unicode
        """
        return self._properties['extension']

    @property
    def extension_context(self):
        """
        :returns: The Media Extension context
        :rtype: unicode
        """
        return self._properties['extension_context']

    @property
    def status(self):
        """
        :returns: The status of the MediaProcessor
        :rtype: MediaProcessorInstance.Status
        """
        return self._properties['status']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def ended_reason(self):
        """
        :returns: The reason why a MediaProcessor ended
        :rtype: unicode
        """
        return self._properties['ended_reason']

    @property
    def status_callback(self):
        """
        :returns: The URL to which Twilio will send MediaProcessor event updates
        :rtype: unicode
        """
        return self._properties['status_callback']

    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method Twilio should use to call the `status_callback` URL
        :rtype: unicode
        """
        return self._properties['status_callback_method']

    @property
    def max_duration(self):
        """
        :returns: Maximum MediaProcessor duration in seconds
        :rtype: unicode
        """
        return self._properties['max_duration']

    def fetch(self):
        """
        Fetch the MediaProcessorInstance

        :returns: The fetched MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        """
        return self._proxy.fetch()

    def update(self, status):
        """
        Update the MediaProcessorInstance

        :param MediaProcessorInstance.UpdateStatus status: The status of the MediaProcessor

        :returns: The updated MediaProcessorInstance
        :rtype: twilio.rest.media.v1.media_processor.MediaProcessorInstance
        """
        return self._proxy.update(status, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Media.V1.MediaProcessorInstance {}>'.format(context)
