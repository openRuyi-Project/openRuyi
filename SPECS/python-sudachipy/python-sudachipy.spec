# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sudachipy

Name:           python-sudachipy
Version:        0.6.10
Release:        %autorelease
Summary:        A Japanese morphological analyzer
License:        Apache-2.0
URL:            https://github.com/WorksApplications/sudachi.rs/
#!RemoteAsset:  sha256:b8910a4610de98b2c3cb6dc3362fea93e3ba5059f1eb445a68baa9585278f31b
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset:  sha256:c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4
Source1:        https://raw.githubusercontent.com/WorksApplications/sudachi.rs/v%{version}/LICENSE
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(wheel)
BuildRequires:  crate(pyo3-0.23/extension-module) >= 0.23.5
BuildRequires:  crate(pyo3-macros-0.23) >= 0.23.5
BuildRequires:  crate(scopeguard-1.0) >= 1.2.0
BuildRequires:  crate(thread-local-1.0) >= 1.1.9
BuildRequires:  crate(indoc-2.0) >= 2.0.7
BuildRequires:  crate(unindent-0.2) >= 0.2.4
BuildRequires:  crate(aho-corasick-1.0) >= 1.1.4
BuildRequires:  crate(bitflags-2.0) >= 2.11.0
BuildRequires:  crate(csv-1.0) >= 1.4.0
BuildRequires:  crate(fancy-regex-0.13) >= 0.13.0
BuildRequires:  crate(indexmap-2.0) >= 2.13.0
BuildRequires:  crate(itertools-0.13) >= 0.13.0
BuildRequires:  crate(lazy-static-1.0) >= 1.5.0
BuildRequires:  crate(libloading-0.8) >= 0.8.9
BuildRequires:  crate(memmap2-0.9) >= 0.9.10
BuildRequires:  crate(nom-7.0) >= 7.1.3
BuildRequires:  crate(regex-1.0) >= 1.12.3
BuildRequires:  crate(serde-1.0) >= 1.0.228
BuildRequires:  crate(serde-json-1.0) >= 1.0.149
BuildRequires:  crate(thiserror-1.0) >= 1.0.69
BuildRequires:  crate(unicode-normalization-0.1) >= 0.1.25
BuildRequires:  crate(yada-0.5) >= 0.5.1

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

mkdir -p ~/.cargo
cat > ~/.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/sudachipy

%changelog
%autochangelog
