# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name resize
%global full_version 0.8.9
%global pkgname resize-0.8

Name:           rust-resize-0.8
Version:        0.8.9
Release:        %autorelease
Summary:        Rust crate "resize"
License:        MIT
URL:            https://github.com/PistonDevelopers/resize
#!RemoteAsset:  sha256:71725ecd5e0197b54fe859055b108688472ab6a358f8fbe5cee4a556b1b5bfea
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rgb-0.8) >= 0.8.52

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description
Source code for takopackized Rust crate "resize"

%package     -n %{name}+default
Summary:        Simple image resampling library in pure Rust - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/rayon) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust resize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-std
Summary:        Simple image resampling library in pure Rust - feature "no_std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(hashbrown-0.15/default) >= 0.15.0
Requires:       crate(libm-0.2/default) >= 0.2.16
Provides:       crate(%{pkgname}/no-std) = %{version}

%description -n %{name}+no-std
This metapackage enables feature "no_std" for the Rust resize crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rayon
Summary:        Simple image resampling library in pure Rust - feature "rayon"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(rayon-1/default) >= 1.11.0
Provides:       crate(%{pkgname}/rayon) = %{version}

%description -n %{name}+rayon
This metapackage enables feature "rayon" for the Rust resize crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
