# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qtransport
%global full_version 0.1.0
%global pkgname qtransport-0.1

Name:           rust-qtransport-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "qtransport"
License:        Apache-2.0
URL:            https://github.com/genmeta/dquic
#!RemoteAsset:  sha256:3fff22111657b3a094a75403ec051c0dcd1ee83b3c7fe28983469a2617c5f439
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(dashmap-6/default) >= 6.0.0
Requires:       crate(derive-more-2/default) >= 2.0.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(qbase-0.7/default) >= 0.7.0
Requires:       crate(qcongestion-0.7/default) >= 0.7.0
Requires:       crate(qevent-0.7/default) >= 0.7.0
Requires:       crate(qprotocol-0.7/default) >= 0.7.0
Requires:       crate(qrecovery-0.7/default) >= 0.7.0
Requires:       crate(qtls-0.1/default) >= 0.1.0
Requires:       crate(smallvec-1/const-generics) >= 1.0.0
Requires:       crate(smallvec-1/const-new) >= 1.0.0
Requires:       crate(smallvec-1/default) >= 1.0.0
Requires:       crate(smallvec-1/union) >= 1.0.0
Requires:       crate(thiserror-2/default) >= 2.0.20
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/macros) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Requires:       crate(tokio-1/sync) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "qtransport"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
