# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name prost-build
%global full_version 0.14.1
%global pkgname prost-build-0.14

Name:           rust-prost-build-0.14
Version:        0.14.1
Release:        %autorelease
Summary:        Rust crate "prost-build"
License:        Apache-2.0
URL:            https://github.com/tokio-rs/prost
#!RemoteAsset:  sha256:ac6c3320f9abac597dcbc668774ef006702672474aad53c6d596b62e487b40b1
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(heck-0.4/default) >= 0.4.0
Requires:       crate(itertools-0.10/use-alloc) >= 0.10.0
Requires:       crate(log-0.4/default) >= 0.4.4
Requires:       crate(multimap-0.8) >= 0.8.0
Requires:       crate(once-cell-1/default) >= 1.17.1
Requires:       crate(petgraph-0.6) >= 0.6.0
Requires:       crate(prost-0.14) >= 0.14.1
Requires:       crate(prost-types-0.14) >= 0.14.1
Requires:       crate(regex-1/std) >= 1.8.1
Requires:       crate(regex-1/unicode-bool) >= 1.8.1
Requires:       crate(tempfile-3/default) >= 3.0.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "prost-build"

%package     -n %{name}+cleanup-markdown
Summary:        Generate Prost annotated Rust types from Protocol Buffers files - feature "cleanup-markdown"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pulldown-cmark-0.13) >= 0.13.0
Requires:       crate(pulldown-cmark-to-cmark-21/default) >= 21.0.0
Provides:       crate(%{pkgname}/cleanup-markdown) = %{version}

%description -n %{name}+cleanup-markdown
This metapackage enables feature "cleanup-markdown" for the Rust prost-build crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+format
Summary:        Generate Prost annotated Rust types from Protocol Buffers files - feature "format" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prettyplease-0.2/default) >= 0.2.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/format) = %{version}

%description -n %{name}+format
This metapackage enables feature "format" for the Rust prost-build crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
