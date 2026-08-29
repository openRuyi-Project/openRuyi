# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name csscolorparser
%global full_version 0.6.2
%global pkgname csscolorparser-0.6

Name:           rust-csscolorparser-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "csscolorparser"
License:        MIT OR Apache-2.0
URL:            https://github.com/mazznoer/csscolorparser-rs
#!RemoteAsset:  sha256:eb2a7d3066da2de787b7f032c736763eb7ae5d355f81a68bab2675a96008b0bf
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

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

%package     -n %{name}+lab
Summary:        CSS color parser library - feature "lab"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lab-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/lab) = %{version}

%description -n %{name}+lab
This metapackage enables feature "lab" for the Rust csscolorparser crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+phf
Summary:        CSS color parser library - feature "phf" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-0.11/default) >= 0.11.0
Requires:       crate(phf-0.11/macros) >= 0.11.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/named-colors) = %{version}
Provides:       crate(%{pkgname}/phf) = %{version}

%description -n %{name}+phf
This metapackage enables feature "phf" for the Rust csscolorparser crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "named-colors" features.

%package     -n %{name}+rgb
Summary:        CSS color parser library - feature "rgb" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rgb-0.8/default) >= 0.8.33
Provides:       crate(%{pkgname}/rgb) = %{version}
Provides:       crate(%{pkgname}/rust-rgb) = %{version}

%description -n %{name}+rgb
This metapackage enables feature "rgb" for the Rust csscolorparser crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "rust-rgb" feature.

%package     -n %{name}+serde
Summary:        CSS color parser library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.139
Requires:       crate(serde-1/derive) >= 1.0.139
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust csscolorparser crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
