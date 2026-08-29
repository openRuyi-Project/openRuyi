# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name kurbo
%global full_version 0.11.3
%global pkgname kurbo-0.11

Name:           rust-kurbo-0.11
Version:        0.11.3
Release:        %autorelease
Summary:        Rust crate "kurbo"
License:        Apache-2.0 OR MIT
URL:            https://github.com/linebender/kurbo
#!RemoteAsset:  sha256:c62026ae44756f8a599ba21140f350303d4f08dcdcc71b5ad9c9bb8128c13c62
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arrayvec-0.7) >= 0.7.6
Requires:       crate(smallvec-1/default) >= 1.15.1

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "kurbo"

%package     -n %{name}+euclid
Summary:        2D curves library - feature "euclid"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(euclid-0.22) >= 0.22.0
Provides:       crate(%{pkgname}/euclid) = %{version}

%description -n %{name}+euclid
This metapackage enables feature "euclid" for the Rust kurbo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        2D curves library - feature "libm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(euclid-0.22/libm) >= 0.22.0
Requires:       crate(libm-0.2/default) >= 0.2.15
Provides:       crate(%{pkgname}/libm) = %{version}

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust kurbo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mint
Summary:        2D curves library - feature "mint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mint-0.5/default) >= 0.5.9
Provides:       crate(%{pkgname}/mint) = %{version}

%description -n %{name}+mint
This metapackage enables feature "mint" for the Rust kurbo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+schemars
Summary:        2D curves library - feature "schemars"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(schemars-0.8/default) >= 0.8.22
Requires:       crate(schemars-0.8/smallvec) >= 0.8.22
Provides:       crate(%{pkgname}/schemars) = %{version}

%description -n %{name}+schemars
This metapackage enables feature "schemars" for the Rust kurbo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        2D curves library - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/alloc) >= 1.0.219
Requires:       crate(serde-1/derive) >= 1.0.219
Requires:       crate(smallvec-1/serde) >= 1.15.1
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust kurbo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        2D curves library - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(euclid-0.22/std) >= 0.22.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust kurbo crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
