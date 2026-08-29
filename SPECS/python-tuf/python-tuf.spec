# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tuf

Name:           python-%{srcname}
Version:        7.0.0
Release:        %autorelease
Summary:        Secure updater framework for Python
License:        Apache-2.0 OR MIT
URL:            https://www.updateframework.com
VCS:            git:https://github.com/theupdateframework/python-tuf.git
#!RemoteAsset:  sha256:9d2e6723538e0d5a3e482b6de805fcfe64481448d5853039ba6b06ba541efd7f
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
BuildOption(check):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(hatchling) = 1.29
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(securesystemslib) >= 1
BuildRequires:  python3dist(urllib3) < 3
BuildRequires:  python3dist(urllib3) >= 1.21.1

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

Requires:       python3dist(requests)

%description
The Update Framework secures software update systems against repository and
signing-key compromise. This package provides its Python metadata, repository,
and client implementations.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE LICENSE-MIT

%changelog
%autochangelog
