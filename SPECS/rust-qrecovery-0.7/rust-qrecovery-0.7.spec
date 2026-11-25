# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qrecovery
%global full_version 0.7.0
%global pkgname qrecovery-0.7

Name:           rust-qrecovery-0.7
Version:        0.7.0
Release:        %autorelease
Summary:        Rust crate "qrecovery"
License:        Apache-2.0
URL:            https://github.com/genmeta/dquic
#!RemoteAsset:  sha256:51eac3d871931d94a867e50c54d58fabbfb1c8d893bd48e6a95f12ebaf87bf7a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytes-1/default) >= 1.0.0
Requires:       crate(derive-more-2/default) >= 2.0.0
Requires:       crate(derive-more-2/deref) >= 2.0.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(qbase-0.7/default) >= 0.7.0
Requires:       crate(qevent-0.7/default) >= 0.7.0
Requires:       crate(thiserror-2/default) >= 2.0.20
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/time) >= 1.0.0
Requires:       crate(tracing-0.1/default) >= 0.1.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/test-util) = %{version}

%description
Source code for takopackized Rust crate "qrecovery"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
