# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name starlark_syntax
%global full_version 0.14.2
%global pkgname starlark-syntax-0.14

Name:           rust-starlark-syntax-0.14
Version:        0.14.2
Release:        %autorelease
Summary:        Rust crate "starlark_syntax"
License:        Apache-2.0
URL:            https://github.com/facebook/starlark-rust
#!RemoteAsset:  sha256:7492c571c531e68099c911cfd909d32659f1cc0910cf3adee9fce66e39d21f14
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(allocative-0.3/default) >= 0.3.6
Requires:       crate(annotate-snippets-0.9/default) >= 0.9.0
Requires:       crate(anyhow-1/default) >= 1.0.102
Requires:       crate(derivative-2/default) >= 2.2.0
Requires:       crate(derive-more-1/default) >= 1.0.0
Requires:       crate(derive-more-1/full) >= 1.0.0
Requires:       crate(dupe-0.9/default) >= 0.9.1
Requires:       crate(logos-0.15/default) >= 0.15.0
Requires:       crate(lsp-types-0.97/default) >= 0.97.0
Requires:       crate(memchr-2/default) >= 2.8.0
Requires:       crate(num-bigint-0.4/default) >= 0.4.6
Requires:       crate(num-bigint-0.4/serde) >= 0.4.6
Requires:       crate(num-traits-0.2/default) >= 0.2.0
Requires:       crate(once-cell-1/default) >= 1.21.4
Requires:       crate(pagable-0.4/default) >= 0.4.1
Requires:       crate(starlark-map-0.14/default) >= 0.14.2
Requires:       crate(thiserror-2/default) >= 2.0.18

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "starlark_syntax"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
