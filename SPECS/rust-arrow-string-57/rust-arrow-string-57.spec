# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name arrow-string
%global full_version 57.3.1
%global pkgname arrow-string-57

Name:           rust-arrow-string-57
Version:        57.3.1
Release:        %autorelease
Summary:        Rust crate "arrow-string"
License:        Apache-2.0
URL:            https://github.com/apache/arrow-rs
#!RemoteAsset:  sha256:b493e99162e5764077e7823e50ba284858d365922631c7aaefe9487b1abd02c2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrow-array-57/default) >= 57.3.1
Requires:       crate(arrow-buffer-57/default) >= 57.3.1
Requires:       crate(arrow-data-57/default) >= 57.3.1
Requires:       crate(arrow-schema-57/default) >= 57.3.1
Requires:       crate(arrow-select-57/default) >= 57.3.1
Requires:       crate(memchr-2/default) >= 2.7.4
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Requires:       crate(regex-1/perf) >= 1.7.0
Requires:       crate(regex-1/std) >= 1.7.0
Requires:       crate(regex-1/unicode) >= 1.7.0
Requires:       crate(regex-syntax-0.8/unicode) >= 0.8.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "arrow-string"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
