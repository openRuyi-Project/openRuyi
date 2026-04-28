# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname uvicorn

Name:           python-%{srcname}
Version:        0.44.0
Release:        %autorelease
Summary:        The lightning-fast ASGI server
License:        BSD-3-Clause
URL:            https://github.com/Kludex/uvicorn
VCS:            git:https://github.com/Kludex/uvicorn.git
#!RemoteAsset:  sha256:6c942071b68f07e178264b9152f1f16dfac5da85880c4ce06366a96d70d4f31e
Source:         https://files.pythonhosted.org/packages/source/u/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  -e "%{srcname}.protocols.websockets.wsproto_impl" -e "%{srcname}.supervisors.watchfilesreload"

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(uvloop)
BuildRequires:  python3dist(httptools)
BuildRequires:  python3dist(websockets)
BuildRequires:  python3dist(gunicorn)

Requires:       python3dist(click)
Requires:       python3dist(h11)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Uvicorn is a lightning-fast ASGI server implementation, using uvloop and
httptools. It supports HTTP/1.1 and WebSockets.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.md
%{_bindir}/uvicorn

%changelog
%autochangelog
