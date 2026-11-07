# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name fuchsia-zircon
%global full_version 0.3.3
%global pkgname fuchsia-zircon-0.3

Name:           rust-fuchsia-zircon-0.3
Version:        0.3.3
Release:        %autorelease
Summary:        Rust crate "fuchsia-zircon"
License:        BSD-3-Clause
URL:            https://fuchsia.googlesource.com/garnet/
#!RemoteAsset:  sha256:2e9763c69ebaae630ba35f74888db465e49e259ba1bc0eda7d06f4a067615d82
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-1/default) >= 1.0.0
Requires:       crate(fuchsia-zircon-sys-0.3/default) >= 0.3.3

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "fuchsia-zircon"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
