# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sigstore

Name:           python-%{srcname}
Version:        4.4.0
Release:        %autorelease
Summary:        Python tool for signing and verifying artifacts with Sigstore
License:        Apache-2.0
URL:            https://github.com/sigstore/sigstore-python
VCS:            git:https://github.com/sigstore/sigstore-python.git
#!RemoteAsset:  sha256:20ffe791c1fa33ce62148c0291b46280d29c1910964d9afac419e9b1a8afc56b
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cryptography) >= 42
BuildRequires:  python3dist(flit-core) >= 3.2
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(id) >= 1.1
BuildRequires:  python3dist(platformdirs) >= 4.2
BuildRequires:  python3dist(platformdirs) < 5
BuildRequires:  python3dist(pyasn1) >= 0.6
BuildRequires:  python3dist(pyasn1) < 0.7
BuildRequires:  python3dist(pydantic) >= 2
BuildRequires:  python3dist(pydantic) < 3
BuildRequires:  python3dist(pyjwt) >= 2.1
BuildRequires:  python3dist(pyopenssl) >= 23
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(rfc3161-client) >= 1.0.3
BuildRequires:  python3dist(rfc3161-client) < 1.1
BuildRequires:  python3dist(rfc8785) >= 0.1.2
BuildRequires:  python3dist(rfc8785) < 0.2
BuildRequires:  python3dist(rich) >= 13
BuildRequires:  python3dist(rich) < 16
BuildRequires:  python3dist(sigstore-models) = 0.0.6
BuildRequires:  python3dist(sigstore-rekor-types) = 0.0.18
BuildRequires:  python3dist(tuf) >= 6
BuildRequires:  python3dist(tuf) < 8

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Sigstore provides keyless signing and verification of software artifacts with
identity-based certificates and transparency logs.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/sigstore

%changelog
%autochangelog
