# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sequoia-keystore-gpg-agent
%global full_version 0.5.0
%global pkgname sequoia-keystore-gpg-agent-0.5

Name:           rust-sequoia-keystore-gpg-agent-0.5
Version:        0.5.0
Release:        %autorelease
Summary:        Rust crate "sequoia-keystore-gpg-agent"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:7ad901f1f1d88b38f5f5738d5bf2b80136ec44e94a40716193be0bbf3314df2b
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.18
Requires:       crate(async-trait-0.1/default) >= 0.1.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(log-0.4/default) >= 0.4.17
Requires:       crate(openpgp-cert-d-0.3) >= 0.3.4
Requires:       crate(sequoia-gpg-agent-0.6) >= 0.6.0
Requires:       crate(sequoia-ipc-0.36) >= 0.36.0
Requires:       crate(sequoia-keystore-backend-0.7/default) >= 0.7.0
Requires:       crate(sequoia-openpgp-2) >= 2.0.0
Requires:       crate(tokio-1/default) >= 1.19.0
Requires:       crate(tokio-1/io-util) >= 1.19.0
Requires:       crate(tokio-1/net) >= 1.19.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.19.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "sequoia-keystore-gpg-agent"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
