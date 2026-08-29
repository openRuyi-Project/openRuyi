# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname requests-mock
%global modname requests_mock

Name:           python-%{srcname}
Version:        1.12.1
Release:        %autorelease
Summary:        Mock out responses from the requests package
License:        Apache-2.0
URL:            https://requests-mock.readthedocs.io/
VCS:            git:https://github.com/jamielennox/requests-mock.git
#!RemoteAsset:  sha256:e9e12e333b525156e82a3c852f22016b9158220d2f47454de9cae8a77d371401
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{modname}
# requests_mock.contrib modules import fixtures and pytest, which are
# optional integrations not required at runtime
BuildOption(check):  -e '%{modname}.contrib*'

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
requests-mock provides a building block to stub out the HTTP requests
portions of your testing code. It creates a transport adapter for the
requests library so that requests made in tests are handled by mocked
responses instead of real network calls.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
