# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name pest
%global full_version 2.8.6
%global pkgname pest-2

Name:           rust-pest-2
Version:        2.8.6
Release:        %autorelease
Summary:        Rust crate "pest"
License:        MIT OR Apache-2.0
URL:            https://pest.rs/
#!RemoteAsset:  sha256:e0848c601009d37dfa3430c4666e147e49cdcf1b92ecd3e63657d8a5f19da662
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ucd-trie-0.1) >= 0.1.5
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/const-prec-climber) = %{version}

%description
Source code for takopackized Rust crate "pest"

%package     -n %{name}+default
Summary:        Elegant Parser - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/memchr) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust pest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+memchr
Summary:        Elegant Parser - feature "memchr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2/default) >= 2.4.0
Provides:       crate(%{pkgname}/memchr) = %{version}

%description -n %{name}+memchr
This metapackage enables feature "memchr" for the Rust pest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+miette-error
Summary:        Elegant Parser - feature "miette-error"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pretty-print) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(miette-7/default) >= 7.2.0
Requires:       crate(miette-7/fancy) >= 7.2.0
Provides:       crate(%{pkgname}/miette-error) = %{version}

%description -n %{name}+miette-error
This metapackage enables feature "miette-error" for the Rust pest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pretty-print
Summary:        Elegant Parser - feature "pretty-print"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.145
Requires:       crate(serde-json-1/default) >= 1.0.85
Provides:       crate(%{pkgname}/pretty-print) = %{version}

%description -n %{name}+pretty-print
This metapackage enables feature "pretty-print" for the Rust pest crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Elegant Parser - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ucd-trie-0.1/std) >= 0.1.5
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust pest crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
