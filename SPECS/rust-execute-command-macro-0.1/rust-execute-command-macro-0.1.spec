# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name execute-command-macro
%global full_version 0.1.1
%global pkgname execute-command-macro-0.1

Name:           rust-execute-command-macro-0.1
Version:        0.1.1
Release:        %autorelease
Summary:        Rust crate "execute-command-macro"
License:        MIT
URL:            https://magiclen.org/execute
#!RemoteAsset:  sha256:2b4353abd5da2fe2323abcb6c111d1dc7e67a4ba89c992e5af5cb55274379eff
Source:         https://static.crates.io/crates/execute-command-macro/0.1.1/download#/rust-execute-command-macro-0.1-0.1.1.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(execute-command-macro-impl-0.1/default) >= 0.1.0
Requires:       crate(proc-macro-hack-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "execute-command-macro"

%package     -n %{name}+default
Summary:        Create `Command` instances using the `command!` macro or the `command_args!` marco - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust execute-command-macro crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
