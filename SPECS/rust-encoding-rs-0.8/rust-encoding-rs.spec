# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name encoding_rs
%global full_version 0.8.35
%global pkgname encoding-rs-0.8

Name:           rust-encoding-rs-0.8
Version:        0.8.35
Release:        %autorelease
Summary:        Rust crate "encoding_rs"
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause
URL:            https://docs.rs/encoding_rs/
#!RemoteAsset:  sha256:75030f3c4f45dafd7586dd6780965a8c7e8e285a5ecb86713e63a79c5b2766f3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/fast-big5-hanzi-encode)
Provides:       crate(%{pkgname}/fast-gb-hanzi-encode)
Provides:       crate(%{pkgname}/fast-hangul-encode)
Provides:       crate(%{pkgname}/fast-hanja-encode)
Provides:       crate(%{pkgname}/fast-kanji-encode)
Provides:       crate(%{pkgname}/less-slow-big5-hanzi-encode)
Provides:       crate(%{pkgname}/less-slow-gb-hanzi-encode)
Provides:       crate(%{pkgname}/less-slow-kanji-encode)

%description
Source code for takopackized Rust crate "encoding_rs"

%package     -n %{name}+any-all-workaround
Summary:        Gecko-oriented implementation of the Encoding Standard - feature "any_all_workaround" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(any-all-workaround-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/any-all-workaround)
Provides:       crate(%{pkgname}/simd-accel)

%description -n %{name}+any-all-workaround
This metapackage enables feature "any_all_workaround" for the Rust encoding_rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "simd-accel" feature.

%package     -n %{name}+fast-legacy-encode
Summary:        Gecko-oriented implementation of the Encoding Standard - feature "fast-legacy-encode"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/fast-big5-hanzi-encode)
Requires:       crate(%{pkgname}/fast-gb-hanzi-encode)
Requires:       crate(%{pkgname}/fast-hangul-encode)
Requires:       crate(%{pkgname}/fast-hanja-encode)
Requires:       crate(%{pkgname}/fast-kanji-encode)
Provides:       crate(%{pkgname}/fast-legacy-encode)

%description -n %{name}+fast-legacy-encode
This metapackage enables feature "fast-legacy-encode" for the Rust encoding_rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Gecko-oriented implementation of the Encoding Standard - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust encoding_rs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
