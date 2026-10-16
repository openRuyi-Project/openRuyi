# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-gpg-agent
%global full_version 0.6.2
%global pkgname sequoia-gpg-agent-0.6

Name:           rust-sequoia-gpg-agent-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "sequoia-gpg-agent"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:5c36b37720b61230507a953d9879eb0dd8c228d86948d37cba53ced942e862a1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.0
Requires:       crate(chrono-0.4/default) >= 0.4.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(lalrpop-0.17) >= 0.17.0
Requires:       crate(lalrpop-util-0.17/default) >= 0.17.0
Requires:       crate(libc-0.2/default) >= 0.2.152
Requires:       crate(sequoia-ipc-0.36) >= 0.36.0
Requires:       crate(sequoia-openpgp-2) >= 2.0.0
Requires:       crate(stfu8-0.2/default) >= 0.2.0
Requires:       crate(tempfile-3/default) >= 3.1.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.35.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sequoia-gpg-agent"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
