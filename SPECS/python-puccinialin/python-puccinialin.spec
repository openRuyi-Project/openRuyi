# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname puccinialin

Name:           python-%{srcname}
Version:        0.1.8
Release:        %autorelease
Summary:        Install rust into a temporary directory for boostrapping a rust-based build backend
License:        MIT OR Apache-2.0
URL:            https://github.com/konstin/puccinialin
#!RemoteAsset:  sha256:e19f6316967ae100bf3fb92d8af95e3cec11ce0de58acd2f1a0bca835403a394
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(platformdirs)
BuildRequires:  python3dist(tqdm)
BuildRequires:  python3dist(flit-core)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Install rust into a temporary directory to support rust-based builds.
Cargo and rustc are installed into a cache directory, to avoid modifying
the host's environment, and activated using a set of environment variables.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%{_bindir}/puccinialize
%doc README.md
%license license-mit
%license license-apache

%changelog
%{?autochangelog}
