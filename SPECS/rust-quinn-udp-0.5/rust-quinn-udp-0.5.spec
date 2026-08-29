# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name quinn-udp
%global full_version 0.5.14
%global pkgname quinn-udp-0.5

Name:           rust-quinn-udp-0.5
Version:        0.5.14
Release:        %autorelease
Summary:        Rust crate "quinn-udp"
License:        MIT OR Apache-2.0
URL:            https://github.com/quinn-rs/quinn
#!RemoteAsset:  sha256:addec6a0dcad8a8d96a771f815f0eaf55f9d1805756410b39f5fa81332574cbd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-aliases-0.2) >= 0.2.0
Requires:       crate(libc-0.2/default) >= 0.2.158
Requires:       crate(once-cell-1/default) >= 1.19.0
Requires:       crate(socket2-0.5/default) >= 0.5.0
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-networking-winsock) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-system-io) >= 0.52.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/fast-apple-datapath) = %{version}

%description
Source code for takopackized Rust crate "quinn-udp"

%package     -n %{name}+default
Summary:        UDP sockets with ECN information for the QUIC transport protocol - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/log) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust quinn-udp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+direct-log
Summary:        UDP sockets with ECN information for the QUIC transport protocol - feature "direct-log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/direct-log) = %{version}

%description -n %{name}+direct-log
This metapackage enables feature "direct-log" for the Rust quinn-udp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        UDP sockets with ECN information for the QUIC transport protocol - feature "log"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/log) >= 0.1.10
Requires:       crate(tracing-0.1/std) >= 0.1.10
Provides:       crate(%{pkgname}/log) = %{version}

%description -n %{name}+log
This metapackage enables feature "log" for the Rust quinn-udp crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        UDP sockets with ECN information for the QUIC transport protocol - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tracing-0.1/std) >= 0.1.10
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust quinn-udp crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
