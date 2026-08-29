# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname libcst

Name:           python-%{srcname}
Version:        1.8.6
Release:        %autorelease
Summary:        Concrete syntax tree with AST-like properties for Python
License:        MIT AND PSF-2.0
URL:            https://github.com/Instagram/LibCST
#!RemoteAsset:  sha256:f729c37c9317126da9475bdd06a7208eb52fcbd180a6341648b45a56b4ba708b
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  -l %{srcname}
# libcst.tests* and libcst.codemod.tests* are upstream test modules, not runtime
# modules required by the installed library import check.
BuildOption(check):  -e "libcst.tests*" -e "libcst.codemod.tests*"

BuildRequires:  crate(annotate-snippets-0.11/default) >= 0.11.5
BuildRequires:  crate(memchr-2/default) >= 2.7.4
BuildRequires:  crate(paste-1/default) >= 1.0.15
BuildRequires:  crate(peg-0.8/default) >= 0.8.5
BuildRequires:  crate(proc-macro2-1/default)
BuildRequires:  crate(pyo3-0.26/default) >= 0.26.0
BuildRequires:  crate(pyo3-0.26/extension-module) >= 0.26.0
BuildRequires:  crate(quote-1/default)
BuildRequires:  crate(regex-1/default) >= 1.11.2
BuildRequires:  crate(syn-2/default)
BuildRequires:  crate(thiserror-2/default) >= 2.0.12
BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pyyaml-ft) >= 8
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
LibCST provides a concrete syntax tree for Python source code with AST-like
properties and codemod tooling.

%prep -a
%rust_setup_registry

rm -f native/Cargo.lock
# setuptools-rust invokes cargo metadata, which resolves dev/bench
# dependencies even though this package only builds the extension module.
perl -0pi -e 's/\n\[dev-dependencies\].*?(?=\n\[\[bench\]\]|\n\[package\.metadata|\z)//s;
              s/\n\[\[bench\]\].*?(?=\n\[\[bench\]\]|\n\[package\.metadata|\z)//gs' \
  native/libcst/Cargo.toml
perl -0pi -e 's/\n\[dev-dependencies\].*?\z//s' native/libcst_derive/Cargo.toml
sed -e '/^[[:space:]]*\\(annotate-snippets\\|memchr\\|paste\\|peg\\|regex\\|thiserror\\)[[:space:]]*=/ s/= *"/= ">=/' \
  -e '/\\bpyo3\\b/ s/version *= *"/version = ">=/' \
  -e '/^[[:space:]]*\\(quote\\|syn\\)[[:space:]]*=/ s/= *"/= ">=/' \
  -i native/libcst/Cargo.toml native/libcst_derive/Cargo.toml

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.rst CHANGELOG.md CODE_OF_CONDUCT.md
%license LICENSE

%changelog
%autochangelog
