# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qlean
%global full_version 0.4.0
%global pkgname qlean-0.4

Name:           rust-qlean-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "qlean"
License:        MIT
URL:            https://github.com/buck2hub/qlean
#!RemoteAsset:  sha256:e675b362cafd35e0f05d53fb6022a0b70b656e293c870e1518c42be125778914
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.104
Requires:       crate(console-0.16/default) >= 0.16.6
Requires:       crate(dir-lock-0.5/default) >= 0.5.0
Requires:       crate(directories-6/default) >= 6.0.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(hex-0.4/default) >= 0.4.3
Requires:       crate(indicatif-0.18/default) >= 0.18.6
Requires:       crate(kvm-ioctls-0.25/default) >= 0.25.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(nanoid-0.5/default) >= 0.5.0
Requires:       crate(qapi-0.15/async-tokio-all) >= 0.15.0
Requires:       crate(qapi-0.15/default) >= 0.15.0
Requires:       crate(qapi-0.15/qmp) >= 0.15.0
Requires:       crate(rand-0.10/default) >= 0.10.2
Requires:       crate(reqwest-0.13/default) >= 0.13.5
Requires:       crate(reqwest-0.13/stream) >= 0.13.5
Requires:       crate(russh-0.63/default) >= 0.63.3
Requires:       crate(russh-sftp-3/default) >= 3.0.0
Requires:       crate(serde-1/default) >= 1.0.229
Requires:       crate(serde-1/derive) >= 1.0.229
Requires:       crate(serde-json-1/default) >= 1.0.151
Requires:       crate(serde-yml-0.0.13/default) >= 0.0.13
Requires:       crate(sha2-0.11/default) >= 0.11.0
Requires:       crate(shell-escape-0.1/default) >= 0.1.5
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/full) >= 1.0.0
Requires:       crate(tokio-util-0.7/default) >= 0.7.19
Requires:       crate(tokio-vsock-0.7/default) >= 0.7.2
Requires:       crate(tracing-0.1/default) >= 0.1.44
Requires:       crate(tracing-0.1/log) >= 0.1.44
Requires:       crate(tracing-indicatif-0.3/default) >= 0.3.14
Requires:       crate(walkdir-2/default) >= 2.5.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "qlean"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
