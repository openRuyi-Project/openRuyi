# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname aiohappyeyeballs

Name:           python-%{srcname}
Version:        2.6.1
Release:        %autorelease
Summary:        Happy Eyeballs for asyncio
License:        PSF-2.0
URL:            https://github.com/aio-libs/aiohappyeyeballs
#!RemoteAsset:  sha256:c3f9d0113123803ccadfdf3f0faa505bc78e6a72d1cc4806cbd719826e943558
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(poetry-core)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
This library exists to allow connecting with Happy Eyeballs (RFC 8305) when you
already have a list of addrinfo and not a DNS name.

The stdlib version of loop.create_connection() will only work when you pass in
an unresolved name which is not a good fit when using DNS caching or resolving
names via another method such as zeroconf.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
