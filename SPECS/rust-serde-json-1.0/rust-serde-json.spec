# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serde_json
%global full_version 1.0.149
%global pkgname serde-json-1.0

Name:           rust-serde-json-1.0
Version:        1.0.149
Release:        %autorelease
Summary:        Rust crate "serde_json"
License:        MIT OR Apache-2.0
URL:            https://github.com/serde-rs/json
#!RemoteAsset:  sha256:83fc039473c5595ace860d8c4fafa220ff474b3fc6bfdb4293327f1a37e94d86
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(itoa-1.0/default) >= 1.0.18
Requires:       crate(memchr-2.0) >= 2.8.0
Requires:       crate(serde-1.0) >= 1.0.228
Requires:       crate(serde-core-1.0) >= 1.0.228
Requires:       crate(zmij-1.0/default) >= 1.0.21
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/arbitrary-precision)
Provides:       crate(%{pkgname}/float-roundtrip)
Provides:       crate(%{pkgname}/raw-value)
Provides:       crate(%{pkgname}/unbounded-depth)

%description
Source code for takopackized Rust crate "serde_json"

%package     -n %{name}+alloc
Summary:        JSON serialization file format - feature "alloc"
Requires:       crate(%{pkgname})
Requires:       crate(serde-core-1.0/alloc) >= 1.0.228
Provides:       crate(%{pkgname}/alloc)

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust serde_json crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        JSON serialization file format - feature "indexmap"
Requires:       crate(%{pkgname})
Requires:       crate(indexmap-2.0/default) >= 2.2.3
Provides:       crate(%{pkgname}/indexmap)

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust serde_json crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+preserve-order
Summary:        JSON serialization file format - feature "preserve_order"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/indexmap)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/preserve-order)

%description -n %{name}+preserve-order
This metapackage enables feature "preserve_order" for the Rust serde_json crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        JSON serialization file format - feature "std" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(memchr-2.0/std) >= 2.8.0
Requires:       crate(serde-core-1.0/std) >= 1.0.228
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust serde_json crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
