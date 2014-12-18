import types
from metis import app
from metis.core.query.operator import DataAccess
from metis.core.query.operator import Operator
from pykronos.client import KronosClient

class KronosSource(DataAccess):
  def __init__(self, source, stream=None, start_time=None, end_time=None,
               namespace=None, **kwargs):
    self._config = app.config['DATA_SOURCES'][source]
    self._host = self._config['url']
    self.type = Operator.Type.DATA_ACCESS
    self.source = source
    self.stream = stream
    self.start_time = start_time
    self.end_time = end_time
    self.namespace = namespace
    super(KronosSource, self).__init__(**kwargs)

  @classmethod
  def parse(cls, _dict):
    kronos_source = KronosSource(**_dict)

    # TODO(usmanm): Improve validation.
    assert isinstance(kronos_source._config, types.DictType)
    assert isinstance(kronos_source._host, types.StringTypes)
    assert isinstance(kronos_source.source, types.StringTypes)
    assert (kronos_source.stream is None or
            isinstance(kronos_source.stream, types.StringTypes))
    assert (kronos_source.start_time is None or
            isinstance(kronos_source.start_time, int))
    assert (kronos_source.end_time is None or
            isinstance(kronos_source.end_time, int))
    assert (kronos_source.namespace is None or
            isinstance(kronos_source.namespace, types.StringTypes))

    return kronos_source

  def get_streams(self):
    kc = KronosClient(self._host, namespace=self.namespace)
    kstreams = kc.get_streams(namespace=self.namespace)
    return sorted(kstreams)

  def get_schema(self, stream_name):
    kc = KronosClient(self._host, namespace=self.namespace)
    schema = kc.infer_schema(stream_name, namespace=self.namespace)
    return schema
