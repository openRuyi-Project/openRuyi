# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name zerocopy
%global full_version 0.8.48
%global pkgname zerocopy-0.8

Name:           rust-zerocopy-0.8
Version:        0.8.48
Release:        %autorelease
Summary:        Rust crate "zerocopy"
License:        BSD-2-Clause OR Apache-2.0 OR MIT
URL:            https://github.com/google/zerocopy
#!RemoteAsset:  sha256:eed437bf9d6692032087e337407a86f04cd8d6a16a37199ed57949d415bd68e9
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(zerocopy-derive-0.8/default) >= 0.8.48
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/float-nightly)
Provides:       crate(%{pkgname}/simd)
Provides:       crate(%{pkgname}/simd-nightly)
Provides:       crate(%{pkgname}/std)

%description
We write "unsafe" so you don't have to.
Source code for takopackized Rust crate "zerocopy"

%package     -n %{name}+internal-use-only-features-that-work-on-stable
Summary:        Zerocopy makes zero-cost memory manipulation effortless - feature "__internal_use_only_features_that_work_on_stable"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/derive)
Requires:       crate(%{pkgname}/simd)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/internal-use-only-features-that-work-on-stable)

%description -n %{name}+internal-use-only-features-that-work-on-stable
We write "unsafe" so you don't have to.
This metapackage enables feature "__internal_use_only_features_that_work_on_stable" for the Rust zerocopy crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zerocopy-derive
Summary:        Zerocopy makes zero-cost memory manipulation effortless - feature "zerocopy-derive" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(zerocopy-derive-0.8/default) >= 0.8.48
Provides:       crate(%{pkgname}/derive)
Provides:       crate(%{pkgname}/zerocopy-derive)

%description -n %{name}+zerocopy-derive
We write "unsafe" so you don't have to.
This metapackage enables feature "zerocopy-derive" for the Rust zerocopy crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
