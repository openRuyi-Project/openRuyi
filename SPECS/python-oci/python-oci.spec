# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname oci

Name:           python-%{srcname}
Version:        2.186.0
Release:        %autorelease
Summary:        Oracle Cloud Infrastructure SDK for Python
License:        (UPL-1.0 OR Apache-2.0) AND MIT AND MPL-2.0 AND BSD-2-Clause AND BSD-3-Clause AND LGPL-2.1-only AND PSF-2.0 AND OpenSSL-standalone AND SSLeay-standalone
URL:            https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/
VCS:            git:https://github.com/oracle/oci-python-sdk.git
#!RemoteAsset:  sha256:d8c75fb73bddaadcf3835b07b584f80c785686aa3c8a66ae4e4062ac63757c58
Source0:        https://files.pythonhosted.org/packages/source/o/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

Patch2000:      2000-use-mcp-2-streamable-http-client.patch

BuildOption(install):  -L %{srcname} +auto

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(aiohttp) >= 3.10.11
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(circuitbreaker) >= 1.3.1
BuildRequires:  python3dist(crc32c) = 2.8
BuildRequires:  python3dist(cryptography) < 51
BuildRequires:  python3dist(docstring-parser) >= 0.16
BuildRequires:  python3dist(mcp) >= 1.9
BuildRequires:  python3dist(pydantic) >= 2.10.6
BuildRequires:  python3dist(pydantic) < 3
BuildRequires:  python3dist(pyjwt) >= 2.12
BuildRequires:  python3dist(pyopenssl) >= 26.2
BuildRequires:  python3dist(python-dateutil) >= 2.5.3
BuildRequires:  python3dist(pytz) >= 2016.10
BuildRequires:  python3dist(rich) >= 13.9.4
BuildRequires:  python3dist(setuptools) >= 78.1.1
BuildRequires:  python3dist(urllib3) >= 2.6.3
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
The OCI Python SDK enables Python applications to manage Oracle Cloud
Infrastructure resources and services.

%pyproject_extras_subpkg -n python-%{srcname} adk

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst CHANGELOG.rst
%license LICENSE.txt THIRD_PARTY_LICENSES.txt

%changelog
%autochangelog
