# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tokenizers

Name:           python-%{srcname}
Version:        0.22.2
Release:        %autorelease
Summary:        Fast, state-of-the-art tokenizers optimized for research and production
License:        Apache-2.0
URL:            https://pypi.org/project/tokenizers/
VCS:            git:https://github.com/huggingface/tokenizers
#!RemoteAsset:  sha256:473b83b915e547aa366d1eee11806deaf419e17be16310ac0a14077f1e28f917
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Drop test-only dependencies to keep the offline build closure minimal.
Patch2000:      2000-fix-cargo.patch
Patch2001:      2001-fix-bindings-cargo.patch

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(maturin)
BuildRequires:  python3dist(huggingface-hub)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(ahash-0.8/default)
BuildRequires:  crate(ahash-0.8/serde)
BuildRequires:  crate(aho-corasick-1) >= 1.1
BuildRequires:  crate(aho-corasick-1/default)
BuildRequires:  crate(compact-str-0.9/default)
BuildRequires:  crate(compact-str-0.9/serde)
BuildRequires:  crate(dary-heap-0.3/default)
BuildRequires:  crate(dary-heap-0.3/serde)
BuildRequires:  crate(derive-builder-0.20/default)
BuildRequires:  crate(env-logger-0.11/default)
BuildRequires:  crate(esaxx-rs-0.1/cpp)
BuildRequires:  crate(fancy-regex-0.14/default)
BuildRequires:  crate(getrandom-0.3/default)
BuildRequires:  crate(hf-hub-0.4/ureq)
BuildRequires:  crate(indicatif-0.18/default)
BuildRequires:  crate(itertools-0.14/default)
BuildRequires:  crate(libc-0.2/default)
BuildRequires:  crate(log-0.4/default)
BuildRequires:  crate(macro-rules-attribute-0.2/default)
BuildRequires:  crate(monostate-0.1/default)
BuildRequires:  crate(ndarray-0.16/default)
BuildRequires:  crate(numpy-0.26/default)
BuildRequires:  crate(onig-6/default)
BuildRequires:  crate(once-cell-1/default)
BuildRequires:  crate(paste-1/default)
BuildRequires:  crate(pyo3-0.26/abi3)
BuildRequires:  crate(pyo3-0.26/abi3-py39)
BuildRequires:  crate(pyo3-0.26/default)
BuildRequires:  crate(pyo3-0.26/py-clone)
BuildRequires:  crate(pyo3-async-runtimes-0.26) >= 0.26
BuildRequires:  crate(pyo3-async-runtimes-0.26/default)
BuildRequires:  crate(pyo3-async-runtimes-0.26/tokio-runtime)
BuildRequires:  crate(pkg-config-0.3/default) >= 0.3.33
BuildRequires:  crate(rand-0.9/default)
BuildRequires:  crate(rayon-1/default)
BuildRequires:  crate(rayon-cond-0.4/default)
BuildRequires:  crate(regex-1/default)
BuildRequires:  crate(regex-syntax-0.8/default)
BuildRequires:  crate(serde-1/default)
BuildRequires:  crate(serde-1/derive)
BuildRequires:  crate(serde-1/rc)
BuildRequires:  crate(serde-json-1/default)
BuildRequires:  crate(spm-precompiled-0.1/default)
BuildRequires:  crate(thiserror-2/default)
BuildRequires:  crate(tokio-1/default)
BuildRequires:  crate(tokio-1/macros)
BuildRequires:  crate(tokio-1/rt)
BuildRequires:  crate(tokio-1/rt-multi-thread)
BuildRequires:  crate(tokio-1/signal)
BuildRequires:  crate(unicode-categories-0.1/default)
BuildRequires:  crate(unicode-normalization-alignments-0.1/default)
BuildRequires:  crate(unicode-segmentation-1/default)

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Tokenizers provides fast and production-ready tokenization implementations for
modern natural language processing workloads.

%prep -a
%rust_setup_registry
rm -f bindings/python/Cargo.lock

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc tokenizers/README.md
%license tokenizers/LICENSE

%changelog
%autochangelog
