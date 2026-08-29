# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name skrifa
%global full_version 0.31.3
%global pkgname skrifa-0.31

Name:           rust-skrifa-0.31
Version:        0.31.3
Release:        %autorelease
Summary:        Rust crate "skrifa"
License:        MIT OR Apache-2.0
URL:            https://github.com/googlefonts/fontations
#!RemoteAsset:  sha256:dbeb4ca4399663735553a09dd17ce7e49a0a0203f03b706b39628c4d913a8607
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytemuck-1/default) >= 1.13.1
Requires:       crate(read-fonts-0.29) >= 0.29.2

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/autohint-shaping) = %{version}

%description
Source code for takopackized Rust crate "skrifa"

%package     -n %{name}+default
Summary:        Metadata reader and glyph scaler for OpenType fonts - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/autohint-shaping) = %{version}
Requires:       crate(%{pkgname}/traversal) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust skrifa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        Metadata reader and glyph scaler for OpenType fonts - feature "libm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(core-maths-0.1/default) >= 0.1.0
Requires:       crate(read-fonts-0.29/libm) >= 0.29.2
Provides:       crate(%{pkgname}/libm) = %{version}

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust skrifa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spec-next
Summary:        Metadata reader and glyph scaler for OpenType fonts - feature "spec_next"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(read-fonts-0.29/spec-next) >= 0.29.2
Provides:       crate(%{pkgname}/spec-next) = %{version}

%description -n %{name}+spec-next
This metapackage enables feature "spec_next" for the Rust skrifa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Metadata reader and glyph scaler for OpenType fonts - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(read-fonts-0.29/std) >= 0.29.2
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust skrifa crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+traversal
Summary:        Metadata reader and glyph scaler for OpenType fonts - feature "traversal"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(read-fonts-0.29/experimental-traverse) >= 0.29.2
Provides:       crate(%{pkgname}/traversal) = %{version}

%description -n %{name}+traversal
This metapackage enables feature "traversal" for the Rust skrifa crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
