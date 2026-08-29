# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name csscolorparser
%global full_version 0.8.3
%global pkgname csscolorparser-0.8

Name:           rust-csscolorparser-0.8
Version:        0.8.3
Release:        %autorelease
Summary:        Rust crate "csscolorparser"
License:        MIT OR Apache-2.0
URL:            https://github.com/mazznoer/csscolorparser-rs
#!RemoteAsset:  sha256:199f851bd3cb5004c09474252c7f74e7c047441ed0979bf3688a7106a13da952
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2/libm) >= 0.2.19
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "csscolorparser"

%package     -n %{name}+cint
Summary:        CSS color parser library - feature "cint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cint-0.3/default) >= 0.3.1
Provides:       crate(%{pkgname}/cint) = %{version}

%description -n %{name}+cint
This metapackage enables feature "cint" for the Rust csscolorparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        CSS color parser library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/named-colors) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust csscolorparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+named-colors
Summary:        CSS color parser library - feature "named-colors"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-0.13/macros) >= 0.13.1
Requires:       crate(phf-0.13/uncased) >= 0.13.1
Requires:       crate(uncased-0.9) >= 0.9.10
Provides:       crate(%{pkgname}/named-colors) = %{version}

%description -n %{name}+named-colors
This metapackage enables feature "named-colors" for the Rust csscolorparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-rgb
Summary:        CSS color parser library - feature "rust-rgb"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rgb-0.8/default) >= 0.8.33
Provides:       crate(%{pkgname}/rust-rgb) = %{version}

%description -n %{name}+rust-rgb
This metapackage enables feature "rust-rgb" for the Rust csscolorparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        CSS color parser library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/derive) >= 1.0.139
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust csscolorparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        CSS color parser library - feature "std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-0.13/macros) >= 0.13.1
Requires:       crate(phf-0.13/std) >= 0.13.1
Requires:       crate(phf-0.13/uncased) >= 0.13.1
Requires:       crate(serde-1/derive) >= 1.0.139
Requires:       crate(serde-1/std) >= 1.0.139
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust csscolorparser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
