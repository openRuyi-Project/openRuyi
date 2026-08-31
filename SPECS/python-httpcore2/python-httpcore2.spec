# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zitao Zhou <zitao.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname httpcore2

Name:           python-%{srcname}
Version:        2.12.0
Release:        %autorelease
Summary:        Minimal low-level Python HTTP client
License:        BSD-3-Clause
URL:            https://github.com/pydantic/httpx2
#!RemoteAsset:  sha256:9293522bba0aa7c4c8e9e3f040c16575bd8868e155a77fa30c7a9085a5eae648
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Disable dynamic versioning and use the system TLS backend.
Patch2000:      2000-python-httpcore2-use-static-version-and-system-tls.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(h11)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
HTTP Core 2 provides a minimal low-level HTTP client for HTTPX 2.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE.md

%changelog
%autochangelog
