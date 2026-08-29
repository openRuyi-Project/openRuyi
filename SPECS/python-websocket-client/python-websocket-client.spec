# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname websocket_client

Name:           python-websocket-client
Version:        1.9.0
Release:        %autorelease
Summary:        WebSocket client for python
License:        Apache-2.0
URL:            https://github.com/websocket-client/websocket-client
#!RemoteAsset:  sha256:9e813624b6eb619999a97dc7958469217c3176312b3a16a4bd1bc7e08a46ec98
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l websocket

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

Provides:       python3-websocket-client = %{version}-%{release}
%python_provide python3-websocket-client

%description
websocket-client is a WebSocket client for Python. It provides access to low
level APIs for WebSockets. websocket-client implements version hybi-13 of the
WebSocket protocol.

%generate_buildrequires
%pyproject_buildrequires

%check -a
%pytest -v websocket/tests

%files -f %{pyproject_files}
%doc README.md ChangeLog
%{_bindir}/wsdump

%changelog
%autochangelog
