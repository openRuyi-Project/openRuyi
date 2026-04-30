# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname httpx-sse
%global pypi_name httpx_sse

Name:           python-%{srcname}
Version:        0.4.3
Release:        %autorelease
Summary:        Consume Server-Sent Event messages with HTTPX
License:        MIT
URL:            https://github.com/florimondmanca/httpx-sse
#!RemoteAsset:  sha256:9b1ed0127459a66014aec3c56bebd93da3c1bc8bb6618c8082039a44889a755d
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Patches
# Drop setuptools-scm to build with distro-provided static version metadata
Patch2000:      2000-python-httpx-sse-drop-setuptools-scm-build-requirement.patch

BuildOption(install):  -l %{pypi_name}
BuildOption(check):  %{pypi_name}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
httpx-sse provides helpers to consume Server-Sent Event (SSE) streams through
HTTPX clients.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE

%changelog
%autochangelog
