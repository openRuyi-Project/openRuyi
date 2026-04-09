# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name bit-vec
%global full_version 0.6.3
%global pkgname bit-vec-0.6

Name:           rust-bit-vec-0.6
Version:        0.6.3
Release:        %autorelease
Summary:        Rust crate "bit-vec"
License:        MIT/Apache-2.0
URL:            https://github.com/contain-rs/bit-vec
#!RemoteAsset:  sha256:349f9b6a179ed607305526ca489b34ad0a41aed5f7980fa90eb03160b69598fb
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "bit-vec"

%package     -n %{name}+serde
Summary:        Vector of bits - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust bit-vec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-no-std
Summary:        Vector of bits - feature "serde_no_std"
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/alloc) >= 1.0.0
Requires:       crate(serde-1.0/derive) >= 1.0.0
Provides:       crate(%{pkgname}/serde-no-std)

%description -n %{name}+serde-no-std
This metapackage enables feature "serde_no_std" for the Rust bit-vec crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde-std
Summary:        Vector of bits - feature "serde_std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(serde-1.0/derive) >= 1.0.0
Requires:       crate(serde-1.0/std) >= 1.0.0
Provides:       crate(%{pkgname}/serde-std)

%description -n %{name}+serde-std
This metapackage enables feature "serde_std" for the Rust bit-vec crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
