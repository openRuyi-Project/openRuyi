# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lexical-write-integer
%global full_version 1.0.6
%global pkgname lexical-write-integer-1

Name:           rust-lexical-write-integer-1
Version:        1.0.6
Release:        %autorelease
Summary:        Rust crate "lexical-write-integer"
License:        MIT OR Apache-2.0
URL:            https://github.com/Alexhuszagh/rust-lexical
#!RemoteAsset:  sha256:409851a618475d2d5796377cad353802345cba92c867d9fbcde9cf4eac4e14df
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lexical-util-1/write-integers) >= 1.0.7

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "lexical-write-integer"

%package     -n %{name}+compact
Summary:        Efficient formatting of integers to strings - feature "compact"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-1/compact) >= 1.0.7
Requires:       crate(lexical-util-1/write-integers) >= 1.0.7
Provides:       crate(%{pkgname}/compact) = %{version}

%description -n %{name}+compact
This metapackage enables feature "compact" for the Rust lexical-write-integer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+format
Summary:        Efficient formatting of integers to strings - feature "format"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-1/format) >= 1.0.7
Requires:       crate(lexical-util-1/write-integers) >= 1.0.7
Provides:       crate(%{pkgname}/format) = %{version}

%description -n %{name}+format
This metapackage enables feature "format" for the Rust lexical-write-integer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lint
Summary:        Efficient formatting of integers to strings - feature "lint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-1/lint) >= 1.0.7
Requires:       crate(lexical-util-1/write-integers) >= 1.0.7
Provides:       crate(%{pkgname}/lint) = %{version}

%description -n %{name}+lint
This metapackage enables feature "lint" for the Rust lexical-write-integer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+power-of-two
Summary:        Efficient formatting of integers to strings - feature "power-of-two"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-1/power-of-two) >= 1.0.7
Requires:       crate(lexical-util-1/write-integers) >= 1.0.7
Provides:       crate(%{pkgname}/power-of-two) = %{version}

%description -n %{name}+power-of-two
This metapackage enables feature "power-of-two" for the Rust lexical-write-integer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+radix
Summary:        Efficient formatting of integers to strings - feature "radix"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/power-of-two) = %{version}
Requires:       crate(lexical-util-1/radix) >= 1.0.7
Requires:       crate(lexical-util-1/write-integers) >= 1.0.7
Provides:       crate(%{pkgname}/radix) = %{version}

%description -n %{name}+radix
This metapackage enables feature "radix" for the Rust lexical-write-integer crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Efficient formatting of integers to strings - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-1/std) >= 1.0.7
Requires:       crate(lexical-util-1/write-integers) >= 1.0.7
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust lexical-write-integer crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
