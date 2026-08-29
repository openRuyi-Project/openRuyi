# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name num-complex
%global full_version 0.4.6
%global pkgname num-complex-0.4

Name:           rust-num-complex-0.4
Version:        0.4.6
Release:        %autorelease
Summary:        Rust crate "num-complex"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-num/num-complex
#!RemoteAsset:  sha256:73f88a1307638156682bada9d7604135552957b7818057dcef22705b4d509495
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(num-traits-0.2/i128) >= 0.2.18
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "num-complex"

%package     -n %{name}+bytecheck
Summary:        Complex numbers implementation for Rust - feature "bytecheck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytecheck-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/bytecheck) = %{version}

%description -n %{name}+bytecheck
This metapackage enables feature "bytecheck" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytemuck
Summary:        Complex numbers implementation for Rust - feature "bytemuck"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytemuck-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/bytemuck) = %{version}

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        Complex numbers implementation for Rust - feature "libm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2/i128) >= 0.2.18
Requires:       crate(num-traits-0.2/libm) >= 0.2.18
Provides:       crate(%{pkgname}/libm) = %{version}

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Complex numbers implementation for Rust - feature "rand"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rand-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/rand) = %{version}

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rkyv
Summary:        Complex numbers implementation for Rust - feature "rkyv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rkyv-0.7) >= 0.7.0
Provides:       crate(%{pkgname}/rkyv) = %{version}

%description -n %{name}+rkyv
This metapackage enables feature "rkyv" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Complex numbers implementation for Rust - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1) >= 1.0.0
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Complex numbers implementation for Rust - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(num-traits-0.2/i128) >= 0.2.18
Requires:       crate(num-traits-0.2/std) >= 0.2.18
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
