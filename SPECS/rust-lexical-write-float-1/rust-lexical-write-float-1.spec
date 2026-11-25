# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lexical-write-float
%global full_version 1.0.6
%global pkgname lexical-write-float-1

Name:           rust-lexical-write-float-1
Version:        1.0.6
Release:        %autorelease
Summary:        Rust crate "lexical-write-float"
License:        MIT OR Apache-2.0
URL:            https://github.com/Alexhuszagh/rust-lexical
#!RemoteAsset:  sha256:50c438c87c013188d415fbabbb1dceb44249ab81664efbd31b14ae55dabb6361
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(lexical-util-1/write-floats) >= 1.0.7
Requires:       crate(lexical-write-integer-1) >= 1.0.6

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "lexical-write-float"

%package     -n %{name}+compact
Summary:        Efficient formatting of floats to strings - feature "compact"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-1/compact) >= 1.0.7
Requires:       crate(lexical-util-1/write-floats) >= 1.0.7
Requires:       crate(lexical-write-integer-1/compact) >= 1.0.6
Provides:       crate(%{pkgname}/compact) = %{version}

%description -n %{name}+compact
This metapackage enables feature "compact" for the Rust lexical-write-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+f128
Summary:        Efficient formatting of floats to strings - feature "f128"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-1/f128) >= 1.0.7
Requires:       crate(lexical-util-1/write-floats) >= 1.0.7
Provides:       crate(%{pkgname}/f128) = %{version}

%description -n %{name}+f128
This metapackage enables feature "f128" for the Rust lexical-write-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+f16
Summary:        Efficient formatting of floats to strings - feature "f16"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-1/f16) >= 1.0.7
Requires:       crate(lexical-util-1/write-floats) >= 1.0.7
Provides:       crate(%{pkgname}/f16) = %{version}

%description -n %{name}+f16
This metapackage enables feature "f16" for the Rust lexical-write-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+format
Summary:        Efficient formatting of floats to strings - feature "format"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-1/format) >= 1.0.7
Requires:       crate(lexical-util-1/write-floats) >= 1.0.7
Provides:       crate(%{pkgname}/format) = %{version}

%description -n %{name}+format
This metapackage enables feature "format" for the Rust lexical-write-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lint
Summary:        Efficient formatting of floats to strings - feature "lint"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-1/lint) >= 1.0.7
Requires:       crate(lexical-util-1/write-floats) >= 1.0.7
Requires:       crate(lexical-write-integer-1/lint) >= 1.0.6
Provides:       crate(%{pkgname}/lint) = %{version}

%description -n %{name}+lint
This metapackage enables feature "lint" for the Rust lexical-write-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+power-of-two
Summary:        Efficient formatting of floats to strings - feature "power-of-two"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-1/power-of-two) >= 1.0.7
Requires:       crate(lexical-util-1/write-floats) >= 1.0.7
Requires:       crate(lexical-write-integer-1/power-of-two) >= 1.0.6
Provides:       crate(%{pkgname}/power-of-two) = %{version}

%description -n %{name}+power-of-two
This metapackage enables feature "power-of-two" for the Rust lexical-write-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+radix
Summary:        Efficient formatting of floats to strings - feature "radix"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/power-of-two) = %{version}
Requires:       crate(lexical-util-1/radix) >= 1.0.7
Requires:       crate(lexical-util-1/write-floats) >= 1.0.7
Requires:       crate(lexical-write-integer-1/radix) >= 1.0.6
Provides:       crate(%{pkgname}/radix) = %{version}

%description -n %{name}+radix
This metapackage enables feature "radix" for the Rust lexical-write-float crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Efficient formatting of floats to strings - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(lexical-util-1/std) >= 1.0.7
Requires:       crate(lexical-util-1/write-floats) >= 1.0.7
Requires:       crate(lexical-write-integer-1/std) >= 1.0.6
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust lexical-write-float crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
