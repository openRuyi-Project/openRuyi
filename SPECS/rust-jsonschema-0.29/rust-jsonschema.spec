# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jsonschema
%global full_version 0.29.1
%global pkgname jsonschema-0.29

Name:           rust-jsonschema-0.29
Version:        0.29.1
Release:        %autorelease
Summary:        Rust crate "jsonschema"
License:        MIT
URL:            https://github.com/Stranger6667/jsonschema
#!RemoteAsset:  sha256:161c33c3ec738cfea3288c5c53dfcdb32fd4fc2954de86ea06f71b5a1a40bfcd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ahash-0.8/default) >= 0.8.12
Requires:       crate(ahash-0.8/serde) >= 0.8.12
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(bytecount-0.6/default) >= 0.6.9
Requires:       crate(bytecount-0.6/runtime-dispatch-simd) >= 0.6.9
Requires:       crate(email-address-0.2/default) >= 0.2.9
Requires:       crate(fancy-regex-0.14/default) >= 0.14.0
Requires:       crate(fraction-0.15/with-bigint) >= 0.15.3
Requires:       crate(idna-1.0/default) >= 1.0.3
Requires:       crate(itoa-1.0/default) >= 1.0.15
Requires:       crate(num-cmp-0.1/default) >= 0.1.0
Requires:       crate(once-cell-1.0/default) >= 1.21.3
Requires:       crate(percent-encoding-2.0/default) >= 2.3.1
Requires:       crate(referencing-0.29/default) >= 0.29.1
Requires:       crate(regex-syntax-0.8/default) >= 0.8.5
Requires:       crate(serde-1.0/default) >= 1.0.219
Requires:       crate(serde-1.0/derive) >= 1.0.219
Requires:       crate(serde-json-1.0/default) >= 1.0.140
Requires:       crate(uuid-simd-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/resolve-file)

%description
Source code for takopackized Rust crate "jsonschema"

%package     -n %{name}+default
Summary:        JSON schema validaton library - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/resolve-file)
Requires:       crate(%{pkgname}/resolve-http)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust jsonschema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+reqwest
Summary:        JSON schema validaton library - feature "reqwest" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(reqwest-0.12/blocking) >= 0.12.22
Requires:       crate(reqwest-0.12/json) >= 0.12.22
Provides:       crate(%{pkgname}/reqwest)
Provides:       crate(%{pkgname}/resolve-http)

%description -n %{name}+reqwest
This metapackage enables feature "reqwest" for the Rust jsonschema crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "resolve-http" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
