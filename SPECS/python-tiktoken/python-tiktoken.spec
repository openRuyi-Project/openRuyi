# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yifan Xu <xuyifan@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tiktoken

Name:           python-%{srcname}
Version:        0.12.0
Release:        %autorelease
Summary:        tiktoken is a fast BPE tokeniser for use with OpenAI's models
License:        MIT AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND Apache-2.0 AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
URL:            https://pypi.org/project/tiktoken/
#!RemoteAsset:  sha256:b18ba7ee2b093863978fcb14f74b3707cdc8d4d4d3836853ce7ec60772139931
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(regex)
BuildRequires:  python3dist(requests)
BuildRequires:  rust-rpm-macros
BuildRequires:  rust
BuildRequires:  crate(pyo3-0.26/extension-module) >= 0.26.0
BuildRequires:  crate(pyo3-0.26/macros) >= 0.26.0
BuildRequires:  crate(pyo3-macros-0.26/default) >= 0.26.0
BuildRequires:  crate(bstr-1)
BuildRequires:  crate(fancy-regex-0.13)
BuildRequires:  crate(bit-set-0.5)
BuildRequires:  crate(regex-1)
BuildRequires:  crate(rustc-hash-2)
BuildRequires:  crate(regex-automata-0.4)
BuildRequires:  crate(serde-1)
BuildRequires:  crate(indoc-2)
BuildRequires:  crate(unindent-0.2)
BuildRequires:  crate(aho-corasick-1)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
tiktoken is a fast BPE tokeniser for use with OpenAI's models.

%prep -a
%rust_setup_registry
rm -f Cargo.lock

sed -e '/^[[:space:]]*\(fancy-regex\|regex\|rustc-hash\|bstr\)[[:space:]]*=/ s/= *"/= ">=/' \
  -e '/\bpyo3\b/ s/version *= *"/version = ">=/' \
  -i Cargo.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE
%{python3_sitearch}/tiktoken_ext/*

%changelog
%autochangelog
