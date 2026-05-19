# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tryfn
%global full_version 1.0.0
%global pkgname tryfn-1.0

Name:           rust-tryfn-1.0
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "tryfn"
License:        MIT OR Apache-2.0
URL:            https://github.com/assert-rs/snapbox/
#!RemoteAsset:  sha256:f68b00518dd6c69ee2289900b140e55dad068cb925678603bfa8d539f61ef6c1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ignore-0.4/default) >= 0.4.20
Requires:       crate(libtest-mimic-0.7/default) >= 0.7.0
Requires:       crate(snapbox-1.0) >= 1.0.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "tryfn"

%package     -n %{name}+color
Summary:        File-driven snapshot testing for a function - feature "color"
Requires:       crate(%{pkgname})
Requires:       crate(snapbox-1.0/color) >= 1.0.0
Provides:       crate(%{pkgname}/color)

%description -n %{name}+color
This metapackage enables feature "color" for the Rust tryfn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+color-auto
Summary:        File-driven snapshot testing for a function - feature "color-auto"
Requires:       crate(%{pkgname})
Requires:       crate(snapbox-1.0/color-auto) >= 1.0.0
Provides:       crate(%{pkgname}/color-auto)

%description -n %{name}+color-auto
This metapackage enables feature "color-auto" for the Rust tryfn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        File-driven snapshot testing for a function - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/color-auto)
Requires:       crate(%{pkgname}/diff)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tryfn crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+diff
Summary:        File-driven snapshot testing for a function - feature "diff"
Requires:       crate(%{pkgname})
Requires:       crate(snapbox-1.0/diff) >= 1.0.0
Provides:       crate(%{pkgname}/diff)

%description -n %{name}+diff
This metapackage enables feature "diff" for the Rust tryfn crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
