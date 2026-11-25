# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qresolve
%global full_version 0.9.0
%global pkgname qresolve-0.9

Name:           rust-qresolve-0.9
Version:        0.9.0
Release:        %autorelease
Summary:        Rust crate "qresolve"
License:        Apache-2.0
URL:            https://github.com/genmeta/dquic
#!RemoteAsset:  sha256:304f2a3ffacb1a2516044b13b3a8e95a7e91fd5b87dafb4a37a7cb23086a7cbd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dns-lookup-4/default) >= 4.0.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(qbase-0.7/default) >= 0.7.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "qresolve"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
