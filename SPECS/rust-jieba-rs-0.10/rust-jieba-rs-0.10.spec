# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jieba-rs
%global full_version 0.10.3
%global pkgname jieba-rs-0.10

Name:           rust-jieba-rs-0.10
Version:        0.10.3
Release:        %autorelease
Summary:        Rust crate "jieba-rs"
License:        MIT
URL:            https://github.com/messense/jieba-rs
#!RemoteAsset:  sha256:bb5bdea4dc241d589e179f39d2a778f31490f3370aa2f626223dbd930ebc5c9d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bytecount-0.6/default) >= 0.6.0
Requires:       crate(bytecount-0.6/runtime-dispatch-simd) >= 0.6.0
Requires:       crate(cedarwood-0.5/default) >= 0.5.0
Requires:       crate(jieba-macros-0.10/default) >= 0.10.0
Requires:       crate(phf-0.13/default) >= 0.13.1
Requires:       crate(regex-1/default) >= 1.11.2
Requires:       crate(rustc-hash-2/default) >= 2.1.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "jieba-rs"

%package     -n %{name}+default-dict
Summary:        Jieba Chinese Word Segmentation in Rust - feature "default-dict" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(include-flate-0.3/default) >= 0.3.1
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/default-dict) = %{version}

%description -n %{name}+default-dict
This metapackage enables feature "default-dict" for the Rust jieba-rs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+textrank
Summary:        Jieba Chinese Word Segmentation in Rust - feature "textrank"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ordered-float-5/default) >= 5.0.0
Provides:       crate(%{pkgname}/textrank) = %{version}

%description -n %{name}+textrank
This metapackage enables feature "textrank" for the Rust jieba-rs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tfidf
Summary:        Jieba Chinese Word Segmentation in Rust - feature "tfidf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(include-flate-0.3/default) >= 0.3.1
Requires:       crate(ordered-float-5/default) >= 5.0.0
Provides:       crate(%{pkgname}/tfidf) = %{version}

%description -n %{name}+tfidf
This metapackage enables feature "tfidf" for the Rust jieba-rs crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
