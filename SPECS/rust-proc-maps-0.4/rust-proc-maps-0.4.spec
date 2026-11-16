# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: A.Donz <avrova.minix@donz.si>
# SPDX-FileContributor: MMLA-org <https://github.com/MMLA-org>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Sponsored by cha86.dev <https://cha86.dev>

%global crate_name proc-maps
%global full_version 0.4.0
%global pkgname proc-maps-0.4

Name:           rust-proc-maps-0.4
Version:        0.4.0
Release:        %autorelease
Summary:        Rust crate "proc-maps"
License:        MIT
URL:            https://github.com/rbspy/proc-maps
#!RemoteAsset:  sha256:3db44c5aa60e193a25fcd93bb9ed27423827e8f118897866f946e2cf936c44fb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "proc-maps"

%package     -n %{name}+default
Summary:        Helper crate for getting virtual memory maps from processes - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/generate-bindings) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust proc-maps crate.

%package     -n %{name}+generate-bindings
Summary:        Helper crate for getting virtual memory maps from processes - feature "generate-bindings"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bindgen-0.70/default) >= 0.70.1
Provides:       crate(%{pkgname}/generate-bindings) = %{version}

%description -n %{name}+generate-bindings
This metapackage enables feature "generate-bindings" for the Rust proc-maps crate.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
