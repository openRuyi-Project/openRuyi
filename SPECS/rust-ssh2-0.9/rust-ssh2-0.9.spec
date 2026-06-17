# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ssh2
%global full_version 0.9.5
%global pkgname ssh2-0.9

Name:           rust-ssh2-0.9
Version:        0.9.5
Release:        %autorelease
Summary:        Rust crate "ssh2"
License:        MIT OR Apache-2.0
URL:            https://github.com/alexcrichton/ssh2-rs
#!RemoteAsset:  sha256:2f84d13b3b8a0d4e91a2629911e951db1bb8671512f5c09d7d4ba34500ba68c8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.0.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(libssh2-sys-0.3/default) >= 0.3.1
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "ssh2"

%package     -n %{name}+openssl-on-win32
Summary:        Bindings to libssh2 for interacting with SSH servers and executing remote commands, forwarding local ports, etc - feature "openssl-on-win32"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libssh2-sys-0.3/openssl-on-win32) >= 0.3.1
Provides:       crate(%{pkgname}/openssl-on-win32) = %{version}

%description -n %{name}+openssl-on-win32
This metapackage enables feature "openssl-on-win32" for the Rust ssh2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored-openssl
Summary:        Bindings to libssh2 for interacting with SSH servers and executing remote commands, forwarding local ports, etc - feature "vendored-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libssh2-sys-0.3/vendored-openssl) >= 0.3.1
Provides:       crate(%{pkgname}/vendored-openssl) = %{version}

%description -n %{name}+vendored-openssl
This metapackage enables feature "vendored-openssl" for the Rust ssh2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
