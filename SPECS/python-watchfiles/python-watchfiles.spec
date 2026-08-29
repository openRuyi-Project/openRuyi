# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname watchfiles

Name:           python-%{srcname}
Version:        1.2.0
Release:        %autorelease
Summary:        Simple, modern and high performance file watching and code reload in python.
License:        MIT
URL:            https://github.com/samuelcolvin/watchfiles
#!RemoteAsset:  sha256:c995fba777f1ea992f090f9236e9284cf7a5d1a0130dd5a3d82c598cacd76838
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
BuildRequires:  python3dist(anyio)
BuildRequires:  crate(crossbeam-channel-0.5/default) >= 0.5.15
BuildRequires:  crate(notify-8/default) >= 8.2.0
BuildRequires:  crate(pyo3-0.28/default) >= 0.28.3
BuildRequires:  crate(pyo3-0.28/extension-module) >= 0.28.3
BuildRequires:  crate(pyo3-0.28/generate-import-lib) >= 0.28.3

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Simple, modern and high performance file watching and code reload in python.

%prep -a
%rust_setup_registry
rm -f Cargo.lock

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/watchfiles

%changelog
%autochangelog
