# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name virtue-next
%global full_version 0.1.3
%global pkgname virtue-next-0.1

Name:           rust-virtue-next-0.1
Version:        0.1.3
Release:        %autorelease
Summary:        Rust crate "virtue-next"
License:        MIT or Apache-2.0
URL:            https://github.com/Apich-Organization/virtue
#!RemoteAsset:  sha256:8d5208a9710a6ca1c2da0d64289a5dcca13deb05afdedf651f4e11bcd9fc53eb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "virtue-next"

%package     -n %{name}+proc-macro2
Summary:        Sinless derive macro helper - feature "proc-macro2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/proc-macro2) = %{version}

%description -n %{name}+proc-macro2
This metapackage enables feature "proc-macro2" for the Rust virtue-next crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
