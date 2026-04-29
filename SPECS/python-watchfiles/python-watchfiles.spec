# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname watchfiles

Name:           python-%{srcname}
Version:        1.1.1
Release:        %autorelease
Summary:        Simple, modern and high performance file watching and code reload in python.
License:        MIT
URL:            https://github.com/samuelcolvin/watchfiles
#!RemoteAsset:  sha256:a173cb5c16c4f40ab19cecf48a534c409f7ea983ab8fed0741304a1c0a31b3f2
Source0:        https://files.pythonhosted.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  python3dist(maturin)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(puccinialin)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Simple, modern and high performance file watching and code reload in python.

%prep -a
%rust_setup_registry

%generate_buildrequires
%cargo_buildrequires

%build -p
%rust_build_release

%files -f %{pyproject_files}
%{_bindir}/watchfiles

%changelog
%autochangelog
