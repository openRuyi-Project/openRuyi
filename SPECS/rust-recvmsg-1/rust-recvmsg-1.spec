# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name recvmsg
%global full_version 1.0.0
%global pkgname recvmsg-1

Name:           rust-recvmsg-1
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "recvmsg"
License:        0BSD
URL:            FIXME
#!RemoteAsset:  sha256:d3edd4d5d42c92f0a659926464d4cce56b562761267ecf0f469d85b7de384175
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "recvmsg"

%package     -n %{name}+libc
Summary:        Traits for receiving datagrams reliably, without truncation - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.150
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust recvmsg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std-net
Summary:        Traits for receiving datagrams reliably, without truncation - feature "std_net"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/windows-sys) = %{version}
Provides:       crate(%{pkgname}/std-net) = %{version}

%description -n %{name}+std-net
This metapackage enables feature "std_net" for the Rust recvmsg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Traits for receiving datagrams reliably, without truncation - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std-net) = %{version}
Requires:       crate(tokio-1/default) >= 1.34.0
Requires:       crate(tokio-1/net) >= 1.34.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust recvmsg crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+windows-sys
Summary:        Traits for receiving datagrams reliably, without truncation - feature "windows-sys"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(windows-sys-0.52/default) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-networking-winsock) >= 0.52.0
Provides:       crate(%{pkgname}/windows-sys) = %{version}

%description -n %{name}+windows-sys
This metapackage enables feature "windows-sys" for the Rust recvmsg crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
