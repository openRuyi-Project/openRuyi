# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname httpx-sse
%global pypi_name httpx_sse

Name:           python-%{srcname}
Version:        0.4.3
Release:        %autorelease
Summary:        Consume Server-Sent Event (SSE) messages with HTTPX
License:        MIT
URL:            https://github.com/florimondmanca/httpx-sse
#!RemoteAsset:  sha256:9b1ed0127459a66014aec3c56bebd93da3c1bc8bb6618c8082039a44889a755d
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Consume Server-Sent Event (SSE) messages with HTTPX, supporting both
synchronous and asynchronous clients.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE

%changelog
%autochangelog
