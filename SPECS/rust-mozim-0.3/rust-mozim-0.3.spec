# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mozim
%global full_version 0.3.1
%global pkgname mozim-0.3

Name:           rust-mozim-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "mozim"
License:        Apache-2.0
URL:            https://github.com/nispor/mozim
#!RemoteAsset:  sha256:f0437e58b082a444d57ee1e67eff5f5b98e4c3c64063bffc447ac9ae29a5ca3a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(etherparse-0.19/default) >= 0.19.0
Requires:       crate(futures-0.3/std) >= 0.3.0
Requires:       crate(libc-0.2/default) >= 0.2.132
Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(nix-0.30/default) >= 0.30.0
Requires:       crate(nix-0.30/event) >= 0.30.0
Requires:       crate(nix-0.30/fs) >= 0.30.0
Requires:       crate(nix-0.30/poll) >= 0.30.0
Requires:       crate(nix-0.30/socket) >= 0.30.0
Requires:       crate(nix-0.30/time) >= 0.30.0
Requires:       crate(rand-0.9/std) >= 0.9.0
Requires:       crate(rand-0.9/std-rng) >= 0.9.0
Requires:       crate(rand-0.9/thread-rng) >= 0.9.0
Requires:       crate(tokio-1/default) >= 1.19.0
Requires:       crate(tokio-1/macros) >= 1.19.0
Requires:       crate(tokio-1/net) >= 1.19.0
Requires:       crate(tokio-1/rt) >= 1.19.0
Requires:       crate(tokio-1/time) >= 1.19.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "mozim"

%package     -n %{name}+netlink
Summary:        DHCP Client Library - feature "netlink" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rtnetlink-0.18/default) >= 0.18.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/netlink) = %{version}

%description -n %{name}+netlink
This metapackage enables feature "netlink" for the Rust mozim crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
