# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-url
%global full_version 0.32.0
%global pkgname gix-url-0.32

Name:           rust-gix-url-0.32
Version:        0.32.0
Release:        %autorelease
Summary:        Rust crate "gix-url"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:1b76a9d266254ad287ffd44467cd88e7868799b08f4d52e02d942b93e514d16f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(gix-features-0.43/default) >= 0.43.0
Requires:       crate(gix-path-0.10/default) >= 0.10.19
Requires:       crate(percent-encoding-2/default) >= 2.3.1
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(url-2/default) >= 2.5.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gix-url"

%package     -n %{name}+document-features
Summary:        The gitoxide project implementing parsing and serialization of gix-url - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-url crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        The gitoxide project implementing parsing and serialization of gix-url - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bstr-1/serde) >= 1.12.0
Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(serde-1/derive) >= 1.0.114
Requires:       crate(serde-1/std) >= 1.0.114
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-url crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
