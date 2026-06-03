# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name virtue
%global full_version 0.0.18
%global pkgname virtue-0.0.18

Name:           rust-virtue-0.0.18
Version:        0.0.18
Release:        %autorelease
Summary:        Rust crate "virtue"
License:        MIT
URL:            https://github.com/bincode-org/virtue
#!RemoteAsset:  sha256:051eb1abcf10076295e815102942cc58f9d5e3b4560e46e53c21e8ff6f3af7b1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "virtue"

%package     -n %{name}+proc-macro2
Summary:        Sinless derive macro helper - feature "proc-macro2"
Requires:       crate(%{pkgname})
Requires:       crate(proc-macro2-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/proc-macro2)

%description -n %{name}+proc-macro2
This metapackage enables feature "proc-macro2" for the Rust virtue crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
