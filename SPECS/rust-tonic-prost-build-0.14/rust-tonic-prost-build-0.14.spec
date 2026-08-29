# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name tonic-prost-build
%global full_version 0.14.2
%global pkgname tonic-prost-build-0.14

Name:           rust-tonic-prost-build-0.14
Version:        0.14.2
Release:        %autorelease
Summary:        Rust crate "tonic-prost-build"
License:        MIT
URL:            https://github.com/hyperium/tonic
#!RemoteAsset:  sha256:b4a16cba4043dc3ff43fcb3f96b4c5c154c64cbd18ca8dce2ab2c6a451d058a2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(prettyplease-0.2/default) >= 0.2.0
Requires:       crate(proc-macro2-1/default) >= 1.0.0
Requires:       crate(prost-build-0.14/default) >= 0.14.0
Requires:       crate(prost-types-0.14/default) >= 0.14.0
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(tempfile-3/default) >= 3.0.0
Requires:       crate(tonic-build-0.14) >= 0.14.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "tonic-prost-build"

%package     -n %{name}+cleanup-markdown
Summary:        Prost build integration for tonic - feature "cleanup-markdown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prost-build-0.14/cleanup-markdown) >= 0.14.0
Provides:       crate(%{pkgname}/cleanup-markdown) = %{version}

%description -n %{name}+cleanup-markdown
This metapackage enables feature "cleanup-markdown" for the Rust tonic-prost-build crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Prost build integration for tonic - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cleanup-markdown) = %{version}
Requires:       crate(%{pkgname}/transport) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust tonic-prost-build crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+transport
Summary:        Prost build integration for tonic - feature "transport"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tonic-build-0.14/transport) >= 0.14.0
Provides:       crate(%{pkgname}/transport) = %{version}

%description -n %{name}+transport
This metapackage enables feature "transport" for the Rust tonic-prost-build crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
