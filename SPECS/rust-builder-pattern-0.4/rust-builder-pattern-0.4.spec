# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name builder-pattern
%global full_version 0.4.2
%global pkgname builder-pattern-0.4

Name:           rust-builder-pattern-0.4
Version:        0.4.2
Release:        %autorelease
Summary:        Rust crate "builder-pattern"
License:        MIT
URL:            https://github.com/SeokminHong/builder-pattern
#!RemoteAsset:  sha256:d85376b93d8efe18dd819f56505e33e7a9c0f93fb02bd761f8690026178ed6e5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(builder-pattern-macro-0.4/default) >= 0.4.2

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "builder-pattern"

%package     -n %{name}+futures
Summary:        Derivable macro for declaring a builder pattern - feature "futures" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/future) = %{version}
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust builder-pattern crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "future" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
