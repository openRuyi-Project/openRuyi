# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname etelemetry

Name:           python-%{srcname}
Version:        0.3.1
Release:        %autorelease
Summary:        Etelemetry python client API
License:        Apache-2.0 AND Unlicense
# No pypi download source.
URL:            https://github.com/sensein/etelemetry-client
#!RemoteAsset:  sha256:91861fc0e9593e583ad12610a99859d88a45216f59e803c96cfa8b7334f6171f
Source0:        https://github.com/sensein/etelemetry-client/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# fix version,or will 0+unknown.dist-info
Patch0:         0001-fix-version-error.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(ci-info)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
A lightweight python client to communicate with the etelemetry server.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.*
%license LICENSE

%changelog
%{?autochangelog}
