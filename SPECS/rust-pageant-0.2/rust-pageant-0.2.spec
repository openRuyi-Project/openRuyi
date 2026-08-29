# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pageant
%global full_version 0.2.1
%global pkgname pageant-0.2

Name:           rust-pageant-0.2
Version:        0.2.1
Release:        %autorelease
Summary:        Rust crate "pageant"
License:        Apache-2.0
URL:            https://github.com/warp-tech/russh
#!RemoteAsset:  sha256:4f3a5ae18f65a85c67a77d18d42d3606c07948e3c17c1e5f74852b26589e88a5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base16ct-1/alloc) >= 1.0.0
Requires:       crate(base16ct-1/default) >= 1.0.0
Requires:       crate(byteorder-1/default) >= 1.4.0
Requires:       crate(bytes-1/default) >= 1.7.0
Requires:       crate(delegate-0.13/default) >= 0.13.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(log-0.4/default) >= 0.4.11
Requires:       crate(rand-0.10/default) >= 0.10.0
Requires:       crate(rand-0.10/thread-rng) >= 0.10.0
Requires:       crate(thiserror-2/default) >= 2.0.18
Requires:       crate(tokio-1/default) >= 1.17.0
Requires:       crate(windows-0.62/default) >= 0.62.0
Requires:       crate(windows-0.62/win32-security) >= 0.62.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "pageant"

%package     -n %{name}+default
Summary:        Pageant SSH agent transport client - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/namedpipes) = %{version}
Requires:       crate(%{pkgname}/wmmessage) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust pageant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+namedpipes
Summary:        Pageant SSH agent transport client - feature "namedpipes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sha2-0.11/default) >= 0.11.0
Requires:       crate(sha2-0.11/oid) >= 0.11.0
Requires:       crate(tokio-1/net) >= 1.17.0
Requires:       crate(tokio-1/time) >= 1.17.0
Requires:       crate(windows-0.62/win32-security) >= 0.62.0
Requires:       crate(windows-0.62/win32-security-authentication-identity) >= 0.62.0
Requires:       crate(windows-0.62/win32-security-cryptography) >= 0.62.0
Requires:       crate(windows-strings-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/namedpipes) = %{version}

%description -n %{name}+namedpipes
This metapackage enables feature "namedpipes" for the Rust pageant crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+wmmessage
Summary:        Pageant SSH agent transport client - feature "wmmessage"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/io-util) >= 1.17.0
Requires:       crate(tokio-1/rt) >= 1.17.0
Requires:       crate(windows-0.62/win32-security) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-dataexchange) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-memory) >= 0.62.0
Requires:       crate(windows-0.62/win32-system-threading) >= 0.62.0
Requires:       crate(windows-0.62/win32-ui-windowsandmessaging) >= 0.62.0
Provides:       crate(%{pkgname}/wmmessage) = %{version}

%description -n %{name}+wmmessage
This metapackage enables feature "wmmessage" for the Rust pageant crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
