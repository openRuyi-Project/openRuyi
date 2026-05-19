# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pest
%global full_version 2.8.2
%global pkgname pest-2.0

Name:           rust-pest-2.0
Version:        2.8.2
Release:        %autorelease
Summary:        Rust crate "pest"
License:        MIT OR Apache-2.0
URL:            https://pest.rs/
#!RemoteAsset:  sha256:21e0a3a33733faeaf8651dfee72dd0f388f0c8e5ad496a3478fa5a922f49cfa8
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ucd-trie-0.1) >= 0.1.7
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/const-prec-climber)

%description
Source code for takopackized Rust crate "pest"

%package     -n %{name}+default
Summary:        Elegant Parser - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/memchr)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust pest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memchr
Summary:        Elegant Parser - feature "memchr"
Requires:       crate(%{pkgname})
Requires:       crate(memchr-2.0/default) >= 2.8.0
Provides:       crate(%{pkgname}/memchr)

%description -n %{name}+memchr
This metapackage enables feature "memchr" for the Rust pest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+miette-error
Summary:        Elegant Parser - feature "miette-error"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pretty-print)
Requires:       crate(%{pkgname}/std)
Requires:       crate(miette-7.0/default) >= 7.2.0
Requires:       crate(miette-7.0/fancy) >= 7.2.0
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname}/miette-error)

%description -n %{name}+miette-error
This metapackage enables feature "miette-error" for the Rust pest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pretty-print
Summary:        Elegant Parser - feature "pretty-print"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.145
Requires:       crate(serde-json-1.0/default) >= 1.0.85
Provides:       crate(%{pkgname}/pretty-print)

%description -n %{name}+pretty-print
This metapackage enables feature "pretty-print" for the Rust pest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Elegant Parser - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Requires:       crate(ucd-trie-0.1/std) >= 0.1.7
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pest crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
