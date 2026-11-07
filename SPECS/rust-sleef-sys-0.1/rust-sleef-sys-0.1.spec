# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sleef-sys
%global full_version 0.1.2
%global pkgname sleef-sys-0.1

Name:           rust-sleef-sys-0.1
Version:        0.1.2
Release:        %autorelease
Summary:        Rust crate "sleef-sys"
License:        MIT OR Apache-2.0
URL:            https://github.com/gnzlbg/sleef-sys
#!RemoteAsset:  sha256:7bce803eaa6c2fbe971573c86cafae41f391d8212400b87da8429ec0bcc001a1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bindgen-0.46) >= 0.46.0
Requires:       crate(cfg-if-0.1/default) >= 0.1.0
Requires:       crate(cmake-0.1) >= 0.1.0
Requires:       crate(env-logger-0.6) >= 0.6.0
Requires:       crate(libc-0.2) >= 0.2.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/dft) = %{version}

%description
Source code for takopackized Rust crate "sleef-sys"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
