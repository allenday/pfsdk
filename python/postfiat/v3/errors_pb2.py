# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: postfiat/v3/errors.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'postfiat/v3/errors.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18postfiat/v3/errors.proto\x12\x0bpostfiat.v3\"\x8d\x04\n\tErrorInfo\x12*\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x16.postfiat.v3.ErrorCodeR\x04\x63ode\x12\x36\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\x1a.postfiat.v3.ErrorCategoryR\x08\x63\x61tegory\x12\x36\n\x08severity\x18\x03 \x01(\x0e\x32\x1a.postfiat.v3.ErrorSeverityR\x08severity\x12\x18\n\x07message\x18\x04 \x01(\tR\x07message\x12\x18\n\x07\x64\x65tails\x18\x05 \x01(\tR\x07\x64\x65tails\x12\x14\n\x05\x66ield\x18\x06 \x01(\tR\x05\x66ield\x12=\n\x07\x63ontext\x18\x07 \x03(\x0b\x32#.postfiat.v3.ErrorInfo.ContextEntryR\x07\x63ontext\x12\x1c\n\ttimestamp\x18\x08 \x01(\x03R\ttimestamp\x12\x19\n\x08\x65rror_id\x18\t \x01(\tR\x07\x65rrorId\x12\x1d\n\ndebug_info\x18\n \x01(\tR\tdebugInfo\x12 \n\x0bremediation\x18\x0b \x03(\tR\x0bremediation\x12%\n\x0erelated_errors\x18\x0c \x03(\tR\rrelatedErrors\x1a:\n\x0c\x43ontextEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xc2\x01\n\rErrorResponse\x12,\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x16.postfiat.v3.ErrorInfoR\x05\x65rror\x12\x43\n\x11\x61\x64\x64itional_errors\x18\x02 \x03(\x0b\x32\x16.postfiat.v3.ErrorInfoR\x10\x61\x64\x64itionalErrors\x12\x1d\n\nrequest_id\x18\x03 \x01(\tR\trequestId\x12\x1f\n\x0b\x61pi_version\x18\x04 \x01(\tR\napiVersion\"\xfd\x02\n\x13\x45xceptionDefinition\x12\x1d\n\nclass_name\x18\x01 \x01(\tR\tclassName\x12!\n\x0cparent_class\x18\x02 \x01(\tR\x0bparentClass\x12\x37\n\x0b\x65rror_codes\x18\x03 \x03(\x0e\x32\x16.postfiat.v3.ErrorCodeR\nerrorCodes\x12\x36\n\x08\x63\x61tegory\x18\x04 \x01(\x0e\x32\x1a.postfiat.v3.ErrorCategoryR\x08\x63\x61tegory\x12\x45\n\x10\x64\x65\x66\x61ult_severity\x18\x05 \x01(\x0e\x32\x1a.postfiat.v3.ErrorSeverityR\x0f\x64\x65\x66\x61ultSeverity\x12$\n\rdocumentation\x18\x06 \x01(\tR\rdocumentation\x12\x1c\n\tretryable\x18\x07 \x01(\x08R\tretryable\x12(\n\x10http_status_code\x18\x08 \x01(\x05R\x0ehttpStatusCode*J\n\rErrorSeverity\x12\x08\n\x04INFO\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x0c\n\x08\x43RITICAL\x10\x03\x12\t\n\x05\x46\x41TAL\x10\x04*\x8a\x01\n\rErrorCategory\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06\x43LIENT\x10\x01\x12\n\n\x06SERVER\x10\x02\x12\x0b\n\x07NETWORK\x10\x03\x12\x08\n\x04\x41UTH\x10\x04\x12\x0e\n\nVALIDATION\x10\x05\x12\x11\n\rCONFIGURATION\x10\x06\x12\x0c\n\x08\x42USINESS\x10\x07\x12\x0c\n\x08\x45XTERNAL\x10\x08*\xce\n\n\tErrorCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x12\n\rUNKNOWN_ERROR\x10\xe8\x07\x12\x10\n\x0b\x42\x41\x44_REQUEST\x10\xe9\x07\x12\x12\n\rINVALID_INPUT\x10\xea\x07\x12\x16\n\x11MISSING_PARAMETER\x10\xeb\x07\x12\x16\n\x11INVALID_PARAMETER\x10\xec\x07\x12\x16\n\x11MALFORMED_REQUEST\x10\xed\x07\x12\x1a\n\x15UNSUPPORTED_OPERATION\x10\xee\x07\x12\x17\n\x12RESOURCE_NOT_FOUND\x10\xef\x07\x12\x17\n\x12\x44UPLICATE_RESOURCE\x10\xf0\x07\x12\x18\n\x13PRECONDITION_FAILED\x10\xf1\x07\x12\x16\n\x11REQUEST_TOO_LARGE\x10\xf2\x07\x12\x1c\n\x17\x41UTHENTICATION_REQUIRED\x10\xd1\x0f\x12\x1a\n\x15\x41UTHENTICATION_FAILED\x10\xd2\x0f\x12\x18\n\x13INVALID_CREDENTIALS\x10\xd3\x0f\x12\x12\n\rTOKEN_EXPIRED\x10\xd4\x0f\x12\x12\n\rTOKEN_INVALID\x10\xd5\x0f\x12\x14\n\x0fSESSION_EXPIRED\x10\xd6\x0f\x12\x13\n\x0e\x41\x43\x43OUNT_LOCKED\x10\xd7\x0f\x12\x15\n\x10\x41\x43\x43OUNT_DISABLED\x10\xd8\x0f\x12\x19\n\x14\x41UTHORIZATION_FAILED\x10\xb9\x17\x12\x1d\n\x18INSUFFICIENT_PERMISSIONS\x10\xba\x17\x12\x12\n\rACCESS_DENIED\x10\xbb\x17\x12\x17\n\x12RESOURCE_FORBIDDEN\x10\xbc\x17\x12\x1a\n\x15OPERATION_NOT_ALLOWED\x10\xbd\x17\x12\x16\n\x11VALIDATION_FAILED\x10\xa1\x1f\x12\x1d\n\x18SCHEMA_VALIDATION_FAILED\x10\xa2\x1f\x12\x12\n\rTYPE_MISMATCH\x10\xa3\x1f\x12\x17\n\x12VALUE_OUT_OF_RANGE\x10\xa4\x1f\x12\x13\n\x0eINVALID_FORMAT\x10\xa5\x1f\x12\x19\n\x14\x43ONSTRAINT_VIOLATION\x10\xa6\x1f\x12\x1b\n\x16REQUIRED_FIELD_MISSING\x10\xa7\x1f\x12\x1a\n\x15INTERNAL_SERVER_ERROR\x10\x89\'\x12\x18\n\x13SERVICE_UNAVAILABLE\x10\x8a\'\x12\x13\n\x0e\x44\x41TABASE_ERROR\x10\x8b\'\x12\x18\n\x13\x43ONFIGURATION_ERROR\x10\x8c\'\x12\x17\n\x12\x44\x45PENDENCY_FAILURE\x10\x8d\'\x12\x17\n\x12RESOURCE_EXHAUSTED\x10\x8e\'\x12\x0c\n\x07TIMEOUT\x10\x8f\'\x12\r\n\x08\x44\x45\x41\x44LOCK\x10\x90\'\x12\x12\n\rNETWORK_ERROR\x10\xf1.\x12\x16\n\x11\x43ONNECTION_FAILED\x10\xf2.\x12\x17\n\x12\x43ONNECTION_TIMEOUT\x10\xf3.\x12\x17\n\x12\x43ONNECTION_REFUSED\x10\xf4.\x12\x1a\n\x15\x44NS_RESOLUTION_FAILED\x10\xf5.\x12\x0e\n\tSSL_ERROR\x10\xf6.\x12\x13\n\x0ePROTOCOL_ERROR\x10\xf7.\x12\x1c\n\x17\x42USINESS_RULE_VIOLATION\x10\xd9\x36\x12\x1b\n\x16\x45XTERNAL_SERVICE_ERROR\x10\xc1>\x12!\n\x1c\x45XTERNAL_SERVICE_UNAVAILABLE\x10\xc2>\x12\x1d\n\x18\x45XTERNAL_SERVICE_TIMEOUT\x10\xc3>\x12\x17\n\x12\x45XTERNAL_API_ERROR\x10\xc4>\x12\x18\n\x13THIRD_PARTY_FAILURE\x10\xc5>\x12\x18\n\x13RATE_LIMIT_EXCEEDED\x10\xa9\x46\x12\x13\n\x0eQUOTA_EXCEEDED\x10\xaa\x46\x12\x0e\n\tTHROTTLED\x10\xab\x46\x42\x83\x01\n\x0f\x63om.postfiat.v3B\x0b\x45rrorsProtoP\x01Z\x16postfiat/v3;postfiatv3\xa2\x02\x03PXX\xaa\x02\x0bPostfiat.V3\xca\x02\x0bPostfiat\\V3\xe2\x02\x17Postfiat\\V3\\GPBMetadata\xea\x02\x0cPostfiat::V3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'postfiat.v3.errors_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.postfiat.v3B\013ErrorsProtoP\001Z\026postfiat/v3;postfiatv3\242\002\003PXX\252\002\013Postfiat.V3\312\002\013Postfiat\\V3\342\002\027Postfiat\\V3\\GPBMetadata\352\002\014Postfiat::V3'
  _globals['_ERRORINFO_CONTEXTENTRY']._loaded_options = None
  _globals['_ERRORINFO_CONTEXTENTRY']._serialized_options = b'8\001'
  _globals['_ERRORSEVERITY']._serialized_start=1150
  _globals['_ERRORSEVERITY']._serialized_end=1224
  _globals['_ERRORCATEGORY']._serialized_start=1227
  _globals['_ERRORCATEGORY']._serialized_end=1365
  _globals['_ERRORCODE']._serialized_start=1368
  _globals['_ERRORCODE']._serialized_end=2726
  _globals['_ERRORINFO']._serialized_start=42
  _globals['_ERRORINFO']._serialized_end=567
  _globals['_ERRORINFO_CONTEXTENTRY']._serialized_start=509
  _globals['_ERRORINFO_CONTEXTENTRY']._serialized_end=567
  _globals['_ERRORRESPONSE']._serialized_start=570
  _globals['_ERRORRESPONSE']._serialized_end=764
  _globals['_EXCEPTIONDEFINITION']._serialized_start=767
  _globals['_EXCEPTIONDEFINITION']._serialized_end=1148
# @@protoc_insertion_point(module_scope)
