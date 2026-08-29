# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name value-bag
%global full_version 1.12.0
%global pkgname value-bag-1

Name:           rust-value-bag-1
Version:        1.12.0
Release:        %autorelease
Summary:        Rust crate "value-bag"
License:        Apache-2.0 OR MIT
URL:            https://github.com/sval-rs/value-bag
#!RemoteAsset:  sha256:7ba6f5989077681266825251a52748b8c1d8a4ad098cc37e440103d0ea717fc0
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/inline-i128) = %{version}
Provides:       crate(%{pkgname}/inline-str) = %{version}
Provides:       crate(%{pkgname}/seq) = %{version}

%description
Source code for takopackized Rust crate "value-bag"

%package     -n %{name}+alloc
Summary:        Anonymous structured values - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(value-bag-serde1-1/alloc) >= 1.12.0
Requires:       crate(value-bag-sval2-1/alloc) >= 1.12.0
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust value-bag crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+owned
Summary:        Anonymous structured values - feature "owned"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(value-bag-serde1-1/owned) >= 1.12.0
Provides:       crate(%{pkgname}/owned) = %{version}

%description -n %{name}+owned
This metapackage enables feature "owned" for the Rust value-bag crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde1
Summary:        Anonymous structured values - feature "serde1" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/value-bag-serde1) = %{version}
Requires:       crate(value-bag-sval2-1/serde1) >= 1.12.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serde1) = %{version}

%description -n %{name}+serde1
This metapackage enables feature "serde1" for the Rust value-bag crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serde" feature.

%package     -n %{name}+std
Summary:        Anonymous structured values - feature "std" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(value-bag-serde1-1/std) >= 1.12.0
Requires:       crate(value-bag-sval2-1/std) >= 1.12.0
Provides:       crate(%{pkgname}/error) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/test) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust value-bag crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "error", and "test" features.

%package     -n %{name}+value-bag-serde1
Summary:        Anonymous structured values - feature "value-bag-serde1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(value-bag-serde1-1/default) >= 1.12.0
Provides:       crate(%{pkgname}/value-bag-serde1) = %{version}

%description -n %{name}+value-bag-serde1
This metapackage enables feature "value-bag-serde1" for the Rust value-bag crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+value-bag-sval2
Summary:        Anonymous structured values - feature "value-bag-sval2" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(value-bag-sval2-1/default) >= 1.12.0
Provides:       crate(%{pkgname}/sval) = %{version}
Provides:       crate(%{pkgname}/sval2) = %{version}
Provides:       crate(%{pkgname}/value-bag-sval2) = %{version}

%description -n %{name}+value-bag-sval2
This metapackage enables feature "value-bag-sval2" for the Rust value-bag crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "sval", and "sval2" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
