# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name phf_macros
%global full_version 0.14.0
%global pkgname phf-macros-0.14

Name:           rust-phf-macros-0.14
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "phf_macros"
License:        MIT
URL:            https://github.com/rust-phf/rust-phf
#!RemoteAsset:  sha256:5fa8d0ca26d424d27630da600c6624696e7dec8bf7b3b492b383c5dc49e5e085
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(phf-generator-0.14/default) >= 0.14.0
Requires:       crate(phf-shared-0.14) >= 0.14.0
Requires:       crate(proc-macro2-1/default) >= 1.0.95
Requires:       crate(quote-1/default) >= 1.0.0
Requires:       crate(syn-2/default) >= 2.0.0
Requires:       crate(syn-2/full) >= 2.0.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "phf_macros"

%package     -n %{name}+ptrhash
Summary:        Macros to generate types in the phf crate - feature "ptrhash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(phf-generator-0.14/ptrhash) >= 0.14.0
Provides:       crate(%{pkgname}/ptrhash) = %{version}

%description -n %{name}+ptrhash
This metapackage enables feature "ptrhash" for the Rust phf_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uncased
Summary:        Macros to generate types in the phf crate - feature "uncased"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/uncased-) = %{version}
Requires:       crate(phf-shared-0.14/uncased) >= 0.14.0
Provides:       crate(%{pkgname}/uncased) = %{version}

%description -n %{name}+uncased
This metapackage enables feature "uncased" for the Rust phf_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+uncased-
Summary:        Macros to generate types in the phf crate - feature "uncased_"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(uncased-0.9/default) >= 0.9.7
Provides:       crate(%{pkgname}/uncased-) = %{version}

%description -n %{name}+uncased-
This metapackage enables feature "uncased_" for the Rust phf_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicase
Summary:        Macros to generate types in the phf crate - feature "unicase"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/unicase-) = %{version}
Requires:       crate(phf-shared-0.14/unicase) >= 0.14.0
Provides:       crate(%{pkgname}/unicase) = %{version}

%description -n %{name}+unicase
This metapackage enables feature "unicase" for the Rust phf_macros crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicase-
Summary:        Macros to generate types in the phf crate - feature "unicase_"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(unicase-2/default) >= 2.4.0
Provides:       crate(%{pkgname}/unicase-) = %{version}

%description -n %{name}+unicase-
This metapackage enables feature "unicase_" for the Rust phf_macros crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
