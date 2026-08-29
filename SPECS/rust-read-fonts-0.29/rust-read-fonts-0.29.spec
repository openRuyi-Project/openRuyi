# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name read-fonts
%global full_version 0.29.3
%global pkgname read-fonts-0.29

Name:           rust-read-fonts-0.29
Version:        0.29.3
Release:        %autorelease
Summary:        Rust crate "read-fonts"
License:        MIT OR Apache-2.0
URL:            https://github.com/googlefonts/fontations
#!RemoteAsset:  sha256:04ca636dac446b5664bd16c069c00a9621806895b8bb02c2dc68542b23b8f25d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytemuck-1/default) >= 1.13.1
Requires:       crate(font-types-0.9/bytemuck) >= 0.9.0
Requires:       crate(font-types-0.9/default) >= 0.9.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/codegen-test) = %{version}
Provides:       crate(%{pkgname}/ift) = %{version}
Provides:       crate(%{pkgname}/scaler-test) = %{version}
Provides:       crate(%{pkgname}/spec-next) = %{version}

%description
Source code for takopackized Rust crate "read-fonts"

%package     -n %{name}+libm
Summary:        Reading OpenType font files - feature "libm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(core-maths-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/libm) = %{version}

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust read-fonts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Reading OpenType font files - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(font-types-0.9/bytemuck) >= 0.9.0
Requires:       crate(font-types-0.9/serde) >= 0.9.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust read-fonts crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Reading OpenType font files - feature "std" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(font-types-0.9/bytemuck) >= 0.9.0
Requires:       crate(font-types-0.9/std) >= 0.9.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/experimental-traverse) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust read-fonts crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "experimental_traverse" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
