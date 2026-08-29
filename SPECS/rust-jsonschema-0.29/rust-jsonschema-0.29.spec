# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name jsonschema
%global full_version 0.29.0
%global pkgname jsonschema-0.29

Name:           rust-jsonschema-0.29
Version:        0.29.0
Release:        %autorelease
Summary:        Rust crate "jsonschema"
License:        MIT
URL:            https://github.com/Stranger6667/jsonschema
#!RemoteAsset:  sha256:3c59cb1733c34377b6067a0419befd7f25073c5249ec3b0614a482bf499e1df5
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ahash-0.8/default) >= 0.8.0
Requires:       crate(ahash-0.8/serde) >= 0.8.0
Requires:       crate(base64-0.22/default) >= 0.22.0
Requires:       crate(bytecount-0.6/default) >= 0.6.0
Requires:       crate(bytecount-0.6/runtime-dispatch-simd) >= 0.6.0
Requires:       crate(email-address-0.2/default) >= 0.2.9
Requires:       crate(fancy-regex-0.14/default) >= 0.14.0
Requires:       crate(fraction-0.15/with-bigint) >= 0.15.0
Requires:       crate(idna-1/default) >= 1.0.2
Requires:       crate(itoa-1/default) >= 1.0.0
Requires:       crate(num-cmp-0.1/default) >= 0.1.0
Requires:       crate(once-cell-1/default) >= 1.20.1
Requires:       crate(percent-encoding-2/default) >= 2.3.0
Requires:       crate(referencing-0.29/default) >= 0.29.0
Requires:       crate(regex-syntax-0.8/default) >= 0.8.5
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(uuid-simd-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/resolve-file) = %{version}

%description
Source code for takopackized Rust crate "jsonschema"

%package     -n %{name}+default
Summary:        JSON schema validaton library - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/resolve-file) = %{version}
Requires:       crate(%{pkgname}/resolve-http) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust jsonschema crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+reqwest
Summary:        JSON schema validaton library - feature "reqwest" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(reqwest-0.12/blocking) >= 0.12.0
Requires:       crate(reqwest-0.12/json) >= 0.12.0
Provides:       crate(%{pkgname}/reqwest) = %{version}
Provides:       crate(%{pkgname}/resolve-http) = %{version}

%description -n %{name}+reqwest
This metapackage enables feature "reqwest" for the Rust jsonschema crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "resolve-http" feature.

%package     -n %{name}+resolve-async
Summary:        JSON schema validaton library - feature "resolve-async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-trait-0.1/default) >= 0.1.86
Requires:       crate(referencing-0.29/retrieve-async) >= 0.29.0
Requires:       crate(reqwest-0.12/blocking) >= 0.12.0
Requires:       crate(reqwest-0.12/default) >= 0.12.0
Requires:       crate(reqwest-0.12/json) >= 0.12.0
Requires:       crate(tokio-1/default) >= 1.0.0
Requires:       crate(tokio-1/fs) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Provides:       crate(%{pkgname}/resolve-async) = %{version}

%description -n %{name}+resolve-async
This metapackage enables feature "resolve-async" for the Rust jsonschema crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
