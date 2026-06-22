# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ui_test
%global full_version 0.30.7
%global pkgname ui-test-0.30

Name:           rust-ui-test-0.30
Version:        0.30.7
Release:        %autorelease
Summary:        Rust crate "ui_test"
License:        MIT OR Apache-2.0
URL:            https://github.com/oli-obk/ui_test
#!RemoteAsset:  sha256:8c8811281d587a786747c0c49245925016c07767bc996305bdd34d5ce076786a
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(annotate-snippets-0.11/default) >= 0.11.2
Requires:       crate(anyhow-1/default) >= 1.0.6
Requires:       crate(bstr-1/default) >= 1.0.1
Requires:       crate(color-eyre-0.6/capture-spantrace) >= 0.6.1
Requires:       crate(colored-3/default) >= 3.1.0
Requires:       crate(comma-1/default) >= 1.0.0
Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.6
Requires:       crate(levenshtein-1/default) >= 1.0.5
Requires:       crate(prettydiff-0.9) >= 0.9.0
Requires:       crate(regex-1/unicode-gencat) >= 1.5.5
Requires:       crate(rustc-version-0.4/default) >= 0.4.0
Requires:       crate(rustfix-0.8/default) >= 0.8.1
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(spanned-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/gha) = %{version}

%description
Source code for takopackized Rust crate "ui_test"

%package     -n %{name}+default
Summary:        Test framework for testing rustc diagnostics output - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gha) = %{version}
Requires:       crate(%{pkgname}/indicatif) = %{version}
Requires:       crate(%{pkgname}/rustc) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ui_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indicatif
Summary:        Test framework for testing rustc diagnostics output - feature "indicatif"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indicatif-0.18/default) >= 0.18.3
Provides:       crate(%{pkgname}/indicatif) = %{version}

%description -n %{name}+indicatif
This metapackage enables feature "indicatif" for the Rust ui_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rustc
Summary:        Test framework for testing rustc diagnostics output - feature "rustc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(cargo-metadata-0.23/default) >= 0.23.0
Requires:       crate(cargo-platform-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/rustc) = %{version}

%description -n %{name}+rustc
This metapackage enables feature "rustc" for the Rust ui_test crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
