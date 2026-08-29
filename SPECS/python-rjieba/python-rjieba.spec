# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Suyun <ziyu.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname rjieba

Name:           python-%{srcname}
Version:        0.2.1
Release:        %autorelease
Summary:        jieba-rs Python binding
License:        MIT
URL:            https://github.com/messense/rjieba-py
VCS:            git:https://github.com/messense/rjieba-py.git
#!RemoteAsset:  sha256:af96d4a14f24b68e053024ab993ec008c868d85598f8af928f2424ff4d86bc44
Source0:        https://files.pythonhosted.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname} -L

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(maturin)
BuildRequires:  python3dist(pip)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(jieba-rs-0.9/default) >= 0.9.0
BuildRequires:  crate(pyo3-0.28/abi3-py38) >= 0.28.3
BuildRequires:  crate(pyo3-0.28/default) >= 0.28.3
BuildRequires:  crate(pyo3-0.28/generate-import-lib) >= 0.28.3

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
jieba-rs Python binding, implemented with Rust and exposed as a Python
extension module.

%prep
%autosetup -n %{srcname}-%{version} -a 0
%rust_setup_registry
rm -f Cargo.lock

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
