# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name purl
%global full_version 0.1.6
%global pkgname purl-0.1

Name:           rust-purl-0.1
Version:        0.1.6
Release:        %autorelease
Summary:        Rust crate "purl"
License:        MIT
URL:            https://github.com/phylum-dev/purl/
#!RemoteAsset:  sha256:60ebe4262ae91ddd28c8721111a0a6e9e58860e211fc92116c4bb85c98fd96ad
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hex-0.4/default) >= 0.4.3
Requires:       crate(percent-encoding-2/default) >= 2.2.0
Requires:       crate(thiserror-2/default) >= 2.0.12
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "purl"

%package     -n %{name}+default
Summary:        Package URL implementation with customizable package types - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/package-type) = %{version}
Requires:       crate(%{pkgname}/smartstring) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust purl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+package-type
Summary:        Package URL implementation with customizable package types - feature "package-type"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/phf) = %{version}
Requires:       crate(%{pkgname}/unicase) = %{version}
Provides:       crate(%{pkgname}/package-type) = %{version}

%description -n %{name}+package-type
This metapackage enables feature "package-type" for the Rust purl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+phf
Summary:        Package URL implementation with customizable package types - feature "phf"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-0.11/default) >= 0.11.1
Requires:       crate(phf-0.11/macros) >= 0.11.1
Requires:       crate(phf-0.11/unicase) >= 0.11.1
Provides:       crate(%{pkgname}/phf) = %{version}

%description -n %{name}+phf
This metapackage enables feature "phf" for the Rust purl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Package URL implementation with customizable package types - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.150
Requires:       crate(serde-1/derive) >= 1.0.150
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust purl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+smartstring
Summary:        Package URL implementation with customizable package types - feature "smartstring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(smartstring-1/default) >= 1.0.1
Provides:       crate(%{pkgname}/smartstring) = %{version}

%description -n %{name}+smartstring
This metapackage enables feature "smartstring" for the Rust purl crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicase
Summary:        Package URL implementation with customizable package types - feature "unicase"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicase-2/default) >= 2.6.0
Provides:       crate(%{pkgname}/unicase) = %{version}

%description -n %{name}+unicase
This metapackage enables feature "unicase" for the Rust purl crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
