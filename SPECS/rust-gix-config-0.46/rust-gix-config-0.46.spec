# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix-config
%global full_version 0.46.0
%global pkgname gix-config-0.46

Name:           rust-gix-config-0.46
Version:        0.46.0
Release:        %autorelease
Summary:        Rust crate "gix-config"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:5dfb898c5b695fd4acfc3c0ab638525a65545d47706064dcf7b5ead6cdb136c0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(gix-config-value-0.15/default) >= 0.15.1
Requires:       crate(gix-features-0.43/default) >= 0.43.0
Requires:       crate(gix-glob-0.21/default) >= 0.21.0
Requires:       crate(gix-path-0.10/default) >= 0.10.19
Requires:       crate(gix-ref-0.53/default) >= 0.53.0
Requires:       crate(gix-sec-0.12/default) >= 0.12.0
Requires:       crate(memchr-2/default) >= 2.0.0
Requires:       crate(once-cell-1/default) >= 1.21.3
Requires:       crate(smallvec-1/default) >= 1.15.1
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(unicode-bom-2/default) >= 2.0.3
Requires:       crate(winnow-0.7/default) >= 0.7.10
Requires:       crate(winnow-0.7/simd) >= 0.7.10
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "gix-config"

%package     -n %{name}+document-features
Summary:        Git-config file parser and editor from the gitoxide project - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix-config crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Git-config file parser and editor from the gitoxide project - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bstr-1/serde) >= 1.12.0
Requires:       crate(bstr-1/std) >= 1.12.0
Requires:       crate(gix-config-value-0.15/serde) >= 0.15.1
Requires:       crate(gix-glob-0.21/serde) >= 0.21.0
Requires:       crate(gix-ref-0.53/serde) >= 0.53.0
Requires:       crate(gix-sec-0.12/serde) >= 0.12.0
Requires:       crate(serde-1/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix-config crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
