# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import p2p_pb2 as p2p__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in p2p_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class P2PServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadFile = channel.unary_unary(
                '/p2p.P2PService/UploadFile',
                request_serializer=p2p__pb2.FileChunk.SerializeToString,
                response_deserializer=p2p__pb2.UploadResponse.FromString,
                _registered_method=True)
        self.DownloadFile = channel.unary_stream(
                '/p2p.P2PService/DownloadFile',
                request_serializer=p2p__pb2.FileRequest.SerializeToString,
                response_deserializer=p2p__pb2.FileChunk.FromString,
                _registered_method=True)


class P2PServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UploadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_P2PServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadFile': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadFile,
                    request_deserializer=p2p__pb2.FileChunk.FromString,
                    response_serializer=p2p__pb2.UploadResponse.SerializeToString,
            ),
            'DownloadFile': grpc.unary_stream_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=p2p__pb2.FileRequest.FromString,
                    response_serializer=p2p__pb2.FileChunk.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'p2p.P2PService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('p2p.P2PService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class P2PService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UploadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/p2p.P2PService/UploadFile',
            p2p__pb2.FileChunk.SerializeToString,
            p2p__pb2.UploadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/p2p.P2PService/DownloadFile',
            p2p__pb2.FileRequest.SerializeToString,
            p2p__pb2.FileChunk.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class TrackerServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterPeer = channel.unary_unary(
                '/p2p.TrackerService/RegisterPeer',
                request_serializer=p2p__pb2.PeerInfo.SerializeToString,
                response_deserializer=p2p__pb2.RegisterResponse.FromString,
                _registered_method=True)
        self.QueryPeers = channel.unary_unary(
                '/p2p.TrackerService/QueryPeers',
                request_serializer=p2p__pb2.FileRequest.SerializeToString,
                response_deserializer=p2p__pb2.PeerList.FromString,
                _registered_method=True)


class TrackerServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterPeer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryPeers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrackerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterPeer': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterPeer,
                    request_deserializer=p2p__pb2.PeerInfo.FromString,
                    response_serializer=p2p__pb2.RegisterResponse.SerializeToString,
            ),
            'QueryPeers': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryPeers,
                    request_deserializer=p2p__pb2.FileRequest.FromString,
                    response_serializer=p2p__pb2.PeerList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'p2p.TrackerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('p2p.TrackerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TrackerService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterPeer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/p2p.TrackerService/RegisterPeer',
            p2p__pb2.PeerInfo.SerializeToString,
            p2p__pb2.RegisterResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def QueryPeers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/p2p.TrackerService/QueryPeers',
            p2p__pb2.FileRequest.SerializeToString,
            p2p__pb2.PeerList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
