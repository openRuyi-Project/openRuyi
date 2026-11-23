# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name proc-macro2-diagnostics
%global full_version 0.10.1
%global pkgname proc-macro2-diagnostics-0.10

Name:           rust-proc-macro2-diagnostics-0.10
Version:        0.10.1
Release:        %autorelease
Summary:        Rust crate "proc-macro2-diagnostics"
License:        MIT OR Apache-2.0
URL:            https://github.com/SergioBenitez/proc-macro2-diagnostics
#!RemoteAsset:  sha256:af066a9c399a26e020ada66a034357a868728e72cd426f3adcd35f80d88d88c8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

Patch2000:      2000-use-stable-yansi.patch

BuildRequires:  rust-rpm-macros

Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(version-check-0.9) >= 0.9.4
Requires:       crate(yansi-1/default) >= 1.0.1

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "proc-macro2-diagnostics"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
