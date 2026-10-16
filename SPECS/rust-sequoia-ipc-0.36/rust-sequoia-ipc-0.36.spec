# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-ipc
%global full_version 0.36.1
%global pkgname sequoia-ipc-0.36

Name:           rust-sequoia-ipc-0.36
Version:        0.36.1
Release:        %autorelease
Summary:        Rust crate "sequoia-ipc"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:0770bf144d96733921b4647cd4b243cbebf032127676a441e3ebe702c0768c54
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.18
Requires:       crate(capnp-rpc-0.25/default) >= 0.25.0
Requires:       crate(capnpc-0.25) >= 0.25.0
Requires:       crate(ctor-0.2/default) >= 0.2.0
Requires:       crate(dirs-5/default) >= 5.0.0
Requires:       crate(fs2-0.4/default) >= 0.4.2
Requires:       crate(lalrpop-0.17) >= 0.17.0
Requires:       crate(lalrpop-util-0.17/default) >= 0.17.0
Requires:       crate(libc-0.2/default) >= 0.2.66
Requires:       crate(memsec-0.5) >= 0.5.0
Requires:       crate(sequoia-openpgp-2) >= 2.0.0
Requires:       crate(socket2-0.6/default) >= 0.6.0
Requires:       crate(tempfile-3/default) >= 3.1.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(tokio-1/default) >= 1.19.0
Requires:       crate(tokio-1/io-util) >= 1.19.0
Requires:       crate(tokio-1/net) >= 1.19.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.19.0
Requires:       crate(tokio-util-0.7/compat) >= 0.7.0
Requires:       crate(tokio-util-0.7/default) >= 0.7.0
Requires:       crate(winapi-0.3/winsock2) >= 0.3.8

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sequoia-ipc"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
