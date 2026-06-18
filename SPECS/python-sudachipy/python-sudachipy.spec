# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sudachipy

Name:           python-sudachipy
Version:        0.6.11
Release:        %autorelease
Summary:        A Japanese morphological analyzer
License:        Apache-2.0
URL:            https://github.com/WorksApplications/sudachi.rs/
#!RemoteAsset:  sha256:4f03310fd3fc779b3000f49395c939d18a30081632d3cb14488426f7c07cc526
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4
Source1:        https://raw.githubusercontent.com/WorksApplications/sudachi.rs/v%{version}/LICENSE
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(wheel)
BuildRequires:  crate(aho-corasick-1/default) >= 1.0.0
BuildRequires:  crate(bitflags-2/default) >= 2.5.0
BuildRequires:  crate(csv-1/default) >= 1.3.0
BuildRequires:  crate(fancy-regex-0.13/default) >= 0.13.0
BuildRequires:  crate(indexmap-2/default) >= 2.2.0
BuildRequires:  crate(itertools-0.13/default) >= 0.13.0
BuildRequires:  crate(lazy-static-1/default) >= 1.4.0
BuildRequires:  crate(libloading-0.8/default) >= 0.8.0
BuildRequires:  crate(memmap2-0.9/default) >= 0.9.0
BuildRequires:  crate(nom-7/default) >= 7.0.0
BuildRequires:  crate(pyo3-0.27/default) >= 0.27.0
BuildRequires:  crate(pyo3-0.27/extension-module) >= 0.27.0
BuildRequires:  crate(regex-1/default) >= 1.0.0
BuildRequires:  crate(scopeguard-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(thiserror-1/default) >= 1.0.0
BuildRequires:  crate(thread-local-1/default) >= 1.1.0
BuildRequires:  crate(unicode-normalization-0.1/default) >= 0.1.0
BuildRequires:  crate(yada-0.5/default) >= 0.5.0

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
SudachiPy is a Python implementation of Sudachi, a Japanese morphological
analyzer. It provides robust word segmentation and part-of-speech tagging,
designed for high-performance natural language processing.

%generate_buildrequires
%pyproject_buildrequires

%prep -a
cp %{SOURCE1} .
%rust_setup_registry
rm -f Cargo.lock

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/sudachipy

%changelog
%autochangelog
