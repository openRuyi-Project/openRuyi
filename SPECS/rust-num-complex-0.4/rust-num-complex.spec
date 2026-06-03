# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
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

Requires:       crate(num-traits-0.2/i128) >= 0.2.19
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "num-complex"

%package     -n %{name}+bytemuck
Summary:        Complex numbers implementation for Rust - feature "bytemuck"
Requires:       crate(%{pkgname})
Requires:       crate(bytemuck-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/bytemuck)

%description -n %{name}+bytemuck
This metapackage enables feature "bytemuck" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libm
Summary:        Complex numbers implementation for Rust - feature "libm"
Requires:       crate(%{pkgname})
Requires:       crate(num-traits-0.2/i128) >= 0.2.19
Requires:       crate(num-traits-0.2/libm) >= 0.2.19
Provides:       crate(%{pkgname}/libm)

%description -n %{name}+libm
This metapackage enables feature "libm" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rand
Summary:        Complex numbers implementation for Rust - feature "rand"
Requires:       crate(%{pkgname})
Requires:       crate(rand-0.8) >= 0.8.0
Provides:       crate(%{pkgname}/rand)

%description -n %{name}+rand
This metapackage enables feature "rand" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Complex numbers implementation for Rust - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Complex numbers implementation for Rust - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(num-traits-0.2/i128) >= 0.2.19
Requires:       crate(num-traits-0.2/std) >= 0.2.19
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust num-complex crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
