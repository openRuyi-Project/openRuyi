# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quinn-udp
%global full_version 0.4.1
%global pkgname quinn-udp-0.4

Name:           rust-quinn-udp-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "quinn-udp"
License:        MIT OR Apache-2.0
URL:            https://github.com/quinn-rs/quinn
#!RemoteAsset:  sha256:055b4e778e8feb9f93c4e439f71dc2156ef13360b432b799e179a8c4cdf0b1d7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.113
Requires:       crate(socket2-0.5/default) >= 0.5.0
Requires:       crate(tracing-0.1/default) >= 0.1.10
Requires:       crate(windows-sys-0.48/default) >= 0.48.0
Requires:       crate(windows-sys-0.48/win32-networking-winsock) >= 0.48.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "quinn-udp"

%package     -n %{name}+log
Summary:        UDP sockets with ECN information for the QUIC transport protocol - feature "log" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/log) >= 0.1.10
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust quinn-udp crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
