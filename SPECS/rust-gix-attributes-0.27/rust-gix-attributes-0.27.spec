# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-attributes
%global full_version 0.27.0
%global pkgname gix-attributes-0.27

Name:           rust-gix-attributes-0.27
Version:        0.27.0
Release:        %autorelease
Summary:        Rust crate "gix-attributes"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:45442188216d08a5959af195f659cb1f244a50d7d2d0c3873633b1cd7135f638
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(bstr-1/unicode) >= 1.12.0
Requires:       crate(gix-glob-0.21/default) >= 0.21.0
Requires:       crate(gix-path-0.10/default) >= 0.10.19
Requires:       crate(gix-quote-0.6/default) >= 0.6.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.13
Requires:       crate(kstring-2/default) >= 2.0.0
Requires:       crate(smallvec-1/default) >= 1.15.1
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(unicode-bom-2/default) >= 2.0.3
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gix-attributes"

%package     -n %{name}+document-features
Summary:        The gitoxide project dealing .gitattributes files - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-attributes crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        The gitoxide project dealing .gitattributes files - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bstr-1/serde) >= 1.12.0
Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(bstr-1/unicode) >= 1.12.0
Requires:       crate(gix-glob-0.21/serde) >= 0.21.0
Requires:       crate(kstring-2/serde) >= 2.0.0
Requires:       crate(serde-1/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-attributes crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
