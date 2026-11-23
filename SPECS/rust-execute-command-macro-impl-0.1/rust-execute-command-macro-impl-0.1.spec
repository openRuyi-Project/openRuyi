# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name execute-command-macro-impl
%global full_version 0.1.12
%global pkgname execute-command-macro-impl-0.1

Name:           rust-execute-command-macro-impl-0.1
Version:        0.1.12
Release:        %autorelease
Summary:        Rust crate "execute-command-macro-impl"
License:        MIT
URL:            https://magiclen.org/execute
#!RemoteAsset:  sha256:57dd896da3fbb77138059b015c013459d96063c66bcdd3b9094ff2e9d3f19a47
Source:         https://static.crates.io/crates/execute-command-macro-impl/0.1.12/download#/rust-execute-command-macro-impl-0.1-0.1.12.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(execute-command-tokens-0.1/default) >= 0.1.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "execute-command-macro-impl"

%package     -n %{name}+default
Summary:        Create `Command` instances using the `command!` macro - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust execute-command-macro-impl crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
