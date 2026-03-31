# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pymongo

Name:           python-%{srcname}
Version:        4.16.0
Release:        %autorelease
Summary:        Python driver for MongoDB
License:        Apache-2.0
URL:            https://pymongo.readthedocs.io/en/stable/
VCS:            git:https://github.com/mongodb/mongo-python-driver
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(dnspython)
BuildRequires:  python3dist(hatch-requirements-txt)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
The Python driver for MongoDB.

%package     -n python-bson
# All code is Apache-2.0 except bson/time64*.{c,h} which is MIT
License:        Apache-2.0 AND MIT
Summary:        Python bson library
Provides:       python3-bson
%python_provide python3-bson

%description -n python-bson
BSON is a binary-encoded serialization of JSON-like documents. BSON is designed
to be lightweight, traversable, and efficient. BSON, like JSON, supports the
embedding of objects and arrays within other objects and arrays.

%package     -n python-pymongo-gridfs
Summary:        Python GridFS driver for MongoDB
Requires:       python-pymongo%{?_isa} = %{version}-%{release}
Provides:       python3-pymongo-gridfs
%python_provide python3-pymongo-gridfs

%description -n python-pymongo-gridfs
GridFS is a storage specification for large objects in MongoDB.
# TODO: enable submodule in the future
# pyproject_extras_subpkg -n python3-pymongo ocsp snappy zstd

%generate_buildrequires
%pyproject_buildrequires
# pyproject_buildrequires -x ocsp,snappy,test,zstd

%build -p
export PYMONGO_C_EXT_MUST_BUILD=1

%check
# Skip tests that require network/nameservers and tests that cause segfaults
%pytest -v \
    --deselect=test/asynchronous/test_client.py::AsyncClientUnitTest::test_connection_timeout_ms_propagates_to_DNS_resolver \
    --deselect=test/asynchronous/test_client.py::AsyncClientUnitTest::test_detected_environment_logging \
    --deselect=test/asynchronous/test_client.py::AsyncClientUnitTest::test_detected_environment_warning \
    --deselect=test/test_client.py::ClientUnitTest::test_connection_timeout_ms_propagates_to_DNS_resolver \
    --deselect=test/test_client.py::ClientUnitTest::test_detected_environment_logging \
    --deselect=test/test_client.py::ClientUnitTest::test_detected_environment_warning \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_10_all_dns_selected \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_11_all_dns_selected \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_12_new_dns_randomly_selected \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_addition \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_dns_failures \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_dns_record_lookup_empty \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_does_not_flipflop \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_recover_from_initially_empty_seedlist \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_recover_from_initially_erroring_seedlist \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_removal \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_replace_both_with_one \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_replace_both_with_two \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_replace_one \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_srv_service_name \
    --deselect=test/test_srv_polling.py::TestSrvPolling::test_srv_waits_to_poll \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_10_all_dns_selected \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_11_all_dns_selected \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_12_new_dns_randomly_selected \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_addition \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_dns_failures \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_dns_record_lookup_empty \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_does_not_flipflop \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_recover_from_initially_empty_seedlist \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_recover_from_initially_erroring_seedlist \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_removal \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_replace_both_with_one \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_replace_both_with_two \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_replace_one \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_srv_service_name \
    --deselect=test/asynchronous/test_srv_polling.py::TestSrvPolling::test_srv_waits_to_poll \
    --deselect=test/test_uri_spec.py::TestAllScenarios::test_test_uri_options_srv-options_SRV_URI_with_custom_srvServiceName \
    --deselect=test/test_uri_spec.py::TestAllScenarios::test_test_uri_options_srv-options_SRV_URI_with_invalid_type_for_srvMaxHosts \
    --deselect=test/test_uri_spec.py::TestAllScenarios::test_test_uri_options_srv-options_SRV_URI_with_negative_integer_for_srvMaxHosts \
    --deselect=test/test_uri_spec.py::TestAllScenarios::test_test_uri_options_srv-options_SRV_URI_with_positive_srvMaxHosts_and_loadBalanced=false \
    --deselect=test/test_uri_spec.py::TestAllScenarios::test_test_uri_options_srv-options_SRV_URI_with_srvMaxHosts \
    --deselect=test/test_uri_spec.py::TestAllScenarios::test_test_uri_options_srv-options_SRV_URI_with_srvMaxHosts=0_and_loadBalanced=true \
    --deselect=test/test_uri_spec.py::TestAllScenarios::test_test_uri_options_srv-options_SRV_URI_with_srvMaxHosts=0_and_replicaSet \
    --deselect=test/asynchronous/test_custom_types.py::TestBSONCustomTypeEncoderAndFallbackEncoderTandem::test_infinite_loop_exceeds_max_recursion_depth \
    --deselect=test/test_custom_types.py::TestBSONCustomTypeEncoderAndFallbackEncoderTandem::test_infinite_loop_exceeds_max_recursion_depth

%files -f %{pyproject_files}
%doc README.md

%files -n python-bson
%license LICENSE
%doc README.md
%{python3_sitearch}/bson

%files -n python-pymongo-gridfs
%license LICENSE
%doc README.md
%{python3_sitearch}/gridfs

%changelog
%{?autochangelog}
