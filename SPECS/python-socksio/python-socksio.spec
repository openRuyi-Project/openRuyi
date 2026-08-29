# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname socksio

Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        Client-side sans-I/O SOCKS proxy implementation
License:        MIT
URL:            https://github.com/sethmlarson/socksio
#!RemoteAsset:  sha256:f88beb3da5b5c38b9890469de67d0cb0f9d494b78b106ca1845f96c10b91c4ac
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# change the dep version of python-flit-core.
Patch0:         0001-Unpin-flit-core-dependency.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(flit-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Client-side sans-I/O SOCKS proxy implementation. Supports SOCKS4, SOCKS4A, and
SOCKS5. socksio is a sans-I/O library similar to h11 or h2.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md CHANGELOG.md
%license LICENSE

%changelog
%autochangelog
