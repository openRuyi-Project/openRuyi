# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name url
%global full_version 2.5.8
%global pkgname url-2.0

Name:           rust-url-2.0
Version:        2.5.8
Release:        %autorelease
Summary:        Rust crate "url"
License:        MIT OR Apache-2.0
URL:            https://github.com/servo/rust-url
#!RemoteAsset:  sha256:ff67a8a4397373c3ef660812acab3268222035010ab8680ec4215f38ba3d0eed
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(form-urlencoded-1.0/alloc) >= 1.2.2
Requires:       crate(idna-1.0/alloc) >= 1.1.0
Requires:       crate(idna-1.0/compiled-data) >= 1.1.0
Requires:       crate(percent-encoding-2.0/alloc) >= 2.3.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/debugger-visualizer)
Provides:       crate(%{pkgname}/expose-internals)

%description
Source code for takopackized Rust crate "url"

%package     -n %{name}+serde
Summary:        URL library for Rust, based on the WHATWG URL Standard - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0) >= 1.0.228
Requires:       crate(serde-derive-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust url crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        URL library for Rust, based on the WHATWG URL Standard - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(form-urlencoded-1.0/alloc) >= 1.2.2
Requires:       crate(form-urlencoded-1.0/std) >= 1.2.2
Requires:       crate(idna-1.0/alloc) >= 1.1.0
Requires:       crate(idna-1.0/compiled-data) >= 1.1.0
Requires:       crate(idna-1.0/std) >= 1.1.0
Requires:       crate(percent-encoding-2.0/alloc) >= 2.3.2
Requires:       crate(percent-encoding-2.0/std) >= 2.3.2
Requires:       crate(serde-1.0/std) >= 1.0.228
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust url crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
