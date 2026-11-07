# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mio
%global full_version 0.6.23
%global pkgname mio-0.6

Name:           rust-mio-0.6
Version:        0.6.23
Release:        %autorelease
Summary:        Rust crate "mio"
License:        MIT
URL:            https://github.com/tokio-rs/mio
#!RemoteAsset:  sha256:4afd66f5b91bf2a3bc13fad0e21caedac168ca4c707504e75585648ae80e4cc4
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-0.1/default) >= 0.1.9
Requires:       crate(fuchsia-zircon-0.3/default) >= 0.3.2
Requires:       crate(fuchsia-zircon-sys-0.3/default) >= 0.3.2
Requires:       crate(iovec-0.1/default) >= 0.1.1
Requires:       crate(kernel32-sys-0.2/default) >= 0.2.0
Requires:       crate(libc-0.2/default) >= 0.2.54
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(miow-0.2/default) >= 0.2.2
Requires:       crate(net2-0.2/default) >= 0.2.36
Requires:       crate(slab-0.4/default) >= 0.4.0
Requires:       crate(winapi-0.2/default) >= 0.2.6

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/with-deprecated) = %{version}

%description
Source code for takopackized Rust crate "mio"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
